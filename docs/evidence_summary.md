# Evidence Summary

## Experiment

The simulator instantiates a long-horizon mobile robot with a stale graph map of a building-like environment. During the robot's absence, unobserved activity walks through the environment and can close remembered traversable edges. Every method receives the same old map and differs only in how it converts stale memory into route risk.

## Main Aggregate

- No decay success: 0.417; mean collisions: 1.569; mean regret: 26.756.
- Age decay success: 0.432; mean collisions: 1.511; mean regret: 25.909.
- Uncertainty-only success: 0.425; mean collisions: 1.502; mean regret: 25.762.
- CEMD success: 0.549; mean collisions: 1.285; mean regret: 22.551. At exposure-noise 1.0, CEMD success is 0.575.

## Formal Counterexample Check

Two route edges have equal age (30.0 days), but exposures 0.05 and 3.80. A monotone age-only rule assigns the same stale-memory risk and chooses the shorter exposed route. Under the exposure hazard model, the expected-cost gap from that choice is 55.054.

## Files

- `results/episode_results.csv`
- `results/aggregate_results.csv`
- `results/edge_exposure_samples.csv`
- `results/noise_stress_results.csv`
- `results/formal_counterexample.json`
- `figures/aggregate_results.png`
- `figures/exposure_calibration.png`
- `figures/noise_stress.png`
- `figures/example_world.png`
