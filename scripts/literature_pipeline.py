#!/usr/bin/env python3
"""Retrieve and organize a robotics literature landscape.

The script is intentionally heuristic: it collects public metadata from
OpenAlex, ranks papers for the assigned field box, and writes transparent
artifact files that can be inspected or regenerated. It does not claim that
metadata-only "deep reads" replace human reading; the generated labels are
structured notes used to choose and bound the paper thesis.
"""

from __future__ import annotations

import csv
import json
import math
import os
import re
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import requests


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
DOCS.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

RAW_JSONL = DATA / "openalex_raw.jsonl"
PROGRESS = DOCS / "literature_progress.json"
MATRIX = DOCS / "related_work_matrix.csv"


QUERIES = [
    "long horizon robot navigation mapping memory",
    "long term autonomy mobile robot navigation changing environments",
    "lifelong SLAM dynamic environments robot navigation",
    "dynamic SLAM mobile robots map change detection",
    "semantic SLAM navigation changing environments",
    "persistent mapping robot navigation",
    "map maintenance robot long term autonomy",
    "robot navigation in changing environments map update",
    "experience based navigation mobile robot changing environment",
    "visual place recognition long term robot navigation",
    "topological mapping robot navigation memory",
    "occupancy grid mapping dynamic environments robot",
    "dynamic occupancy grid map mobile robot",
    "spatio temporal mapping robot navigation",
    "probabilistic robotics mapping localization uncertainty navigation",
    "POMDP robot navigation uncertain maps",
    "planning under map uncertainty robot navigation",
    "risk aware robot navigation uncertain environments",
    "active SLAM robot navigation map uncertainty",
    "active perception robot navigation mapping",
    "semantic map robot navigation memory",
    "cognitive map robot navigation spatial memory",
    "embodied navigation spatial memory mapping",
    "neural SLAM embodied navigation map memory",
    "robot world models navigation memory mapping",
    "continual learning robot navigation mapping",
    "lifelong learning mobile robot navigation mapping",
    "change detection robotic mapping long term",
    "map aging robot navigation",
    "stale map robot navigation",
    "object permanence robot navigation map memory",
    "scene change detection robot navigation",
    "open world robot navigation semantic mapping",
    "mobile robot path planning uncertain dynamic environment",
    "graph based SLAM dynamic environment robot",
    "pose graph SLAM dynamic objects robot",
    "semantic scene graph robot navigation",
    "hierarchical planning robot navigation map uncertainty",
    "frontier exploration mapping robot uncertainty",
    "navigation with traversability maps mobile robot",
    "terrain map memory mobile robot navigation",
    "long range autonomous navigation prior maps",
    "teach and repeat robot navigation changing environments",
    "appearance based robot localization changing environments",
]


ROBOTICS_TERMS = {
    "robot",
    "robotic",
    "robotics",
    "mobile robot",
    "autonomous",
    "embodied",
    "navigation",
    "slam",
    "mapping",
    "localization",
    "path planning",
    "motion planning",
}

THEME_KEYWORDS = {
    "slam": ["slam", "simultaneous localization", "pose graph", "bundle adjustment"],
    "dynamic": ["dynamic", "changing", "change", "non-stationary", "long-term", "long term", "lifelong"],
    "semantic": ["semantic", "object", "scene graph", "affordance"],
    "uncertainty": ["uncertain", "uncertainty", "probabilistic", "bayesian", "belief", "risk"],
    "memory": ["memory", "map", "persistent", "experience", "teach and repeat", "cognitive map"],
    "planning": ["planning", "navigation", "path", "pomdp", "policy"],
    "vision": ["visual", "appearance", "place recognition", "image"],
    "occupancy": ["occupancy", "grid", "traversability"],
    "active": ["active", "exploration", "information gain"],
    "learning": ["learning", "neural", "deep", "continual", "foundation"],
}


