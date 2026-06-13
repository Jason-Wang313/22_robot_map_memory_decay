#!/usr/bin/env python3
"""Runnable evidence for Causal-Exposure Memory Decay (CEMD).

The experiment is a small mechanistic simulator, not a real-robot claim. A
robot navigates with an old map through a building-like graph. During the
robot's absence, unobserved activity can reach and invalidate some remembered
edges. Baselines distrust memory by no decay, fixed hazard, elapsed age, or
sensor uncertainty. CEMD distrusts memory by the estimated physical exposure
opportunity for change.
"""

from __future__ import annotations

import csv
import heapq
import json
import math
import random
import statistics
import sys
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Set, Tuple

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
DOCS = ROOT / "docs"
for path in (RESULTS, FIGURES, DOCS):
    path.mkdir(exist_ok=True)

PROGRESS = RESULTS / "evidence_progress.json"
HAZARD_STRESS_TABLE = RESULTS / "hazard_misspecification_table.tex"


METHOD_ORDER = [
    "no_decay",
    "fixed_hazard",
    "age_decay",
    "uncertainty_only",
    "cemd",
    "oracle_prob",
]

METHOD_LABELS = {
    "no_decay": "No decay",
    "fixed_hazard": "Fixed hazard",
    "age_decay": "Age decay",
    "uncertainty_only": "Uncertainty only",
    "cemd": "CEMD",
    "oracle_prob": "Oracle prob.",
}


@dataclass
class Edge:
    eid: int
    u: int
    v: int
    length: float
    zone: str
    access: float
    age_days: float
    sensor_uncertainty: float
    exposure_true: float = 0.0
    exposure_est: float = 0.0
    closure_prob: float = 0.0
    closed: bool = False


@dataclass
class World:
    width: int
    height: int
    edges: List[Edge]
    adj: Dict[int, List[Tuple[int, int]]] = field(default_factory=dict)
    start: int = 0
    goal: int = 0

    def __post_init__(self) -> None:
        self.rebuild_adj()

    def rebuild_adj(self) -> None:
        self.adj = {i: [] for i in range(self.width * self.height)}
        for edge in self.edges:
            self.adj[edge.u].append((edge.v, edge.eid))
            self.adj[edge.v].append((edge.u, edge.eid))

    def xy(self, node: int) -> Tuple[int, int]:
        return node % self.width, node // self.width

    def edge_between(self, a: int, b: int) -> Optional[int]:
        for nb, eid in self.adj[a]:
            if nb == b:
                return eid
        return None


