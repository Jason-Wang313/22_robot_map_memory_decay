# Paper 22 Execution Plan

## Objective
Create a complete anonymous ICLR-style robotics paper for `22_robot_map_memory_decay`, grounded in a broad literature sweep and runnable evidence, then compile the final PDF to `C:/Users/wangz/Downloads/22.pdf`, push the complete public GitHub repository `22_robot_map_memory_decay`, and write the required audit artifacts.

## Constraints
- Stay in robotics / embodied physical intelligence.
- Treat seed topic as provisional until literature review and hostile prior work review.
- Reuse any existing artifacts if this retry already contains useful work.
- Keep `child_status.md` compact and current.
- Avoid brittle or fatal diagnostics; use explicit timeouts for long commands.
- Use direct `pdflatex`/`bibtex` build steps with generous timeouts if available.

## Execution Stages
1. Inspect repository state and available tools without destructive commands.
2. Create or update `child_status.md` with current facts and exact commands.
3. Retrieve or construct a large literature corpus:
   - 1000-paper landscape sweep saved to `docs/related_work_matrix.csv`.
   - 300-paper serious skim.
   - 200-250-paper deep read.
   - 100-paper hostile prior-work set.
4. Analyze the field box:
   - Define the field.
   - Extract important-paper mechanisms, assumptions, fixed variables, ignored failures, novelty threats, and openings.
   - Identify at least 20 false hidden assumptions.
   - Generate candidate paper directions and choose the strongest.
5. Produce novelty and claim artifacts:
   - `docs/literature_map.md`
   - `docs/hostile_prior_work.md`
   - `docs/novelty_boundary_map.md`
   - `docs/novelty_decision.md`
   - `docs/claims.md`
   - `docs/reviewer_attacks.md`
6. Implement runnable evidence:
   - Minimal simulation / experiment for long-horizon navigation with memory decay or distrust.
   - Reproducible scripts, cached outputs, plots/tables.
   - Verify scripts run end to end.
7. Write the paper:
   - Use the latest official ICLR template available at runtime.
   - Anonymous style.
   - Honest claims and limitations.
   - Sanitized BibTeX and pdfLaTeX-safe text.
8. Build the PDF:
   - Prefer `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
   - Copy final PDF only to `C:/Users/wangz/Downloads/22.pdf`.
   - Document any build failures and recovery steps.
9. Publish:
   - Commit complete repo.
   - Create public GitHub repo `22_robot_map_memory_decay`.
   - Push branch.
   - Document URL or failure.
10. Final audit:
   - Write `docs/final_audit.md` answering all required questions.
   - Include desktop-copy status as `pending orchestrator copy` unless an orchestrator result is present.