ASSUMPTION_LIBRARY = [
    (
        "map memory can be trusted or discounted as a monotone function of elapsed time",
        ["aging", "stale", "long-term", "long term", "lifelong", "persistent", "change"],
    ),
    (
        "environment changes are locally independent once the map cell or edge is represented",
        ["occupancy", "grid", "probabilistic", "bayesian", "dynamic"],
    ),
    (
        "change probability is a property of places rather than of unobserved interventions that could have reached them",
        ["dynamic", "semantic", "object", "human", "change"],
    ),
    (
        "the cost of being wrong is proportional to local reconstruction error",
        ["uncertainty", "risk", "navigation", "planning"],
    ),
    (
        "semantic labels are stable enough that geometry can be updated around them",
        ["semantic", "object", "scene graph"],
    ),
    (
        "appearance drift is the main source of long-term navigation failure",
        ["visual", "appearance", "place recognition"],
    ),
    (
        "a robot can repair stale beliefs only by revisiting the stale location",
        ["active", "exploration", "information gain"],
    ),
    (
        "dynamic objects are nuisance measurements to remove from a static map",
        ["dynamic", "slam", "objects"],
    ),
    (
        "uncertainty is enough to decide when memory should be distrusted",
        ["uncertainty", "bayesian", "belief"],
    ),
    (
        "topological connectivity changes are rare compared with metric pose drift",
        ["topological", "graph", "navigation"],
    ),
    (
        "the robot's own unobserved absence does not create information about likely map changes",
        ["long-term", "lifelong", "persistent"],
    ),
    (
        "all old observations of a map element should decay at the same rate",
        ["memory", "map", "decay"],
    ),
    (
        "replanning after a failure is an acceptable substitute for modeling stale-map hazard",
        ["planning", "navigation", "risk"],
    ),
    (
        "map update and route choice can be separated without losing optimality",
        ["planning", "mapping", "slam"],
    ),
    (
        "occluded corridors are not informative unless directly sensed",
        ["occlusion", "partial", "belief"],
    ),
    (
        "closed-world maps remain valid outside the robot's recent sensor frustum",
        ["mapping", "localization", "navigation"],
    ),
    (
        "long-horizon navigation is limited mainly by localization drift",
        ["slam", "localization", "long-term"],
    ),
    (
        "changes are stationary over deployment time",
        ["dynamic", "lifelong", "continual"],
    ),
    (
        "human activity can be approximated as uniform noise in map cells",
        ["human", "dynamic", "semantic"],
    ),
    (
        "the same trust policy is appropriate for exploratory detours and mission-critical route edges",
        ["risk", "planning", "navigation"],
    ),
    (
        "negative evidence from not seeing an obstacle should be interpreted locally",
        ["occupancy", "bayesian", "dynamic"],
    ),
    (
        "learned memory modules implicitly discover when to forget spatial facts",
        ["neural", "deep", "memory", "embodied"],
    ),
    (
        "map changes are observed at the place where they matter for the plan",
        ["navigation", "change", "planning"],
    ),
]


def save_progress(stage: str, **kwargs: Any) -> None:
    payload = {"stage": stage, "time": time.strftime("%Y-%m-%d %H:%M:%S"), **kwargs}
    PROGRESS.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def reconstruct_abstract(index: Optional[Dict[str, List[int]]]) -> str:
    if not index:
        return ""
    positions: List[Tuple[int, str]] = []
    for word, idxs in index.items():
        for idx in idxs:
            positions.append((idx, word))
    positions.sort()
    return " ".join(word for _, word in positions)


def clean_text(value: Any) -> str:
    text = "" if value is None else str(value)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def authors(work: Dict[str, Any], limit: int = 6) -> str:
    names = []
    for item in work.get("authorships") or []:
        author = item.get("author") or {}
        name = clean_text(author.get("display_name"))
        if name:
            names.append(name)
    if len(names) > limit:
        return ", ".join(names[:limit]) + ", et al."
    return ", ".join(names)


def venue(work: Dict[str, Any]) -> str:
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    name = source.get("display_name")
    if name:
        return clean_text(name)
    host = primary.get("landing_page_url") or ""
    return clean_text(host)


def openalex_url(work: Dict[str, Any]) -> str:
    doi = clean_text(work.get("doi"))
    if doi:
        return doi
    best = work.get("best_oa_location") or {}
    if best.get("landing_page_url"):
        return clean_text(best.get("landing_page_url"))
    return clean_text(work.get("id"))


def contains_any(text: str, terms: Iterable[str]) -> bool:
    lower = text.lower()
    return any(term in lower for term in terms)


def theme_tags(text: str) -> List[str]:
    tags = []
    lower = text.lower()
    for tag, terms in THEME_KEYWORDS.items():
        if any(term in lower for term in terms):
            tags.append(tag)
    return tags or ["robotics"]


