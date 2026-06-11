# Novelty Decision

## Selected Thesis

**Map memory should decay with unobserved intervention opportunity, not with age alone.** For long-horizon embodied navigation, a remembered door, corridor, or traversable edge should be distrusted when agents or processes could have reached and changed it during the robot's absence, especially when relying on that memory would create route-level failure.

## Candidate Directions Considered

### Temporal decay planner

- Idea: Discount map cells by elapsed time and plan around old regions.
- Verdict: Rejected because this is the default weak move; it does not break the field assumption and is close to standard dynamic occupancy or stale-map heuristics.

### Uncertainty-triggered revalidation

- Idea: Ask the robot to verify high-uncertainty map elements before using them.
- Verdict: Rejected because it is essentially active perception plus uncertainty-aware planning unless the source of uncertainty changes.

### Neural map-memory module

- Idea: Train a memory model to forget stale spatial facts.
- Verdict: Rejected because scale and data are not a mechanism, and the literature already contains neural SLAM/embodied memory claims.

### Causal exposure decay

- Idea: Decay a remembered spatial fact when unobserved interventions could have reached and changed it; route choices pay for both exposure hazard and consequence.
- Verdict: Selected because it changes the central mechanism from posterior age/variance to physical opportunity for map invalidation.

## Chosen Central Mechanism

The paper will introduce **Causal-Exposure Memory Decay (CEMD)**. Each map edge or cell stores a last-observed state and a latent exposure clock. The exposure clock grows when unobserved change processes could physically reach that element through the environment's affordance graph. A planner then distrusts old map facts according to exposure-weighted hazard and the current route consequence.

## Why This Is Stronger Than The Seed

The seed asked when spatial memory should decay. The literature makes the stronger direction precise: decay is not a property of memory age; it is a property of missed causal opportunities for change plus the cost of being wrong during embodied operation.