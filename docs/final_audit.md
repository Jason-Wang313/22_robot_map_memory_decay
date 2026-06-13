# Final Audit

1. **Chosen thesis:** Robot map memory should decay with unobserved intervention opportunity, not with elapsed age alone. In long-horizon navigation, a remembered edge should be distrusted when physical change processes could have reached it during the robot's absence and when relying on it would create route-level failure.

2. **Field assumption broken:** The paper breaks the common assumption that stale-map trust is mainly a local monotone function of time, posterior variance, or recent observation.

3. **New central mechanism:** Causal-Exposure Memory Decay (CEMD). Each map element carries an exposure clock driven by activity sources, access constraints, and unobserved reachability. Planning uses exposure-weighted hazard plus route consequence.

4. **Genuine novelty:** The mechanism changes the cause of memory distrust from age/uncertainty to missed physical opportunities for invalidation. This is narrower than dynamic SLAM or active sensing, but distinct from merely adding uncertainty or a verifier.

5. **Closest hostile prior work:** Long-term 3D map maintenance, dynamic occupancy mapping, FreMEn-style temporal models, active SLAM/next-best-view planning, and uncertainty-aware navigation. These make stale maps, dynamic environments, and risk-aware planning less novel, but leave open exposure-driven trust loss during robot absence.

6. **Literature coverage:** `docs/related_work_matrix.csv` contains 1,337 OpenAlex-ranked metadata entries with extraction columns for problem, mechanism, assumptions, fixed variables, ignored failures, novelty pressure, and openings. The run includes a 300-paper serious skim, a 225-paper deep-read subset, and a 100-paper hostile prior-work set. This is metadata-guided and useful for adversarial novelty search, not a substitute for a human camera-ready literature review.

7. **Proof/formal-claim status:** One formal counterexample is proved in the paper: if true hazards depend on exposure, an age-only rule can choose a strictly worse equal-age route. The numeric adversarial check is in `results/formal_counterexample.json`. No global optimality theorem is claimed.

8. **Strongest evidence:** A runnable 650-episode stale-map graph-navigation simulator plus 800 exposure-noise stress episodes and 800 v2 hazard-misspecification episodes. Main success rates: no decay 0.417, age decay 0.432, uncertainty-only 0.425, CEMD 0.549, oracle probability 0.591. CEMD also reduces blocked-edge encounters and regret in this exposure-driven setting. V2 stress shows the boundary: when true hazards are age-driven, age decay reaches 0.444 success and CEMD reaches 0.400.

9. **Biggest weaknesses:** The simulator's main hazard model is exposure-driven by construction; v2 confirms that CEMD can lose when the true hazard source is age rather than exposure. No real robot data validates that exposure clocks predict actual stale-map errors. The literature sweep is metadata-based. Exposure priors may be hard to estimate in deployment. The method does not solve SLAM, localization drift, learned exposure estimation, or multi-agent interaction.

10. **Paper-readiness judgment:** Workshop-only / strong-revise. The mechanism and runnable evidence are coherent enough for a focused workshop submission, but a main-track ICLR-style submission would need real-world validation or a stronger benchmark suite with externally sourced change processes.

11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/22.pdf`.

12. **GitHub URL:** `https://github.com/Jason-Wang313/22_robot_map_memory_decay`.

13. **Visible Desktop PDF copy status:** obsolete orchestrator copy should remain absent under v2 hardening; current Desktop path exists: False.

## Build And Publish Status

- Official template: refreshed from the ICLR 2026 Author Guide link to `https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip`.
- Evidence command completed: `python scripts/run_evidence.py`.
- Artifact audit completed: `python scripts/audit_artifacts.py`.
- V2 hazard-misspecification stress completed: `results/hazard_misspecification_results.csv` and `results/hazard_misspecification_table.tex`.
- LaTeX build completed with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`; all exits were 0.
- Final PDF copied to `C:/Users/wangz/Downloads/22.pdf`; v2 size: 470,419 bytes.
- PDF text verified for the visible v2 marker, hazard-misspecification table, and age-driven failure boundary.
- Local generated `paper/main.pdf` removed after copying; Desktop copies absent.
- Public GitHub repo created and complete repository pushed from local `master` to `origin/master`.

## Orchestrator Desktop Copy

Checked: 2026-06-11 18:04:06 +01:00
Downloads PDF: C:/Users/wangz/Downloads/22.pdf
Result: copy script exit 0 log C:\Users\wangz\robotics_60_paper_batch\logs\desktop_copy_22_20260611_180402.log