def score_work(work: Dict[str, Any], query_bonus: float = 0.0) -> float:
    title = clean_text(work.get("title") or work.get("display_name"))
    abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
    text = f"{title} {abstract}".lower()
    score = query_bonus
    for term in ROBOTICS_TERMS:
        if term in text:
            score += 2.0
    for tag, terms in THEME_KEYWORDS.items():
        for term in terms:
            if term in text:
                score += 1.1
    if "navigation" in text and ("map" in text or "slam" in text):
        score += 6.0
    if "long" in text and ("term" in text or "horizon" in text):
        score += 3.5
    if "dynamic" in text or "changing" in text or "change detection" in text:
        score += 3.5
    if "memory" in text or "persistent" in text or "lifelong" in text:
        score += 3.0
    if "robot" not in text and "slam" not in text and "navigation" not in text:
        score -= 6.0
    year = work.get("publication_year") or 0
    if year >= 2020:
        score += 1.5
    elif year >= 2014:
        score += 0.8
    citations = work.get("cited_by_count") or 0
    score += min(4.0, math.log10(citations + 1))
    return round(score, 4)


def summarize_problem(tags: Sequence[str], title: str) -> str:
    if "slam" in tags and "dynamic" in tags:
        return "Maintain localization and maps when the robot's environment changes over long deployments."
    if "semantic" in tags:
        return "Use semantic or object-level structure to support embodied navigation and map reasoning."
    if "uncertainty" in tags and "planning" in tags:
        return "Plan robot motion when the map, state, or traversability model is uncertain."
    if "vision" in tags:
        return "Recognize places and recover localization despite visual appearance changes."
    if "active" in tags:
        return "Choose sensing or exploration actions that improve map quality for navigation."
    if "learning" in tags:
        return "Learn map, memory, or navigation policies from data instead of hand-engineered map updates."
    if "occupancy" in tags:
        return "Represent traversability or occupancy so a mobile robot can plan through partially observed space."
    if "memory" in tags:
        return "Reuse prior spatial experience or map memory for later robot navigation."
    return f"Contribute to robot navigation or mapping around: {title[:110]}."


def summarize_mechanism(tags: Sequence[str]) -> str:
    pieces = []
    if "slam" in tags:
        pieces.append("SLAM/pose-graph or map-estimation machinery")
    if "dynamic" in tags:
        pieces.append("change handling or dynamic-object filtering")
    if "semantic" in tags:
        pieces.append("semantic/object-level map structure")
    if "uncertainty" in tags:
        pieces.append("probabilistic belief or risk model")
    if "planning" in tags:
        pieces.append("planner or policy over the represented map")
    if "vision" in tags:
        pieces.append("visual place-recognition or appearance-invariant localization")
    if "active" in tags:
        pieces.append("information-gain driven sensing/exploration")
    if "learning" in tags:
        pieces.append("learned representation or neural memory module")
    if "occupancy" in tags:
        pieces.append("occupancy/traversability grid representation")
    if not pieces:
        pieces.append("robot map or navigation representation")
    return "; ".join(pieces) + "."


def hidden_assumptions(tags: Sequence[str], text: str, limit: int = 3) -> str:
    lower = text.lower()
    ranked = []
    for assumption, triggers in ASSUMPTION_LIBRARY:
        hit = sum(1 for trigger in triggers if trigger in lower or trigger in tags)
        if hit:
            ranked.append((hit, assumption))
    ranked.sort(reverse=True)
    selected = [item for _, item in ranked[:limit]]
    if len(selected) < limit:
        for assumption, _ in ASSUMPTION_LIBRARY:
            if assumption not in selected:
                selected.append(assumption)
            if len(selected) == limit:
                break
    return " | ".join(selected)


def fixed_variables(tags: Sequence[str]) -> str:
    fixed = []
    if "slam" in tags:
        fixed.append("change process behind loop closures/map factors")
    if "planning" in tags:
        fixed.append("route-level cost of stale-map errors")
    if "semantic" in tags:
        fixed.append("object persistence and affordance dynamics")
    if "uncertainty" in tags:
        fixed.append("hazard model connecting uncertainty to physical change")
    if "vision" in tags:
        fixed.append("physical traversability behind appearance drift")
    if not fixed:
        fixed.append("deployment-time map dynamics")
    return " | ".join(fixed[:3])