def save_progress(stage: str, **kwargs: object) -> None:
    payload = {"stage": stage, **kwargs}
    PROGRESS.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def zone_for_edge(width: int, height: int, u: int, v: int) -> Tuple[str, float]:
    ux, uy = u % width, u // width
    vx, vy = v % width, v // width
    mx, my = (ux + vx) / 2.0, (uy + vy) / 2.0
    if abs(my - (height // 2)) < 0.35 or abs(mx - (width // 2)) < 0.35:
        return "public_corridor", 1.0
    if mx < 1.3 or my < 1.3:
        return "entrance_area", 0.8
    if mx > width - 2.3 and my > height - 2.3:
        return "locked_storage", 0.08
    if (int(mx) + int(my)) % 5 == 0:
        return "service_room", 0.25
    return "office", 0.42


def make_base_world(rng: random.Random, width: int = 7, height: int = 6) -> World:
    edges: List[Edge] = []
    eid = 0

    def maybe_add(u: int, v: int, forced: bool = False) -> None:
        nonlocal eid
        ux, uy = u % width, u // width
        vx, vy = v % width, v // width
        is_corridor = uy == height // 2 or ux == width // 2 or vy == height // 2 or vx == width // 2
        p = 0.93 if is_corridor else 0.72
        if forced or rng.random() < p:
            zone, access = zone_for_edge(width, height, u, v)
            base_len = 1.0 + 0.15 * rng.random()
            if zone == "locked_storage":
                base_len += 0.15
            edges.append(
                Edge(
                    eid=eid,
                    u=u,
                    v=v,
                    length=base_len,
                    zone=zone,
                    access=access,
                    age_days=rng.uniform(2.0, 120.0),
                    sensor_uncertainty=min(1.0, max(0.0, rng.betavariate(2.2, 3.5))),
                )
            )
            eid += 1

    # Force the central cross and a perimeter backbone, then add many optional edges.
    for y in range(height):
        for x in range(width):
            node = y * width + x
            if x + 1 < width:
                forced = y == height // 2 or y in (0, height - 1)
                maybe_add(node, node + 1, forced=forced)
            if y + 1 < height:
                forced = x == width // 2 or x in (0, width - 1)
                maybe_add(node, node + width, forced=forced)
    world = World(width=width, height=height, edges=edges)
    return ensure_connected(world, rng)


def ensure_connected(world: World, rng: random.Random) -> World:
    width, height = world.width, world.height

    def components() -> List[Set[int]]:
        unseen = set(range(width * height))
        comps: List[Set[int]] = []
        while unseen:
            start = unseen.pop()
            comp = {start}
            q = deque([start])
            while q:
                cur = q.popleft()
                for nb, _ in world.adj[cur]:
                    if nb in unseen:
                        unseen.remove(nb)
                        comp.add(nb)
                        q.append(nb)
            comps.append(comp)
        return comps

    world.rebuild_adj()
    eid = len(world.edges)
    comps = components()
    while len(comps) > 1:
        a = comps[0]
        b = comps[1]
        best_pair = None
        best_dist = 999
        for u in a:
            ux, uy = world.xy(u)
            for v in b:
                vx, vy = world.xy(v)
                dist = abs(ux - vx) + abs(uy - vy)
                if dist == 1 and dist < best_dist:
                    best_pair = (u, v)
                    best_dist = dist
        if best_pair is None:
            best_pair = (next(iter(a)), next(iter(b)))
        u, v = best_pair
        zone, access = zone_for_edge(width, height, u, v)
        world.edges.append(
            Edge(
                eid=eid,
                u=u,
                v=v,
                length=1.1,
                zone=zone,
                access=access,
                age_days=rng.uniform(2.0, 120.0),
                sensor_uncertainty=min(1.0, max(0.0, rng.betavariate(2.2, 3.5))),
            )
        )
        eid += 1
        world.rebuild_adj()
        comps = components()
    return world


def simulate_exposure(world: World, rng: random.Random, absence_days: float, noise: float) -> None:
    sources = [0, world.width - 1, (world.height - 1) * world.width, world.height * world.width - 1]
    counts = defaultdict(float)
    walk_count = int(50 + 3.0 * absence_days)
    for _ in range(walk_count):
        node = rng.choice(sources)
        steps = rng.randint(4, 18)
        for _step in range(steps):
            choices = world.adj[node]
            if not choices:
                break
            nb, eid = rng.choice(choices)
            edge = world.edges[eid]
            if rng.random() <= edge.access:
                counts[eid] += 1.0
                node = nb
            else:
                break

    max_count = max(counts.values() or [1.0])
    for edge in world.edges:
        raw = counts[edge.eid] / max_count
        zone_gain = {
            "public_corridor": 1.35,
            "entrance_area": 1.05,
            "office": 0.72,
            "service_room": 0.38,
            "locked_storage": 0.08,
        }[edge.zone]
        edge.exposure_true = raw * zone_gain * (absence_days / 20.0)
        noisy = edge.exposure_true * (1.0 + rng.gauss(0.0, noise))
        edge.exposure_est = max(0.0, noisy)


def sample_closures(world: World, rng: random.Random, absence_days: float) -> None:
    for edge in world.edges:
        base = {
            "public_corridor": 0.0025,
            "entrance_area": 0.0022,
            "office": 0.0015,
            "service_room": 0.0018,
            "locked_storage": 0.0004,
        }[edge.zone]
        hazard = base * absence_days + 0.32 * edge.exposure_true
        edge.closure_prob = min(0.78, 1.0 - math.exp(-hazard))
        edge.closed = rng.random() < edge.closure_prob


def component_nodes(world: World, use_closed: bool = True) -> List[Set[int]]:
    unseen = set(range(world.width * world.height))
    comps: List[Set[int]] = []
    while unseen:
        start = unseen.pop()
        comp = {start}
        q = deque([start])
        while q:
            cur = q.popleft()
            for nb, eid in world.adj[cur]:
                if use_closed and world.edges[eid].closed:
                    continue
                if nb in unseen:
                    unseen.remove(nb)
                    comp.add(nb)
                    q.append(nb)
        comps.append(comp)
    return comps


def choose_task(world: World, rng: random.Random) -> None:
    comps = sorted(component_nodes(world, use_closed=True), key=len, reverse=True)
    largest = list(comps[0])
    best_pair = (largest[0], largest[-1])
    best_dist = -1
    for _ in range(200):
        a, b = rng.sample(largest, 2)
        ax, ay = world.xy(a)
        bx, by = world.xy(b)
        dist = abs(ax - bx) + abs(ay - by)
        if dist > best_dist:
            best_pair = (a, b)
            best_dist = dist
    world.start, world.goal = best_pair


def generate_world(seed: int, exposure_noise: float = 0.35) -> Tuple[World, float]:
    rng = random.Random(seed)
    world = make_base_world(rng)
    absence_days = rng.uniform(15.0, 140.0)
    simulate_exposure(world, rng, absence_days=absence_days, noise=exposure_noise)
    sample_closures(world, rng, absence_days=absence_days)
    # Ensure a feasible current task by selecting endpoints inside the largest current component.
    choose_task(world, rng)
    return world, absence_days


def calibrations(world: World) -> Dict[str, float]:
    target = max(0.01, min(0.65, statistics.mean(edge.closure_prob for edge in world.edges)))
    mean_age = max(1e-6, statistics.mean(edge.age_days for edge in world.edges))
    mean_uncertainty = max(1e-6, statistics.mean(edge.sensor_uncertainty for edge in world.edges))
    mean_exposure = max(1e-6, statistics.mean(edge.exposure_est for edge in world.edges))
    return {
        "target": target,
        "age_lambda": -math.log(1.0 - target) / mean_age,
        "uncertainty_scale": target / mean_uncertainty,
        "exposure_lambda": -math.log(1.0 - target) / mean_exposure,
    }


def risk_estimator(method: str, world: World) -> Callable[[Edge], float]:
    cal = calibrations(world)
    target = cal["target"]
    if method == "no_decay":
        return lambda _edge: 0.0
    if method == "fixed_hazard":
        return lambda _edge: target
    if method == "age_decay":
        lam = cal["age_lambda"]
        return lambda edge: min(0.85, 1.0 - math.exp(-lam * edge.age_days))
    if method == "uncertainty_only":
        scale = cal["uncertainty_scale"]
        return lambda edge: min(0.85, max(0.0, scale * edge.sensor_uncertainty))
    if method == "cemd":
        lam = cal["exposure_lambda"]
        return lambda edge: min(0.85, 1.0 - math.exp(-lam * edge.exposure_est))
    if method == "oracle_prob":
        return lambda edge: edge.closure_prob
    raise ValueError(f"unknown method: {method}")


def shortest_path(
    world: World,
    start: int,
    goal: int,
    blocked_known: Set[int],
    risk: Callable[[Edge], float],
    failure_penalty: float,
    use_true_closed: bool = False,
) -> Tuple[Optional[List[int]], float]:
    pq: List[Tuple[float, int, List[int]]] = [(0.0, start, [])]
    best = {start: 0.0}
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if cost > best.get(node, float("inf")):
            continue
        for nb, eid in world.adj[node]:
            edge = world.edges[eid]
            if eid in blocked_known:
                continue
            if use_true_closed and edge.closed:
                continue
            w = edge.length + failure_penalty * risk(edge)
            new_cost = cost + w
            if new_cost < best.get(nb, float("inf")):
                best[nb] = new_cost
                heapq.heappush(pq, (new_cost, nb, path + [eid]))
    return None, float("inf")


def other_node(edge: Edge, node: int) -> int:
    return edge.v if edge.u == node else edge.u


def execute_method(world: World, method: str, failure_penalty: float = 18.0) -> Dict[str, float]:
    risk = risk_estimator(method, world)
    oracle_path, oracle_len = shortest_path(
        world,
        world.start,
        world.goal,
        blocked_known=set(),
        risk=lambda _edge: 0.0,
        failure_penalty=0.0,
        use_true_closed=True,
    )
    budget = 1.75 * oracle_len + 22.0 if oracle_path is not None else 9999.0
    known_blocked: Set[int] = set()
    current = world.start
    travelled = 0.0
    replans = 0
    collisions = 0
    planned_blocked_edges = 0
    risk_sum = 0.0
    max_iterations = 80

    for _iteration in range(max_iterations):
        if current == world.goal:
            break
        path, expected_cost = shortest_path(
            world,
            current,
            world.goal,
            blocked_known=known_blocked,
            risk=risk,
            failure_penalty=failure_penalty,
            use_true_closed=False,
        )
        replans += 1
        if path is None:
            return {
                "success": 0.0,
                "travel_cost": travelled,
                "oracle_cost": oracle_len,
                "regret": travelled - oracle_len if math.isfinite(oracle_len) else travelled,
                "collisions": float(collisions),
                "replans": float(replans),
                "planned_blocked_edges": float(planned_blocked_edges),
                "expected_plan_cost": expected_cost,
                "risk_sum": risk_sum,
                "budget": budget,
            }
        progressed = False
        for eid in path:
            edge = world.edges[eid]
            risk_sum += risk(edge)
            if edge.closed:
                collisions += 1
                planned_blocked_edges += 1
                known_blocked.add(eid)
                travelled += failure_penalty + 0.35 * edge.length
                progressed = True
                break
            travelled += edge.length
            current = other_node(edge, current)
            progressed = True
            if current == world.goal:
                break
            if travelled > budget:
                return {
                    "success": 0.0,
                    "travel_cost": travelled,
                    "oracle_cost": oracle_len,
                    "regret": travelled - oracle_len,
                    "collisions": float(collisions),
                    "replans": float(replans),
                    "planned_blocked_edges": float(planned_blocked_edges),
                    "expected_plan_cost": expected_cost,
                    "risk_sum": risk_sum,
                    "budget": budget,
                }
        if not progressed:
            break

    success = 1.0 if current == world.goal and travelled <= budget else 0.0
    return {
        "success": success,
        "travel_cost": travelled,
        "oracle_cost": oracle_len,
        "regret": travelled - oracle_len,
        "collisions": float(collisions),
        "replans": float(replans),
        "planned_blocked_edges": float(planned_blocked_edges),
        "expected_plan_cost": expected_cost if "expected_cost" in locals() else 0.0,
        "risk_sum": risk_sum,
        "budget": budget,
    }


def summarize(rows: Sequence[Dict[str, float]]) -> List[Dict[str, float]]:
    by_method: Dict[str, List[Dict[str, float]]] = defaultdict(list)
    for row in rows:
        by_method[str(row["method"])].append(row)
    summary: List[Dict[str, float]] = []
    for method in METHOD_ORDER:
        items = by_method[method]
        if not items:
            continue
        summary.append(
            {
                "method": method,
                "episodes": float(len(items)),
                "success_rate": statistics.mean(float(r["success"]) for r in items),
                "mean_travel_cost": statistics.mean(float(r["travel_cost"]) for r in items),
                "median_travel_cost": statistics.median(float(r["travel_cost"]) for r in items),
                "mean_regret": statistics.mean(float(r["regret"]) for r in items),
                "mean_collisions": statistics.mean(float(r["collisions"]) for r in items),
                "mean_replans": statistics.mean(float(r["replans"]) for r in items),
                "mean_planned_blocked_edges": statistics.mean(float(r["planned_blocked_edges"]) for r in items),
                "mean_risk_sum": statistics.mean(float(r["risk_sum"]) for r in items),
            }
        )
    return summary


def write_csv(path: Path, rows: Sequence[Dict[str, object]], fieldnames: Sequence[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def run_episode_set(n_episodes: int, seed: int, exposure_noise: float) -> Tuple[List[Dict[str, object]], List[Dict[str, object]]]:
    episode_rows: List[Dict[str, object]] = []
    edge_rows: List[Dict[str, object]] = []
    for ep in range(n_episodes):
        world_seed = seed + ep * 37
        world, absence_days = generate_world(world_seed, exposure_noise=exposure_noise)
        for edge in world.edges:
            edge_rows.append(
                {
                    "episode": ep,
                    "edge": edge.eid,
                    "zone": edge.zone,
                    "age_days": edge.age_days,
                    "sensor_uncertainty": edge.sensor_uncertainty,
                    "exposure_true": edge.exposure_true,
                    "exposure_est": edge.exposure_est,
                    "closure_prob": edge.closure_prob,
                    "closed": int(edge.closed),
                    "absence_days": absence_days,
                }
            )
        for method in METHOD_ORDER:
            metrics = execute_method(world, method)
            row: Dict[str, object] = {
                "episode": ep,
                "method": method,
                "seed": world_seed,
                "absence_days": absence_days,
                "start": world.start,
                "goal": world.goal,
            }
            row.update(metrics)
            episode_rows.append(row)
        if ep % 50 == 0:
            save_progress("episodes", completed=ep, total=n_episodes, exposure_noise=exposure_noise)
    return episode_rows, edge_rows


def run_noise_stress(noises: Sequence[float], n_episodes: int = 180, seed: int = 9000) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for ni, noise in enumerate(noises):
        ep_rows, _edge_rows = run_episode_set(n_episodes, seed + ni * 10000, exposure_noise=noise)
        for summary_row in summarize(ep_rows):
            summary_row = dict(summary_row)
            summary_row["exposure_noise"] = noise
            rows.append(summary_row)
        save_progress("noise_stress", completed=ni + 1, total=len(noises), noise=noise)
    return rows


def calibrate_component_scores(scores: Sequence[float], target: float) -> List[float]:
    mean_score = max(1e-9, statistics.mean(scores))
    scale = target / mean_score
    return [min(0.78, max(0.0, scale * score)) for score in scores]


def resample_closures_with_hazard_mix(world: World, rng: random.Random, exposure_weight: float) -> None:
    target = max(0.02, min(0.55, statistics.mean(edge.closure_prob for edge in world.edges)))
    exposure_scores = [1.0 - math.exp(-0.45 * edge.exposure_true) for edge in world.edges]
    age_scores = [1.0 - math.exp(-0.035 * edge.age_days) for edge in world.edges]
    exposure_probs = calibrate_component_scores(exposure_scores, target)
    age_probs = calibrate_component_scores(age_scores, target)
    for edge, exposure_prob, age_prob in zip(world.edges, exposure_probs, age_probs):
        mixed_prob = exposure_weight * exposure_prob + (1.0 - exposure_weight) * age_prob
        edge.closure_prob = min(0.78, max(0.0, mixed_prob))
        edge.closed = rng.random() < edge.closure_prob
    choose_task(world, rng)


def run_hazard_misspecification_stress(
    exposure_weights: Sequence[float],
    n_episodes: int = 160,
    seed: int = 66000,
) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for wi, exposure_weight in enumerate(exposure_weights):
        episode_rows: List[Dict[str, object]] = []
        for ep in range(n_episodes):
            world_seed = seed + wi * 10000 + ep * 37
            world, absence_days = generate_world(world_seed, exposure_noise=0.35)
            resample_rng = random.Random(world_seed + 991)
            resample_closures_with_hazard_mix(world, resample_rng, exposure_weight)
            for method in METHOD_ORDER:
                metrics = execute_method(world, method)
                row: Dict[str, object] = {
                    "episode": ep,
                    "method": method,
                    "seed": world_seed,
                    "absence_days": absence_days,
                    "hazard_exposure_weight": exposure_weight,
                }
                row.update(metrics)
                episode_rows.append(row)
        for summary_row in summarize(episode_rows):
            summary_row = dict(summary_row)
            summary_row["hazard_exposure_weight"] = exposure_weight
            rows.append(summary_row)
        save_progress(
            "hazard_misspecification_stress",
            completed=wi + 1,
            total=len(exposure_weights),
            exposure_weight=exposure_weight,
        )
    return rows


def write_hazard_misspecification_table(hazard_rows: Sequence[Dict[str, float]]) -> None:
    by_key = {
        (float(row["hazard_exposure_weight"]), str(row["method"])): float(row["success_rate"])
        for row in hazard_rows
    }
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{V2 hazard-misspecification stress. The true closure process is resampled so hazards range from exposure-driven (1.00) to age-driven (0.00), while CEMD still plans with exposure estimates. Success is mission completion rate.}",
        r"\label{tab:hazard-misspecification}",
        r"\begin{tabular}{lrrrr}",
        r"\toprule",
        r"Exposure share & CEMD & Age decay & Uncertainty only & Oracle \\",
        r"\midrule",
    ]
    for exposure_weight in sorted({float(row["hazard_exposure_weight"]) for row in hazard_rows}, reverse=True):
        lines.append(
            f"{exposure_weight:.2f} & "
            f"{by_key[(exposure_weight, 'cemd')]:.3f} & "
            f"{by_key[(exposure_weight, 'age_decay')]:.3f} & "
            f"{by_key[(exposure_weight, 'uncertainty_only')]:.3f} & "
            f"{by_key[(exposure_weight, 'oracle_prob')]:.3f} \\\\"
        )
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}"])
    HAZARD_STRESS_TABLE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def formal_counterexample() -> Dict[str, object]:
    age = 30.0
    beta = 0.35
    failure_penalty = 80.0
    safe = {"length": 11.0, "age": age, "exposure": 0.05}
    exposed = {"length": 8.6, "age": age, "exposure": 3.8}

    def p(edge: Dict[str, float]) -> float:
        return 1.0 - math.exp(-beta * edge["exposure"])

    safe_expected = safe["length"] + failure_penalty * p(safe)
    exposed_expected = exposed["length"] + failure_penalty * p(exposed)
    age_only_safe = safe["length"]
    age_only_exposed = exposed["length"]
    age_only_choice_route = "exposed_shortcut" if age_only_exposed < age_only_safe else "safe_detour"
    exposure_aware_choice_route = "safe_detour" if safe_expected < exposed_expected else "exposed_shortcut"
    return {
        "age_days_equal": age,
        "safe_exposure": safe["exposure"],
        "exposed_exposure": exposed["exposure"],
        "safe_true_change_prob": p(safe),
        "exposed_true_change_prob": p(exposed),
        "safe_true_expected_cost": safe_expected,
        "exposed_true_expected_cost": exposed_expected,
        "age_only_cost_safe": age_only_safe,
        "age_only_cost_exposed": age_only_exposed,
        "age_only_choice_route": age_only_choice_route,
        "exposure_aware_choice_route": exposure_aware_choice_route,
        "choice_code_note": "For legacy numeric fields, 1.0 means the condition named in the field is true.",
        "age_only_chooses_exposed_shortcut": 1.0 if age_only_exposed < age_only_safe else 0.0,
        "exposure_aware_chooses_safe_detour": 1.0 if safe_expected < exposed_expected else 0.0,
        "expected_cost_gap_if_age_only_chooses_exposed": exposed_expected - safe_expected,
    }


def make_plots(
    summary_rows: Sequence[Dict[str, float]],
    edge_rows: Sequence[Dict[str, object]],
    stress_rows: Sequence[Dict[str, float]],
    hazard_rows: Sequence[Dict[str, float]],
) -> None:
    labels = [METHOD_LABELS[row["method"]] for row in summary_rows]
    x = np.arange(len(labels))
    success = [row["success_rate"] for row in summary_rows]
    collisions = [row["mean_collisions"] for row in summary_rows]
    regret = [row["mean_regret"] for row in summary_rows]

    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.3))
    colors = ["#777777", "#9aa3b2", "#4c78a8", "#f58518", "#54a24b", "#b279a2"]
    axes[0].bar(x, success, color=colors[: len(x)])
    axes[0].set_ylim(0, 1.02)
    axes[0].set_title("Mission success")
    axes[0].set_ylabel("rate")
    axes[1].bar(x, collisions, color=colors[: len(x)])
    axes[1].set_title("Blocked-edge encounters")
    axes[1].set_ylabel("per episode")
    axes[2].bar(x, regret, color=colors[: len(x)])
    axes[2].set_title("Cost above oracle")
    axes[2].set_ylabel("travel cost")
    for ax in axes:
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=35, ha="right")
        ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "aggregate_results.png", dpi=200)
    plt.close(fig)

    exp = np.array([float(r["exposure_true"]) for r in edge_rows])
    prob = np.array([float(r["closure_prob"]) for r in edge_rows])
    closed = np.array([float(r["closed"]) for r in edge_rows])
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    ax.scatter(exp, prob, s=7, alpha=0.12, label="edge probability", color="#4c78a8")
    bins = np.linspace(0, max(0.01, exp.max()), 12)
    centers = []
    empirical = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        mask = (exp >= lo) & (exp < hi)
        if mask.sum() >= 10:
            centers.append((lo + hi) / 2.0)
            empirical.append(float(closed[mask].mean()))
    if centers:
        ax.plot(centers, empirical, color="#e45756", marker="o", label="empirical closures")
    ax.set_xlabel("true unobserved exposure")
    ax.set_ylabel("change probability")
    ax.set_title("Exposure, not age alone, drives stale-map hazard")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(FIGURES / "exposure_calibration.png", dpi=200)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    for method in ["age_decay", "uncertainty_only", "cemd"]:
        xs = [float(r["exposure_noise"]) for r in stress_rows if r["method"] == method]
        ys = [float(r["success_rate"]) for r in stress_rows if r["method"] == method]
        ax.plot(xs, ys, marker="o", label=METHOD_LABELS[method])
    ax.set_xlabel("multiplicative exposure-estimate noise")
    ax.set_ylabel("mission success")
    ax.set_ylim(0, 1.02)
    ax.set_title("Stress test: noisy exposure priors")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(FIGURES / "noise_stress.png", dpi=200)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    for method in ["age_decay", "uncertainty_only", "cemd", "oracle_prob"]:
        method_rows = sorted(
            [row for row in hazard_rows if row["method"] == method],
            key=lambda row: float(row["hazard_exposure_weight"]),
        )
        xs = [float(r["hazard_exposure_weight"]) for r in method_rows]
        ys = [float(r["success_rate"]) for r in method_rows]
        ax.plot(xs, ys, marker="o", label=METHOD_LABELS[method])
    ax.set_xlabel("true hazard exposure share")
    ax.set_ylabel("mission success")
    ax.set_ylim(0, 1.02)
    ax.set_title("Stress test: misspecified causal hazard")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(FIGURES / "hazard_misspecification.png", dpi=200)
    plt.close(fig)

    make_example_world_plot()


