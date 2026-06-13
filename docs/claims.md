# Claims

## Supported Claims To Test

1. If map-change hazards depend on unobserved physical exposure, any decay rule that is only a monotone function of elapsed time can mis-rank two equally old map elements and choose a worse route.
2. A causal-exposure clock can be computed from a robot's map, entry points, activity priors, and occlusion/absence intervals without observing the actual change.
3. In simulated long-horizon navigation with stale maps, exposure-based decay reduces collisions with invalidated map edges and improves mission success relative to no-decay, age-decay, fixed-hazard, and uncertainty-only baselines.
4. The mechanism is distinct from generic uncertainty: exposure can increase trust loss in a low-variance old edge and preserve trust in a high-age but physically unreachable edge.
5. V2 support is conditional: when true hazards are resampled to be age-driven instead of exposure-driven, age decay beats CEMD, so the claim requires exposure to be predictive of map invalidation.

## Formal Claim Status

- Proposition planned: under a simple hazard model where change intensity is proportional to unobserved exposure, age-only decay is not Bayes-optimal when equal-age edges have unequal exposure. This can be proved by a two-edge counterexample.
- No theorem will claim global optimality of the planner; the evidence will be empirical and mechanistic.

## Claims To Avoid

- Do not claim a complete solution to dynamic SLAM.
- Do not claim state-of-the-art navigation performance.
- Do not claim learned world models are unnecessary.
- Do not claim real-world validation; this run will provide runnable simulated evidence only unless additional data becomes available.
- Do not claim CEMD is a universally superior forgetting rule; the v2 hazard-misspecification stress identifies an age-driven failure case.
