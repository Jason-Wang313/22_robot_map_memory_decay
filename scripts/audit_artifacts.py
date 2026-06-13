#!/usr/bin/env python3
"""Audit required paper-run artifacts.

This helper checks counts and existence only. It does not judge scientific
quality; that is recorded separately in docs/final_audit.md.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
PAPER = ROOT / "paper"
DOWNLOADS_PDF = Path("C:/Users/wangz/Downloads/22.pdf")


REQUIRED_DOCS = [
    "related_work_matrix.csv",
    "literature_map.md",
    "hostile_prior_work.md",
    "novelty_boundary_map.md",
    "novelty_decision.md",
    "claims.md",
    "reviewer_attacks.md",
    "final_audit.md",
]


def count_markdown_entries(path: Path) -> int:
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    heading_count = len(re.findall(r"^##\s+\d+[.]", text, flags=re.MULTILINE))
    numbered_count = len(re.findall(r"^\d+[.]\s+\*\*", text, flags=re.MULTILINE))
    return max(heading_count, numbered_count)


def is_truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y"}


def read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    related_rows = read_csv_rows(DOCS / "related_work_matrix.csv")
    aggregate_rows = read_csv_rows(RESULTS / "aggregate_results.csv")
    noise_rows = read_csv_rows(RESULTS / "noise_stress_results.csv")
    hazard_rows = read_csv_rows(RESULTS / "hazard_misspecification_results.csv")

    required_columns = {
        "problem_claimed",
        "actual_mechanism_introduced",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
    }
    matrix_columns = set(related_rows[0].keys()) if related_rows else set()

    formal_path = RESULTS / "formal_counterexample.json"
    formal: Dict[str, Any] = {}
    if formal_path.exists():
        formal = json.loads(formal_path.read_text(encoding="utf-8"))

    audit: Dict[str, Any] = {
        "required_docs": {name: (DOCS / name).exists() for name in REQUIRED_DOCS},
        "related_work_entries": len(related_rows),
        "related_work_has_required_extraction_columns": sorted(required_columns) == sorted(required_columns & matrix_columns),
        "serious_skim_flagged": sum(1 for row in related_rows if is_truthy(row.get("in_serious_skim_300", ""))),
        "deep_read_flagged": sum(1 for row in related_rows if is_truthy(row.get("in_deep_read_225", ""))),
        "hostile_prior_flagged": sum(1 for row in related_rows if is_truthy(row.get("in_hostile_prior_100", ""))),
        "serious_skim_doc_entries": count_markdown_entries(DOCS / "serious_skim_300.md"),
        "deep_read_doc_entries": count_markdown_entries(DOCS / "deep_read_225.md"),
        "hostile_prior_doc_entries": count_markdown_entries(DOCS / "hostile_prior_work.md"),
        "aggregate_methods": [row.get("method") for row in aggregate_rows],
        "noise_stress_rows": len(noise_rows),
        "hazard_misspecification_rows": len(hazard_rows),
        "hazard_misspecification_table_exists": (RESULTS / "hazard_misspecification_table.tex").exists(),
        "figures": {
            name: (FIGURES / name).exists()
            for name in [
                "aggregate_results.png",
                "exposure_calibration.png",
                "noise_stress.png",
                "hazard_misspecification.png",
                "example_world.png",
            ]
        },
        "formal_counterexample": {
            "exists": formal_path.exists(),
            "age_only_choice_route": formal.get("age_only_choice_route"),
            "exposure_aware_choice_route": formal.get("exposure_aware_choice_route"),
            "expected_cost_gap": formal.get("expected_cost_gap_if_age_only_chooses_exposed"),
        },
        "paper_main_tex_exists": (PAPER / "main.tex").exists(),
        "paper_main_pdf_exists": (PAPER / "main.pdf").exists(),
        "downloads_pdf_exists": DOWNLOADS_PDF.exists(),
        "official_iclr_2026_files_present": {
            name: (PAPER / name).exists()
            for name in [
                "iclr2026_conference.sty",
                "iclr2026_conference.bst",
                "math_commands.tex",
                "natbib.sty",
                "fancyhdr.sty",
            ]
        },
    }
    output = DOCS / "artifact_audit.json"
    output.write_text(json.dumps(audit, indent=2), encoding="utf-8")
    print(json.dumps(audit, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
