# Submission Attack Log

Updated: 2026-06-13 02:52:00 +01:00

## V2 Attack Rounds

1. **"The simulator bakes in CEMD's causal variable."** Added a hazard-misspecification stress that resamples true closures from exposure-driven to age-driven.
2. **"CEMD may only be a good heuristic when exposure is actually causal."** Confirmed. At exposure share 0.00, age decay reaches 0.444 success and CEMD reaches 0.400.
3. **"The paper overclaims general stale-map superiority."** Narrowed the manuscript to a causal claim: exposure decay helps when exposure predicts invalidation.
4. **"Exposure priors may be wrong in deployment."** Still unresolved without real robot data or externally sourced change logs.
5. **"The evidence is simulation-only."** Decision remains workshop-only / strong-revise.

## Terminal Assessment

The recoverable overclaim was addressed by adding a hostile stress test and narrowing the contribution. Remaining weaknesses require real deployment data or a stronger benchmark with non-synthetic change processes.
