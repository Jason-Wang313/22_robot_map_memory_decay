# Experiment Rigor Checklist

- [x] Main simulator is deterministic from recorded seeds.
- [x] Main comparison uses identical worlds and planner across methods.
- [x] Oracle probability is labeled as an upper reference, not a deployable method.
- [x] Exposure-estimate noise stress is included.
- [x] V2 hazard-misspecification stress attacks the central causal assumption.
- [x] Negative v2 result is included in the paper and docs.
- [ ] No real robot data.
- [ ] No externally sourced building-change benchmark.
- [ ] No learned exposure-estimation baseline.

Decision: rigorous enough for workshop-only / strong-revise positioning; not enough for a main-track submission claim.
