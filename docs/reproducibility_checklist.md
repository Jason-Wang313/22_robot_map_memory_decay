# Reproducibility Checklist

- [x] Dependencies are listed in `requirements.txt`.
- [x] Main experiment source is `scripts/run_evidence.py`.
- [x] Artifact audit source is `scripts/audit_artifacts.py`.
- [x] Main outputs are `results/episode_results.csv`, `results/aggregate_results.csv`, and `results/noise_stress_results.csv`.
- [x] V2 outputs are `results/hazard_misspecification_results.csv` and `results/hazard_misspecification_table.tex`.
- [x] Paper source is `paper/main.tex`.
- [x] Canonical batch PDF path is `C:/Users/wangz/Downloads/22.pdf`.
- [x] Local `paper/main.pdf` is deleted after copying the canonical PDF to Downloads.

Recommended verification commands:

```powershell
python scripts\run_evidence.py
python scripts\audit_artifacts.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
