# Robot Map Memory Decay

Anonymous ICLR-style paper artifact for paper 22 in the robotics/embodied-intelligence batch.

## Thesis

Long-horizon robot map memory should decay when the physical world had unobserved opportunities to invalidate a remembered spatial fact, not simply because the memory is old. The repository implements and tests **Causal-Exposure Memory Decay (CEMD)** in a small stale-map navigation simulator.

## Repository Layout

- `paper/`: ICLR 2026 LaTeX source, official style files, bibliography, and compiled `main.pdf`.
- `scripts/run_evidence.py`: deterministic simulator and plotting pipeline.
- `scripts/literature_pipeline.py`: OpenAlex metadata sweep used for novelty search.
- `scripts/audit_artifacts.py`: compact artifact/count audit.
- `docs/`: literature matrix, novelty notes, hostile prior work, claims, reviewer attacks, evidence summary, and final audit.
- `results/`: generated CSVs and formal counterexample JSON.
- `figures/`: generated paper figures.

## Reproduce Evidence

```powershell
python -m pip install -r requirements.txt
python scripts/run_evidence.py
python scripts/audit_artifacts.py
```

The main simulator command regenerates:

- `results/episode_results.csv`
- `results/aggregate_results.csv`
- `results/noise_stress_results.csv`
- `results/hazard_misspecification_results.csv`
- `results/hazard_misspecification_table.tex`
- `results/formal_counterexample.json`
- `figures/*.png`
- `docs/evidence_summary.md`

## Build Paper

From `paper/`:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final compiled PDF for the orchestrator run was copied to:

```text
C:/Users/wangz/Downloads/22.pdf
```

## Evidence Status

The result is simulated mechanistic evidence, not a real-robot validation. The strongest current support is the formal counterexample and a reproducible 650-episode graph-navigation simulation where CEMD improves mission success over no-decay, age-decay, fixed-hazard, and uncertainty-only baselines. The v2 hazard-misspecification stress shows the boundary: when true stale-map hazards are made age-driven, age decay beats CEMD.