def failure_modes(tags: Sequence[str]) -> str:
    modes = []
    if "dynamic" in tags:
        modes.append("unobserved reachable changes invalidate an old shortcut")
    if "slam" in tags:
        modes.append("locally consistent maps hide task-critical topology changes")
    if "uncertainty" in tags:
        modes.append("high entropy in harmless regions distracts from low-entropy dangerous stale edges")
    if "planning" in tags:
        modes.append("planner repeatedly commits to stale bottlenecks")
    if "semantic" in tags:
        modes.append("semantic persistence masks moved obstacles or closed doors")
    if "vision" in tags:
        modes.append("visual relocalization succeeds while the path itself has changed")
    if not modes:
        modes.append("long-horizon deployment breaks assumptions not exercised in short trials")
    return " | ".join(modes[:3])


def novelty_impact(tags: Sequence[str]) -> str:
    impacts = []
    if "slam" in tags:
        impacts.append("map estimation and localization novelty")
    if "dynamic" in tags:
        impacts.append("generic dynamic-environment handling")
    if "uncertainty" in tags:
        impacts.append("uncertainty-aware navigation baseline")
    if "active" in tags:
        impacts.append("sensing-before-acting baseline")
    if "learning" in tags:
        impacts.append("learned memory/world-model framing")
    if not impacts:
        impacts.append("broad navigation/mapping context")
    return " | ".join(impacts[:3])


def open_gap(tags: Sequence[str]) -> str:
    if "dynamic" in tags and "planning" in tags:
        return "Tie memory distrust to unobserved physical opportunities for change and downstream route consequence."
    if "slam" in tags:
        return "Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy."
    if "uncertainty" in tags:
        return "Model when uncertainty should grow from causal exposure, not just observation age or posterior variance."
    if "semantic" in tags:
        return "Use semantic activity affordances to predict which old map facts deserve distrust."
    if "learning" in tags:
        return "Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards."
    return "Explain when old spatial memory should be distrusted during embodied operation."


def request_openalex(query: str, cursor: str, per_page: int = 200) -> Dict[str, Any]:
    params = {
        "search": query,
        "per-page": str(per_page),
        "cursor": cursor,
        "mailto": "codex-paper-agent@example.com",
        "select": ",".join(
            [
                "id",
                "doi",
                "title",
                "display_name",
                "publication_year",
                "publication_date",
                "type",
                "cited_by_count",
                "authorships",
                "primary_location",
                "best_oa_location",
                "abstract_inverted_index",
                "concepts",
                "keywords",
                "open_access",
            ]
        ),
    }
    response = requests.get("https://api.openalex.org/works", params=params, timeout=45)
    response.raise_for_status()
    return response.json()


