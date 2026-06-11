# Novelty Boundary Map

## Non-Novel Territory

- Better SLAM, loop closure, or visual localization alone is not enough; many hostile papers already cover robust map estimation and place recognition.
- A generic uncertainty-aware planner is not enough; prior work already plans under uncertain occupancy, belief, and risk.
- Active re-observation as a generic verifier is not enough; active SLAM and information-gain exploration already cover the broad move.
- A learned memory module is not enough; neural SLAM, embodied memory, and world-model papers already claim learned spatial memory.
- A benchmark of stale maps is not enough without a mechanism explaining which memories should decay.

## Boundary By Cluster

### memory

- Hostile examples: Robot localization and mapping in complex scenarios (2026); Long-term 3D map maintenance in dynamic environments (2014); A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025)
- Boundary: Prior work reuses experiences; this paper should decide when experience becomes unsafe to reuse.

### planning

- Hostile examples: Robot localization and mapping in complex scenarios (2026); Long-term 3D map maintenance in dynamic environments (2014); A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025)
- Boundary: Prior work plans around risk; this paper must make route consequence interact with memory decay rather than attach a generic risk penalty.

### dynamic

- Hostile examples: Robot localization and mapping in complex scenarios (2026); Long-term 3D map maintenance in dynamic environments (2014); A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025)
- Boundary: Prior work handles moving objects and map updates; this paper must target unobserved opportunities for change during absence, not just observed dynamics.

### slam

- Hostile examples: Robot localization and mapping in complex scenarios (2026); Long-term 3D map maintenance in dynamic environments (2014); A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025)
- Boundary: Prior work estimates maps and poses; this paper must not claim map estimation as the central novelty.

### learning

- Hostile examples: Robot localization and mapping in complex scenarios (2026); A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025); Probabilistic Mapping and Navigation: A Survey of Bayesian Meta-Learning for Autonomous Robots (2025)
- Boundary: Prior work learns memory; this paper should be mechanistic and testable without relying on model scale.

### vision

- Hostile examples: A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025); AI-Driven Visual Navigation for Smart Lab Tour Guide Robot (2025); Toward lifelong visual localization and mapping (2013)
- Boundary: Prior work addresses appearance drift; this paper should distinguish visual relocalization from physical map validity.

### semantic

- Hostile examples: Robot localization and mapping in complex scenarios (2026); Long-term 3D map maintenance in dynamic environments (2014); A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025)
- Boundary: Prior work uses objects/labels; this paper may use semantics only as activity affordances for memory hazard.

### active

- Hostile examples: A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025); Probabilistic Mapping and Navigation: A Survey of Bayesian Meta-Learning for Autonomous Robots (2025); Generalized Simultaneous Localization and Mapping (G-SLAM) as unification framework for natural and artificial intelligences: towards reverse engineering the hippocampal/entorhinal system and principles of high-level cognition (2022)
- Boundary: Prior work chooses sensing actions; this paper should use selective revalidation only as a consequence of exposure decay.

### uncertainty

- Hostile examples: Probabilistic Mapping and Navigation: A Survey of Bayesian Meta-Learning for Autonomous Robots (2025); LONG–TERM AUTONOMY OF MOBILE ROBOTS IN CHANGING ENVIRONMENTS (2018); FreMEn: Frequency Map Enhancement for Long-Term Mobile Robot Autonomy in Changing Environments (2017)
- Boundary: Prior work propagates belief uncertainty; this paper must show posterior variance or age can be wrong when intervention exposure differs.

### occupancy

- Hostile examples: Multi-Object Navigation with dynamically learned neural implicit representations (2022); SLAM-RAMU: 3D LiDAR-IMU lifelong SLAM with relocalization and autonomous map updating for accurate and reliable navigation (2024); 3-D Scan Registration Using Normal Distributions Transform with Supervoxel Segmentation (2015)
- Boundary: Prior work updates cells; this paper should challenge local independent cell aging.

## Surviving Novelty Opening

The surviving opening is a **causal-exposure model of map-memory decay**: old spatial facts should decay according to the amount of unobserved physical opportunity for the world to change them, and this distrust should be evaluated through the current route's consequences. That is different from simply making a map uncertain with age, adding a verifier, or learning a larger memory.