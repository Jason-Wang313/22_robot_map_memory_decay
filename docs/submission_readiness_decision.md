# Submission Readiness Decision

Decision: workshop-only / strong-revise.

## Why Not Submit-Ready

- Evidence is synthetic and the main simulator is exposure-driven by construction.
- V2 shows CEMD can lose to age decay when hazards are actually age-driven.
- No real robot, map-change log, or measured exposure prior is included.
- The formal result is a useful counterexample, not a full navigation theorem.

## Why Not Kill

- The causal-exposure variable is crisp and falsifiable.
- The formal counterexample cleanly separates equal age from unequal physical change opportunity.
- The v2 stress makes the causal boundary honest rather than hiding the failure case.

## Required Next Work For Main-Track Strength

- Evaluate on real long-horizon navigation logs with map invalidations.
- Estimate exposure from schedules, access constraints, traffic, or semantic activity sources.
- Compare against learned stale-map risk models.
- Test on non-synthetic benchmarks where the true change process is not constructed by the proposed variable.