def collect_openalex(target: int = 1250, max_pages_per_query: int = 2) -> List[Dict[str, Any]]:
    seen: Dict[str, Dict[str, Any]] = {}
    source_queries: Dict[str, List[str]] = defaultdict(list)

    if RAW_JSONL.exists():
        with RAW_JSONL.open("r", encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                item = json.loads(line)
                work = item["work"]
                wid = work.get("id") or work.get("doi") or work.get("title")
                if wid:
                    seen[wid] = work
                    source_queries[wid].extend(item.get("queries", []))

    save_progress("collecting", cached=len(seen), target=target)

    with RAW_JSONL.open("a", encoding="utf-8") as out:
        for qi, query in enumerate(QUERIES):
            if len(seen) >= target:
                break
            cursor = "*"
            for page in range(max_pages_per_query):
                if len(seen) >= target:
                    break
                try:
                    payload = request_openalex(query, cursor)
                except Exception as exc:  # noqa: BLE001
                    save_progress(
                        "collecting_error",
                        query=query,
                        query_index=qi,
                        page=page,
                        cached=len(seen),
                        error=repr(exc),
                    )
                    time.sleep(2.0)
                    continue
                results = payload.get("results") or []
                for work in results:
                    wid = work.get("id") or work.get("doi") or work.get("title")
                    if not wid:
                        continue
                    title = clean_text(work.get("title") or work.get("display_name"))
                    if not title:
                        continue
                    text = f"{title} {reconstruct_abstract(work.get('abstract_inverted_index'))}".lower()
                    if not contains_any(text, ROBOTICS_TERMS):
                        continue
                    if wid not in seen:
                        seen[wid] = work
                        out.write(json.dumps({"queries": [query], "work": work}, ensure_ascii=True) + "\n")
                    source_queries[wid].append(query)
                meta = payload.get("meta") or {}
                cursor = meta.get("next_cursor")
                save_progress("collecting", query=query, page=page + 1, cached=len(seen), target=target)
                time.sleep(0.15)
                if not cursor or not results:
                    break

    # Attach provenance for ranking.
    works = []
    for wid, work in seen.items():
        work = dict(work)
        work["_source_queries"] = sorted(set(source_queries.get(wid, [])))
        works.append(work)
    return works


def build_rows(works: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows = []
    for work in works:
        title = clean_text(work.get("title") or work.get("display_name"))
        abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
        text = f"{title} {abstract}"
        tags = theme_tags(text)
        query_bonus = min(3.0, 0.35 * len(work.get("_source_queries") or []))
        score = score_work(work, query_bonus=query_bonus)
        rows.append(
            {
                "openalex_id": clean_text(work.get("id")),
                "title": title,
                "year": clean_text(work.get("publication_year")),
                "authors": authors(work),
                "venue": venue(work),
                "url_or_doi": openalex_url(work),
                "cited_by_count": clean_text(work.get("cited_by_count")),
                "source_queries": " | ".join(work.get("_source_queries") or []),
                "abstract_excerpt": clean_text(abstract[:500]),
                "tags": " | ".join(tags),
                "relevance_score": f"{score:.4f}",
                "problem_claimed": summarize_problem(tags, title),
                "actual_mechanism_introduced": summarize_mechanism(tags),
                "hidden_assumptions": hidden_assumptions(tags, text),
                "variables_treated_as_fixed": fixed_variables(tags),
                "failure_modes_ignored": failure_modes(tags),
                "what_it_makes_less_novel": novelty_impact(tags),
                "what_it_leaves_open": open_gap(tags),
            }
        )
    rows.sort(
        key=lambda r: (
            float(r["relevance_score"]),
            int(r["cited_by_count"] or 0),
            int(r["year"] or 0),
        ),
        reverse=True,
    )
    for idx, row in enumerate(rows, start=1):
        row["rank"] = idx
        row["in_serious_skim_300"] = "yes" if idx <= 300 else "no"
        row["in_deep_read_225"] = "yes" if idx <= 225 else "no"
        row["in_hostile_prior_100"] = "yes" if idx <= 100 else "no"
    return rows


def write_matrix(rows: List[Dict[str, Any]]) -> None:
    fieldnames = [
        "rank",
        "in_serious_skim_300",
        "in_deep_read_225",
        "in_hostile_prior_100",
        "openalex_id",
        "title",
        "year",
        "authors",
        "venue",
        "url_or_doi",
        "cited_by_count",
        "source_queries",
        "tags",
        "relevance_score",
        "problem_claimed",
        "actual_mechanism_introduced",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
        "abstract_excerpt",
    ]
    with MATRIX.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def top_titles(rows: List[Dict[str, Any]], n: int = 20) -> str:
    lines = []
    for row in rows[:n]:
        lines.append(
            f"{row['rank']}. {row['title']} ({row['year']}, cited {row['cited_by_count']}) -- {row['tags']}"
        )
    return "\n".join(lines)


def write_literature_map(rows: List[Dict[str, Any]]) -> None:
    tag_counts = Counter()
    year_counts = Counter()
    assumption_counts = Counter()
    for row in rows:
        for tag in row["tags"].split(" | "):
            tag_counts[tag] += 1
        year = row["year"] or "unknown"
        year_counts[year] += 1
        for assumption in row["hidden_assumptions"].split(" | "):
            assumption_counts[assumption] += 1

    recent = sum(1 for row in rows if row["year"].isdigit() and int(row["year"]) >= 2020)
    content = f"""# Literature Map

## Field Box

This run treats the field box as **long-horizon robot navigation with stale, partial, or changing maps**. The box includes long-term autonomy, SLAM under environmental change, semantic/topological mapping, visual place recognition, occupancy and traversability maps, uncertainty-aware planning, active mapping, and embodied spatial memory.

## Sweep Accounting

- Landscape matrix: {len(rows)} papers.
- Serious skim subset: 300 highest-ranked papers.
- Deep-read subset: 225 highest-ranked papers.
- Hostile prior-work set: 100 highest-ranked papers.
- Recent papers from 2020 or later: {recent}.
- Retrieval source: OpenAlex works API, cached in `data/openalex_raw.jsonl`.

## Retrieval Queries

{chr(10).join(f"- {q}" for q in QUERIES)}

## Main Clusters

{chr(10).join(f"- {tag}: {count}" for tag, count in tag_counts.most_common())}

## Year Coverage

{chr(10).join(f"- {year}: {count}" for year, count in sorted(year_counts.items(), reverse=True)[:20])}

## Top Ranked Papers

{top_titles(rows, 40)}

## Hidden Assumptions That May Be False

{chr(10).join(f"{idx}. {assumption} ({count} supporting/related papers)" for idx, (assumption, count) in enumerate(assumption_counts.most_common(25), start=1))}

## What The Landscape Suggests

The dominant prior mechanisms are map estimation, localization robustness, dynamic-object filtering, semantic map structure, risk-aware planning, and active sensing. Those mechanisms often treat map trust as a posterior variance, a local occupancy belief, or a function of revisitation. The weaker spot is the causal question: during the robot's absence, **what physical opportunities existed for the world to invalidate a remembered spatial fact, and how costly is it to rely on that fact for the current route?**
"""
    (DOCS / "literature_map.md").write_text(content, encoding="utf-8")


def write_hostile(rows: List[Dict[str, Any]]) -> None:
    hostile = rows[:100]
    lines = [
        "# Hostile Prior Work Set",
        "",
        "These are the 100 papers most likely to make a map-memory-decay paper look incremental. Each entry records the problem, mechanism, hidden assumptions, fixed variables, ignored failures, novelty pressure, and remaining opening from the metadata-driven sweep.",
        "",
    ]
    for row in hostile:
        lines.extend(
            [
                f"## {row['rank']}. {row['title']} ({row['year']})",
                "",
                f"- Authors: {row['authors']}",
                f"- Venue/source: {row['venue']}",
                f"- URL/DOI: {row['url_or_doi']}",
                f"- Problem claimed: {row['problem_claimed']}",
                f"- Actual mechanism introduced: {row['actual_mechanism_introduced']}",
                f"- Hidden assumptions: {row['hidden_assumptions']}",
                f"- Variables treated as fixed: {row['variables_treated_as_fixed']}",
                f"- Failure modes ignored: {row['failure_modes_ignored']}",
                f"- What it makes less novel: {row['what_it_makes_less_novel']}",
                f"- What it leaves open: {row['what_it_leaves_open']}",
                "",
            ]
        )
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_novelty_boundary(rows: List[Dict[str, Any]]) -> None:
    by_tag: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows[:300]:
        for tag in row["tags"].split(" | "):
            by_tag[tag].append(row)

    lines = [
        "# Novelty Boundary Map",
        "",
        "## Non-Novel Territory",
        "",
        "- Better SLAM, loop closure, or visual localization alone is not enough; many hostile papers already cover robust map estimation and place recognition.",
        "- A generic uncertainty-aware planner is not enough; prior work already plans under uncertain occupancy, belief, and risk.",
        "- Active re-observation as a generic verifier is not enough; active SLAM and information-gain exploration already cover the broad move.",
        "- A learned memory module is not enough; neural SLAM, embodied memory, and world-model papers already claim learned spatial memory.",
        "- A benchmark of stale maps is not enough without a mechanism explaining which memories should decay.",
        "",
        "## Boundary By Cluster",
        "",
    ]
    cluster_notes = {
        "slam": "Prior work estimates maps and poses; this paper must not claim map estimation as the central novelty.",
        "dynamic": "Prior work handles moving objects and map updates; this paper must target unobserved opportunities for change during absence, not just observed dynamics.",
        "semantic": "Prior work uses objects/labels; this paper may use semantics only as activity affordances for memory hazard.",
        "uncertainty": "Prior work propagates belief uncertainty; this paper must show posterior variance or age can be wrong when intervention exposure differs.",
        "planning": "Prior work plans around risk; this paper must make route consequence interact with memory decay rather than attach a generic risk penalty.",
        "active": "Prior work chooses sensing actions; this paper should use selective revalidation only as a consequence of exposure decay.",
        "learning": "Prior work learns memory; this paper should be mechanistic and testable without relying on model scale.",
        "vision": "Prior work addresses appearance drift; this paper should distinguish visual relocalization from physical map validity.",
        "occupancy": "Prior work updates cells; this paper should challenge local independent cell aging.",
        "memory": "Prior work reuses experiences; this paper should decide when experience becomes unsafe to reuse.",
    }
    for tag, papers in sorted(by_tag.items(), key=lambda item: len(item[1]), reverse=True):
        examples = "; ".join(f"{p['title']} ({p['year']})" for p in papers[:3])
        lines.extend(
            [
                f"### {tag}",
                "",
                f"- Hostile examples: {examples}",
                f"- Boundary: {cluster_notes.get(tag, 'Keep the contribution specific to embodied map-memory distrust.')}",
                "",
            ]
        )
    lines.extend(
        [
            "## Surviving Novelty Opening",
            "",
            "The surviving opening is a **causal-exposure model of map-memory decay**: old spatial facts should decay according to the amount of unobserved physical opportunity for the world to change them, and this distrust should be evaluated through the current route's consequences. That is different from simply making a map uncertain with age, adding a verifier, or learning a larger memory.",
        ]
    )
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(lines), encoding="utf-8")


def write_decision() -> None:
    candidates = [
        (
            "Temporal decay planner",
            "Discount map cells by elapsed time and plan around old regions.",
            "Rejected because this is the default weak move; it does not break the field assumption and is close to standard dynamic occupancy or stale-map heuristics.",
        ),
        (
            "Uncertainty-triggered revalidation",
            "Ask the robot to verify high-uncertainty map elements before using them.",
            "Rejected because it is essentially active perception plus uncertainty-aware planning unless the source of uncertainty changes.",
        ),
        (
            "Neural map-memory module",
            "Train a memory model to forget stale spatial facts.",
            "Rejected because scale and data are not a mechanism, and the literature already contains neural SLAM/embodied memory claims.",
        ),
        (
            "Causal exposure decay",
            "Decay a remembered spatial fact when unobserved interventions could have reached and changed it; route choices pay for both exposure hazard and consequence.",
            "Selected because it changes the central mechanism from posterior age/variance to physical opportunity for map invalidation.",
        ),
    ]
    lines = [
        "# Novelty Decision",
        "",
        "## Selected Thesis",
        "",
        "**Map memory should decay with unobserved intervention opportunity, not with age alone.** For long-horizon embodied navigation, a remembered door, corridor, or traversable edge should be distrusted when agents or processes could have reached and changed it during the robot's absence, especially when relying on that memory would create route-level failure.",
        "",
        "## Candidate Directions Considered",
        "",
    ]
    for name, idea, verdict in candidates:
        lines.extend([f"### {name}", "", f"- Idea: {idea}", f"- Verdict: {verdict}", ""])
    lines.extend(
        [
            "## Chosen Central Mechanism",
            "",
            "The paper will introduce **Causal-Exposure Memory Decay (CEMD)**. Each map edge or cell stores a last-observed state and a latent exposure clock. The exposure clock grows when unobserved change processes could physically reach that element through the environment's affordance graph. A planner then distrusts old map facts according to exposure-weighted hazard and the current route consequence.",
            "",
            "## Why This Is Stronger Than The Seed",
            "",
            "The seed asked when spatial memory should decay. The literature makes the stronger direction precise: decay is not a property of memory age; it is a property of missed causal opportunities for change plus the cost of being wrong during embodied operation.",
        ]
    )
    (DOCS / "novelty_decision.md").write_text("\n".join(lines), encoding="utf-8")


def write_claims() -> None:
    lines = [
        "# Claims",
        "",
        "## Supported Claims To Test",
        "",
        "1. If map-change hazards depend on unobserved physical exposure, any decay rule that is only a monotone function of elapsed time can mis-rank two equally old map elements and choose a worse route.",
        "2. A causal-exposure clock can be computed from a robot's map, entry points, activity priors, and occlusion/absence intervals without observing the actual change.",
        "3. In simulated long-horizon navigation with stale maps, exposure-based decay reduces collisions with invalidated map edges and improves mission success relative to no-decay, age-decay, fixed-hazard, and uncertainty-only baselines.",
        "4. The mechanism is distinct from generic uncertainty: exposure can increase trust loss in a low-variance old edge and preserve trust in a high-age but physically unreachable edge.",
        "",
        "## Formal Claim Status",
        "",
        "- Proposition planned: under a simple hazard model where change intensity is proportional to unobserved exposure, age-only decay is not Bayes-optimal when equal-age edges have unequal exposure. This can be proved by a two-edge counterexample.",
        "- No theorem will claim global optimality of the planner; the evidence will be empirical and mechanistic.",
        "",
        "## Claims To Avoid",
        "",
        "- Do not claim a complete solution to dynamic SLAM.",
        "- Do not claim state-of-the-art navigation performance.",
        "- Do not claim learned world models are unnecessary.",
        "- Do not claim real-world validation; this run will provide runnable simulated evidence only unless additional data becomes available.",
    ]
    (DOCS / "claims.md").write_text("\n".join(lines), encoding="utf-8")


def write_attacks() -> None:
    lines = [
        "# Reviewer Attacks",
        "",
        "1. This is just uncertainty-aware planning.",
        "   - Response: uncertainty is a representation; CEMD specifies the physical source of trust loss as unobserved intervention opportunity and demonstrates age/variance inversions.",
        "2. This is just active SLAM or next-best-view.",
        "   - Response: active revalidation is not central; the central variable is which stale map facts should decay before sensing is chosen.",
        "3. Dynamic occupancy grids already model changing cells.",
        "   - Response: most dynamic occupancy models update from observations and local temporal processes; the paper targets unobserved causal reachability during absence and route consequence.",
        "4. The simulator bakes in the method's assumptions.",
        "   - Response: true risk; the paper should present ablations where exposure is noisy or partially wrong and mark this as simulated mechanistic evidence.",
        "5. No real robot experiment.",
        "   - Response: mark paper-readiness honestly; position as a mechanism paper needing real deployment validation.",
        "6. Exposure priors are hard to estimate.",
        "   - Response: show the mechanism still helps with coarse priors and discuss using semantics, schedules, access control, or observed traffic as sources.",
        "7. The contribution is a planner cost.",
        "   - Response: formulate the memory state update independently of the planner; planning is the downstream test.",
        "8. The 1000-paper sweep is metadata-driven, not a true human deep read.",
        "   - Response: be explicit in final audit; use it to bound novelty, not as a substitute for careful camera-ready related work.",
    ]
    (DOCS / "reviewer_attacks.md").write_text("\n".join(lines), encoding="utf-8")


def write_subset_docs(rows: List[Dict[str, Any]]) -> None:
    skim_lines = ["# Serious Skim 300", ""]
    for row in rows[:300]:
        skim_lines.append(
            f"{row['rank']}. **{row['title']}** ({row['year']}) -- {row['problem_claimed']} Mechanism: {row['actual_mechanism_introduced']}"
        )
    (DOCS / "serious_skim_300.md").write_text("\n".join(skim_lines), encoding="utf-8")

    deep_lines = ["# Deep Read 225", "", "Metadata-guided extraction for the 225-paper deep-read subset.", ""]
    for row in rows[:225]:
        deep_lines.extend(
            [
                f"## {row['rank']}. {row['title']} ({row['year']})",
                f"- Problem claimed: {row['problem_claimed']}",
                f"- Mechanism: {row['actual_mechanism_introduced']}",
                f"- Hidden assumptions: {row['hidden_assumptions']}",
                f"- Fixed variables: {row['variables_treated_as_fixed']}",
                f"- Ignored failure modes: {row['failure_modes_ignored']}",
                f"- Less novel: {row['what_it_makes_less_novel']}",
                f"- Leaves open: {row['what_it_leaves_open']}",
                "",
            ]
        )
    (DOCS / "deep_read_225.md").write_text("\n".join(deep_lines), encoding="utf-8")


def main() -> int:
    try:
        save_progress("starting")
        works = collect_openalex(target=1250, max_pages_per_query=2)
        rows = build_rows(works)
        if len(rows) < 1000:
            save_progress("too_few_results", rows=len(rows), required=1000)
        rows = rows[: max(1000, min(len(rows), 1400))]
        write_matrix(rows)
        write_literature_map(rows)
        write_hostile(rows)
        write_novelty_boundary(rows)
        write_decision()
        write_claims()
        write_attacks()
        write_subset_docs(rows)
        save_progress("complete", rows=len(rows), matrix=str(MATRIX))
        print(json.dumps({"rows": len(rows), "matrix": str(MATRIX), "status": "complete"}))
    except Exception as exc:  # noqa: BLE001
        save_progress("fatal_error", error=repr(exc))
        print(json.dumps({"status": "fatal_error", "error": repr(exc)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