def make_example_world_plot() -> None:
    world, _absence = generate_world(12345, exposure_noise=0.35)
    risk = risk_estimator("cemd", world)
    fig, ax = plt.subplots(figsize=(6.0, 4.8))
    for edge in world.edges:
        ux, uy = world.xy(edge.u)
        vx, vy = world.xy(edge.v)
        color = "#d62728" if edge.closed else plt.cm.viridis(min(1.0, risk(edge)))
        lw = 3.8 if edge.closed else 1.2 + 3.0 * risk(edge)
        ax.plot([ux, vx], [-uy, -vy], color=color, linewidth=lw, alpha=0.85)
    sx, sy = world.xy(world.start)
    gx, gy = world.xy(world.goal)
    ax.scatter([sx], [-sy], s=120, color="#54a24b", label="start", zorder=3)
    ax.scatter([gx], [-gy], s=120, color="#e45756", label="goal", zorder=3)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Example stale map: red edges changed, width/color show CEMD risk")
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    fig.savefig(FIGURES / "example_world.png", dpi=200)
    plt.close(fig)


def write_evidence_summary(
    summary_rows: Sequence[Dict[str, float]],
    formal: Dict[str, object],
    stress_rows: Sequence[Dict[str, float]],
    hazard_rows: Sequence[Dict[str, float]],
) -> None:
    cemd = next(row for row in summary_rows if row["method"] == "cemd")
    age = next(row for row in summary_rows if row["method"] == "age_decay")
    uncertainty = next(row for row in summary_rows if row["method"] == "uncertainty_only")
    no_decay = next(row for row in summary_rows if row["method"] == "no_decay")
    worst_noise_cemd = [row for row in stress_rows if row["method"] == "cemd" and abs(float(row["exposure_noise"]) - 1.0) < 1e-9]
    stress_sentence = ""
    if worst_noise_cemd:
        stress_sentence = f" At exposure-noise 1.0, CEMD success is {worst_noise_cemd[0]['success_rate']:.3f}."
    age_driven_cemd = next(
        row
        for row in hazard_rows
        if row["method"] == "cemd" and abs(float(row["hazard_exposure_weight"]) - 0.0) < 1e-9
    )
    age_driven_age = next(
        row
        for row in hazard_rows
        if row["method"] == "age_decay" and abs(float(row["hazard_exposure_weight"]) - 0.0) < 1e-9
    )
    age_driven_uncertainty = next(
        row
        for row in hazard_rows
        if row["method"] == "uncertainty_only" and abs(float(row["hazard_exposure_weight"]) - 0.0) < 1e-9
    )
    content = f"""# Evidence Summary

## Experiment

The simulator instantiates a long-horizon mobile robot with a stale graph map of a building-like environment. During the robot's absence, unobserved activity walks through the environment and can close remembered traversable edges. Every method receives the same old map and differs only in how it converts stale memory into route risk.

## Main Aggregate

- No decay success: {no_decay['success_rate']:.3f}; mean collisions: {no_decay['mean_collisions']:.3f}; mean regret: {no_decay['mean_regret']:.3f}.
- Age decay success: {age['success_rate']:.3f}; mean collisions: {age['mean_collisions']:.3f}; mean regret: {age['mean_regret']:.3f}.
- Uncertainty-only success: {uncertainty['success_rate']:.3f}; mean collisions: {uncertainty['mean_collisions']:.3f}; mean regret: {uncertainty['mean_regret']:.3f}.
- CEMD success: {cemd['success_rate']:.3f}; mean collisions: {cemd['mean_collisions']:.3f}; mean regret: {cemd['mean_regret']:.3f}.{stress_sentence}

## V2 Hazard-Misspecification Stress

When true stale-map hazards are resampled to be age-driven rather than exposure-driven, CEMD is no longer advantaged by the simulator's causal variable. At exposure share 0.00, success is {age_driven_cemd['success_rate']:.3f} for CEMD, {age_driven_age['success_rate']:.3f} for age decay, and {age_driven_uncertainty['success_rate']:.3f} for uncertainty-only. This is the central failure boundary: CEMD is a useful memory-decay rule only when exposure is actually predictive of map invalidation.

## Formal Counterexample Check

Two route edges have equal age ({formal['age_days_equal']:.1f} days), but exposures {formal['safe_exposure']:.2f} and {formal['exposed_exposure']:.2f}. A monotone age-only rule assigns the same stale-memory risk and chooses the shorter exposed route. Under the exposure hazard model, the expected-cost gap from that choice is {formal['expected_cost_gap_if_age_only_chooses_exposed']:.3f}.

## Files

- `results/episode_results.csv`
- `results/aggregate_results.csv`
- `results/edge_exposure_samples.csv`
- `results/noise_stress_results.csv`
- `results/hazard_misspecification_results.csv`
- `results/formal_counterexample.json`
- `figures/aggregate_results.png`
- `figures/exposure_calibration.png`
- `figures/noise_stress.png`
- `figures/hazard_misspecification.png`
- `figures/example_world.png`
"""
    (DOCS / "evidence_summary.md").write_text(content, encoding="utf-8")


