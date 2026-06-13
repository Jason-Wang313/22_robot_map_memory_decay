# Reviewer Attacks

1. This is just uncertainty-aware planning.
   - Response: uncertainty is a representation; CEMD specifies the physical source of trust loss as unobserved intervention opportunity and demonstrates age/variance inversions.
2. This is just active SLAM or next-best-view.
   - Response: active revalidation is not central; the central variable is which stale map facts should decay before sensing is chosen.
3. Dynamic occupancy grids already model changing cells.
   - Response: most dynamic occupancy models update from observations and local temporal processes; the paper targets unobserved causal reachability during absence and route consequence.
4. The simulator bakes in the method's assumptions.
   - Response: true risk; v2 adds a hazard-misspecification stress. When the true closure process is age-driven, age decay reaches 0.444 success and CEMD falls to 0.400, so the paper now states the causal boundary instead of claiming universal dominance.
5. No real robot experiment.
   - Response: mark paper-readiness honestly; position as a mechanism paper needing real deployment validation.
6. Exposure priors are hard to estimate.
   - Response: show the mechanism still helps with coarse priors and discuss using semantics, schedules, access control, or observed traffic as sources.
7. The contribution is a planner cost.
   - Response: formulate the memory state update independently of the planner; planning is the downstream test.
8. The 1000-paper sweep is metadata-driven, not a true human deep read.
   - Response: be explicit in final audit; use it to bound novelty, not as a substitute for careful camera-ready related work.
