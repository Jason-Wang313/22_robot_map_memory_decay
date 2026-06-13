# Hostile Reviewer Response

## Main Concern

The strongest objection is that CEMD wins because the simulator's true stale-map hazard is exposure-driven by construction.

## V2 Response

We added a hazard-misspecification stress test that changes the true closure process while leaving CEMD's estimator exposure-based. As the true hazard shifts from exposure-driven to age-driven, CEMD loses its advantage. At exposure share 0.00, age decay reaches 0.444 success and CEMD reaches 0.400.

## Revised Claim

The paper no longer claims a universally superior forgetting rule. The supported claim is that exposure is the right memory-decay variable when unobserved physical opportunity is predictive of map invalidation, and that age-only or uncertainty-only decay can mis-rank stale map risks under that causal structure.

## Remaining Weakness

The paper still lacks real robot validation, externally sourced map-change logs, and learned exposure-estimation baselines.