def main() -> int:
    try:
        save_progress("starting")
        episode_rows, edge_rows = run_episode_set(n_episodes=650, seed=22000, exposure_noise=0.35)
        summary_rows = summarize(episode_rows)
        stress_rows = run_noise_stress([0.0, 0.25, 0.5, 0.75, 1.0], n_episodes=160, seed=44000)
        hazard_rows = run_hazard_misspecification_stress([1.0, 0.75, 0.5, 0.25, 0.0], n_episodes=160, seed=66000)
        formal = formal_counterexample()

        write_csv(
            RESULTS / "episode_results.csv",
            episode_rows,
            [
                "episode",
                "method",
                "seed",
                "absence_days",
                "start",
                "goal",
                "success",
                "travel_cost",
                "oracle_cost",
                "regret",
                "collisions",
                "replans",
                "planned_blocked_edges",
                "expected_plan_cost",
                "risk_sum",
                "budget",
            ],
        )
        write_csv(
            RESULTS / "aggregate_results.csv",
            summary_rows,
            [
                "method",
                "episodes",
                "success_rate",
                "mean_travel_cost",
                "median_travel_cost",
                "mean_regret",
                "mean_collisions",
                "mean_replans",
                "mean_planned_blocked_edges",
                "mean_risk_sum",
            ],
        )
        write_csv(
            RESULTS / "edge_exposure_samples.csv",
            edge_rows,
            [
                "episode",
                "edge",
                "zone",
                "age_days",
                "sensor_uncertainty",
                "exposure_true",
                "exposure_est",
                "closure_prob",
                "closed",
                "absence_days",
            ],
        )
        write_csv(
            RESULTS / "noise_stress_results.csv",
            stress_rows,
            [
                "exposure_noise",
                "method",
                "episodes",
                "success_rate",
                "mean_travel_cost",
                "median_travel_cost",
                "mean_regret",
                "mean_collisions",
                "mean_replans",
                "mean_planned_blocked_edges",
                "mean_risk_sum",
            ],
        )
        write_csv(
            RESULTS / "hazard_misspecification_results.csv",
            hazard_rows,
            [
                "hazard_exposure_weight",
                "method",
                "episodes",
                "success_rate",
                "mean_travel_cost",
                "median_travel_cost",
                "mean_regret",
                "mean_collisions",
                "mean_replans",
                "mean_planned_blocked_edges",
                "mean_risk_sum",
            ],
        )
        write_hazard_misspecification_table(hazard_rows)
        (RESULTS / "formal_counterexample.json").write_text(json.dumps(formal, indent=2), encoding="utf-8")
        make_plots(summary_rows, edge_rows, stress_rows, hazard_rows)
        write_evidence_summary(summary_rows, formal, stress_rows, hazard_rows)
        save_progress("complete", episodes=650, stress_episodes=800, hazard_stress_episodes=800)
        print(json.dumps({"status": "complete", "episodes": 650, "stress_episodes": 800, "hazard_stress_episodes": 800}))
    except Exception as exc:  # noqa: BLE001
        save_progress("fatal_error", error=repr(exc))
        (RESULTS / "evidence_error.txt").write_text(repr(exc), encoding="utf-8")
        print(json.dumps({"status": "fatal_error", "error": repr(exc)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
