# Deep Read 225

Metadata-guided extraction for the 225-paper deep-read subset.

## 1. Robot localization and mapping in complex scenarios (2026)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map memory can be trusted or discounted as a monotone function of elapsed time | map update and route choice can be separated without losing optimality
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 2. Long-term 3D map maintenance in dynamic environments (2014)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 3. A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 4. Probabilistic Mapping and Navigation: A Survey of Bayesian Meta-Learning for Autonomous Robots (2025)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | environment changes are locally independent once the map cell or edge is represented | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 5. Generalized Simultaneous Localization and Mapping (G-SLAM) as unification framework for natural and artificial intelligences: towards reverse engineering the hippocampal/entorhinal system and principles of high-level cognition (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 6. Generalized Simultaneous Localization and Mapping (G-SLAM) as unification framework for natural and artificial intelligences: towards reverse engineering the hippocampal/entorhinal system and principles of high-level cognition (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 7. AI-Driven Visual Navigation for Smart Lab Tour Guide Robot (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 8. A Comprehensive Review of Mobile Robot Navigation Using Deep Reinforcement Learning Algorithms in Crowded Environments (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 9. Multi-Object Navigation with dynamically learned neural implicit representations (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | change probability is a property of places rather than of unobserved interventions that could have reached them | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 10. SLAM-RAMU: 3D LiDAR-IMU lifelong SLAM with relocalization and autonomous map updating for accurate and reliable navigation (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | environment changes are locally independent once the map cell or edge is represented
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 11. Toward lifelong visual localization and mapping (2013)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | changes are stationary over deployment time
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 12. Lifelong Localization in Semi-Dynamic Environment (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 13. Vision-Based Navigation and Perception for Autonomous Robots: Sensors, SLAM, Control Strategies, and Cross-Domain Applications—A Review (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | human activity can be approximated as uniform noise in map cells | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 14. Stability Analysis and Navigational Techniques of Wheeled Mobile Robot: A Review (2023)
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 15. LONG–TERM AUTONOMY OF MOBILE ROBOTS IN CHANGING ENVIRONMENTS (2018)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 16. A Survey of Computer Vision Detection, Visual SLAM Algorithms, and Their Applications in Energy-Efficient Autonomous Systems (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 17. CausalNav: A Long-term Embodied Navigation System for Autonomous Mobile Robots in Dynamic Outdoor Scenarios (2026)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | semantic labels are stable enough that geometry can be updated around them | map changes are observed at the place where they matter for the plan
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 18. FreMEn: Frequency Map Enhancement for Long-Term Mobile Robot Autonomy in Changing Environments (2017)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 19. OFM-SLAM: A Visual Semantic SLAM for Dynamic Indoor Environments (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 20. Obstacle Persistent Adaptive Map Maintenance for Autonomous Mobile Robots using Spatio-temporal Reasoning (2019)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map memory can be trusted or discounted as a monotone function of elapsed time | map changes are observed at the place where they matter for the plan
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 21. BioSLAM: A Bio-inspired Lifelong Memory System for General Place Recognition (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: appearance drift is the main source of long-term navigation failure | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the robot's own unobserved absence does not create information about likely map changes
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 22. REAL-TIME METRIC-SEMANTIC VISUAL SLAM FOR DYNAMIC AND CHANGING ENVIRONMENTS (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | human activity can be approximated as uniform noise in map cells
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 23. Lightweight Visual Odometry for Autonomous Mobile Robots (2018)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 24. Visual-Inertial SLAM for Unstructured Outdoor Environments: Benchmarking the Benefits and Computational Costs of Loop Closing (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 25. HPPRM: Hybrid Potential Based Probabilistic Roadmap Algorithm for Improved Dynamic Path Planning of Mobile Robots (2020)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 26. 3-D Scan Registration Using Normal Distributions Transform with Supervoxel Segmentation (2015)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | environment changes are locally independent once the map cell or edge is represented | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 27. Advances in Inference and Representation for Simultaneous Localization and Mapping (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 28. The Simultaneous Localization and Mapping (SLAM)-An Overview (2021)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 29. Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation (2022)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 30. Place recognition meet multiple modalities: a comprehensive review, current challenges and future development (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 31. YG-SLAM: Enhancing Visual SLAM in Dynamic Environments With YOLOv8 and Geometric Constraints (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 32. Map Making in Social Indoor Environment Through Robot Navigation Using Active SLAM (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 33. Continual SLAM: Beyond Lifelong Simultaneous Localization and Mapping Through Continual Learning (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | changes are stationary over deployment time
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 34. Online Mapping and Motion Planning Under Uncertainty for Safe Navigation in Unknown Environments (2021)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | closed-world maps remain valid outside the robot's recent sensor frustum | uncertainty is enough to decide when memory should be distrusted
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 35. Towards Persistent Localization and Mapping with a Continuous Appearance-based Topology (2012)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | map update and route choice can be separated without losing optimality | map memory can be trusted or discounted as a monotone function of elapsed time
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 36. SLAM algorithm applied to robotics assistance for navigation in unknown environments (2010)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 37. YES-SLAM: YOLOv7-enhanced-semantic visual SLAM for mobile robots in dynamic scenes (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 38. Navigation Engine Design for Automated Driving Using INS/GNSS/3D LiDAR-SLAM and Integrity Assessment (2020)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | long-horizon navigation is limited mainly by localization drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 39. Are We Ready for Service Robots? The OpenLORIS-Scene Datasets for Lifelong SLAM (2019)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map memory can be trusted or discounted as a monotone function of elapsed time | long-horizon navigation is limited mainly by localization drift
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 40. A Review of Deep Reinforcement Learning Algorithms for Mobile Robot Path Planning (2023)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 41. Development and Testing of an Autonomous Mobile Robot for Material Handling Using SLAM and Nav2 (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 42. Occupancy Grid Models for Robot Mapping in Changing Environments (2021)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 43. Robot Navigation and Map Construction Based on SLAM Technology (2024)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 44. Exploration and mapping with mobile robots (2006)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | a robot can repair stale beliefs only by revisiting the stale location
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 45. Loop Closure Detection for Visual SLAM Based on Deep Learning (2017)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 46. A Comparative Review on Enhancing Visual Simultaneous Localization and Mapping with Deep Semantic Segmentation (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 47. Continuous shared control of a mobile robot with brain–computer interface and autonomous navigation for daily assistance (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 48. Recent Advances in Visual SLAM: Taxonomy, Comparative Analysis, and Open Challenges (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | learned memory modules implicitly discover when to forget spatial facts
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 49. STEP: Stochastic Traversability Evaluation and Planning for Risk-Aware Off-road Navigation (2021)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 50. Efficient navigation based on the Landmark-Tree map and the Z&lt;inf&gt;&amp;#x221E;&lt;/inf&gt; algorithm using an omnidirectional camera (2013)
- Problem claimed: Represent traversability or occupancy so a mobile robot can plan through partially observed space.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 51. Safe and Robust Map Updating For Long-Term Operations in Dynamic Environments (2023)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan | environment changes are locally independent once the map cell or edge is represented
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 52. Autonomous Navigation for Differential Drive Robots: Grid-Based Fastslam with AMCL in ROS2 (2025)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | sensing-before-acting baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 53. Aerial and Ground Robot Collaboration for Autonomous Mapping in Search and Rescue Missions (2020)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 54. Development of a Service Robot for Hospital Environments in Rehabilitation Medicine with LiDAR-Based Simultaneous Localization and Mapping (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 55. From Machinery to Biology: A Review on Mapless Autonomous Underwater Navigation (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 56. Lidar SLAM for Mobile Robot in an Indoor Environment (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 57. General Place Recognition Survey: Towards Real-World Autonomy (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 58. Combining Hector SLAM and Artificial Potential Field for Autonomous Navigation Inside a Greenhouse (2018)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 59. Learning Composable Behavior Embeddings for Long-Horizon Visual Navigation (2021)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 60. BDGS-SLAM: A Probabilistic 3D Gaussian Splatting Framework for Robust SLAM in Dynamic Environments (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | environment changes are locally independent once the map cell or edge is represented
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 61. A Review of Dynamic Object Filtering in SLAM Based on 3D LiDAR (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure.
- Hidden assumptions: long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 62. Robot Path Planning Navigation for Dense Planting Red Jujube Orchards Based on the Joint Improved A* and DWA Algorithms under Laser SLAM (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 63. Learning Composable Behavior Embeddings for Long-horizon Visual\n Navigation (2021)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 64. Building an Integrated Mobile Robotic System for Real-Time Applications in Construction (2018)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | sensing-before-acting baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 65. Semi-direct RGB-D slam algorithm for mobile robot In dynamic indoor environments (2018)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 66. A Systematic Literature Review on Long-Term Localization and Mapping for Mobile Robots (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map memory can be trusted or discounted as a monotone function of elapsed time | long-horizon navigation is limited mainly by localization drift | the robot's own unobserved absence does not create information about likely map changes
- Fixed variables: change process behind loop closures/map factors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 67. Leveraging Pedestrian Detection and Tracking in Robotics Navigation: A Survey With Practical Illustrations (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 68. Safe-Nav: learning to prevent PointGoal navigation failure in unknown environments (2022)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: SLAM/pose-graph or map-estimation machinery; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | uncertainty-aware navigation baseline | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 69. Visual Place Recognition: A Survey (2015)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map changes are observed at the place where they matter for the plan | change probability is a property of places rather than of unobserved interventions that could have reached them | appearance drift is the main source of long-term navigation failure
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 70. LCPF: A Particle Filter Lidar SLAM System With Loop Detection and Correction (2020)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 71. Obstacle Detection System for Agricultural Mobile Robot Application Using RGB-D Cameras (2021)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 72. A Survey on Active Simultaneous Localization and Mapping: State of the Art and New Frontiers (2023)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: SLAM/pose-graph or map-estimation machinery; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | uncertainty-aware navigation baseline | sensing-before-acting baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 73. Robust Visual Robot Localization Across Seasons Using Network Flows (2014)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 74. Real-Time Object Navigation With Deep Neural Networks and Hierarchical Reinforcement Learning (2020)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: learned memory/world-model framing
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 75. Simultaneous Localization and Mapping (SLAM) and Data Fusion in Unmanned Aerial Vehicles: Recent Advances and Challenges (2022)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 76. Deep Learning for Visual SLAM: The State-of-the-Art and Future Trends (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | learned memory modules implicitly discover when to forget spatial facts
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 77. Vision-Based Mobile Robotics Obstacle Avoidance With Deep Reinforcement Learning (2021)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 78. AEKF-SLAM: A New Algorithm for Robotic Underwater Navigation (2017)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 79. Multiple map hypotheses for planning and navigating in non-stationary environments (2014)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the robot's own unobserved absence does not create information about likely map changes | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 80. Generation of Indoor Open Street Maps for Robot Navigation from CAD Files (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 81. Classical and Heuristic Approaches for Mobile Robot Path Planning: A Survey (2023)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 82. Comparing LiDAR and IMU-based SLAM approaches for 3D robotic mapping (2023)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 83. OGM2PGBM: Robust BIM-based 2D-LiDAR localization for lifelong indoor navigation (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 84. Learning Forward Dynamics Model and Informed Trajectory Sampler for Safe Quadruped Navigation (2022)
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 85. SLAM, Path Planning Algorithm and Application Research of an Indoor Substation Wheeled Robot Navigation System (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 86. Hybrid, metric - topological, mobile robot navigation (2001)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 87. Visual Localization and Mapping in Dynamic and Changing Environments (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 88. Language, Environment, and Robotic Navigation (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 89. An Efficient Guiding Manager for Ground Mobile Robots in Agriculture (2023)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: planner or policy over the represented map.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: broad navigation/mapping context
- Leaves open: Explain when old spatial memory should be distrusted during embodied operation.

## 90. Exploration-Based SLAM (e-SLAM) for the Indoor Mobile Robot Using Lidar (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 91. YDD-SLAM: Indoor Dynamic Visual SLAM Fusing YOLOv5 with Depth Information (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 92. Comparison of DSO and ORB‐SLAM3 in Low‐Light Environments With Auxiliary Lighting and Deep Learning Based Image Enhancing (2025)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 93. SGC-VSLAM: A Semantic and Geometric Constraints VSLAM for Dynamic Indoor Environments (2020)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 94. Visual Place Recognition for Autonomous Mobile Robots (2017)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map changes are observed at the place where they matter for the plan | appearance drift is the main source of long-term navigation failure | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 95. Mobile Robot Navigation for Person Following in Indoor Environments (2013)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 96. Key Technologies for Real-time Localization and Scene Semantic Segmentation of Mobile Robots in Dynamic Environments (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 97. Collaborative Mobile Robotics for Semantic Mapping: A Survey (2022)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: broad navigation/mapping context
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 98. Simultaneous localization and mapping of mobile robots with multi-sensor fusion (2023)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 99. Adaptive Monocular Visual–Inertial SLAM for Real-Time Augmented Reality Applications in Mobile Devices (2017)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 100. PLGRIM: Hierarchical Value Learning for Large-scale Exploration in Unknown Environments (2021)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the cost of being wrong is proportional to local reconstruction error | uncertainty is enough to decide when memory should be distrusted
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 101. Simultaneous Localization and Mapping for Inspection Robots in Water and Sewer Pipe Networks: A Review (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 102. Local visual feature based localisation and mapping by mobile robots (2008)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 103. Improving SLAM Techniques with Integrated Multi-Sensor Fusion for 3D Reconstruction (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 104. Autonomous navigation in unstructured outdoor environments using semantic segmentation guided reinforcement learning (2026)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 105. Localization and navigation of the CoBots over long-term deployments (2013)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 106. RAEM-SLAM: A Robust Adaptive End-to-End Monocular SLAM Framework for AUVs in Underwater Environments (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 107. Getting Robots Unfrozen and Unlost in Dense Pedestrian Crowds (2018)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 108. BYE: Build Your Encoder with One Sequence of Exploration Data for Long-Term Dynamic Scene Understanding (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map memory can be trusted or discounted as a monotone function of elapsed time | the robot's own unobserved absence does not create information about likely map changes
- Fixed variables: object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | semantic persistence masks moved obstacles or closed doors | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 109. Comparison of SLAM algorithms for autonomous navigation systems in ROS 2 environment: analysis of mapping accuracy, position estimation and resource consumption (2025)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 110. The Deep Convolutional Neural Network Role in the Autonomous Navigation of Mobile Robots (SROBO) (2022)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 111. Dynamic pose graph SLAM: Long-term mapping in low dynamic environments (2012)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering.
- Hidden assumptions: map memory can be trusted or discounted as a monotone function of elapsed time | the robot's own unobserved absence does not create information about likely map changes | map update and route choice can be separated without losing optimality
- Fixed variables: change process behind loop closures/map factors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 112. A General Framework for Lifelong Localization and Mapping in Changing Environment (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering.
- Hidden assumptions: map memory can be trusted or discounted as a monotone function of elapsed time | long-horizon navigation is limited mainly by localization drift | the robot's own unobserved absence does not create information about likely map changes
- Fixed variables: change process behind loop closures/map factors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 113. Self-Organizing Memory Based on Adaptive Resonance Theory for Vision and Language Navigation (2023)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 114. A review of autonomous navigation systems in agricultural environments (2013)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 115. An Overview of Key SLAM Technologies for Underwater Scenes (2023)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 116. Uncertainty‐aware LiDAR‐based localization for outdoor mobile robots (2024)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 117. Outdoor navigation of mobile robots (2001)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | human activity can be approximated as uniform noise in map cells | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 118. Multi-Robot Hybrid Coverage Path Planning for 3D Reconstruction of Large Structures (2021)
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: map memory can be trusted or discounted as a monotone function of elapsed time | map changes are observed at the place where they matter for the plan | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 119. Visual-based simultaneous localization and mapping and global positioning system correction for geo-localization of a mobile robot (2011)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 120. A Fire Reconnaissance Robot Based on SLAM Position, Thermal Imaging Technologies, and AR Display (2019)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 121. Bacchus Long‐Term (BLT) data set: Acquisition of the agricultural multimodal BLT data set with automated robot deployment (2023)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | semantic labels are stable enough that geometry can be updated around them | human activity can be approximated as uniform noise in map cells
- Fixed variables: object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | semantic persistence masks moved obstacles or closed doors | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 122. Challenges and Solutions for Autonomous Ground Robot Scene Understanding and Navigation in Unstructured Outdoor Environments: A Review (2023)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 123. A Comprehensive Review on Autonomous Navigation (2022)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 124. On the performance of ConvNet features for place recognition (2015)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map changes are observed at the place where they matter for the plan | change probability is a property of places rather than of unobserved interventions that could have reached them | appearance drift is the main source of long-term navigation failure
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 125. Uma abordagem híbrida para planejamento exploratório de trajetórias e controle de navegação de robôs móveis autônomos (2018)
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 126. Artificial Intelligence for Long-Term Robot Autonomy: A Survey (2018)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 127. Visual-SLAM Classical Framework and Key Techniques: A Review (2022)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: SLAM/pose-graph or map-estimation machinery; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | uncertainty-aware navigation baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 128. Collision-Free Autonomous Robot Navigation in Unknown Environments Utilizing PSO for Path Planning (2019)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: broad navigation/mapping context
- Leaves open: Explain when old spatial memory should be distrusted during embodied operation.

## 129. Intelligent Reference Curation for Visual Place Recognition Via Bayesian Selective Fusion (2020)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | appearance drift is the main source of long-term navigation failure | uncertainty is enough to decide when memory should be distrusted
- Fixed variables: hazard model connecting uncertainty to physical change | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- Leaves open: Model when uncertainty should grow from causal exposure, not just observation age or posterior variance.

## 130. A Review of Multi-Sensor Fusion SLAM Systems Based on 3D LIDAR (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 131. AI smart cane technology and assistive navigation for visually impaired users: an overview (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | human activity can be approximated as uniform noise in map cells
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 132. Path Planning Technique for Mobile Robots: A Review (2023)
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Mechanism: planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 133. Autonomous Mobile Robot Path Planning Techniques—A Review: Metaheuristic and Cognitive Techniques (2026)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 134. GOAT: GO to Any Thing (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | human activity can be approximated as uniform noise in map cells | changes are stationary over deployment time
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 135. SLAM-Based Follow-the-Leader Deployment of Concentric Tube Robots (2020)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 136. Convolutional Neural Network-Based Robot Navigation Using Uncalibrated Spherical Images (2017)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 137. Challenges and Solutions for Autonomous Ground Robot Scene Understanding and Navigation in Unstructured Outdoor Environments: A Review (2023)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 138. A Review of Visual-Inertial Simultaneous Localization and Mapping from Filtering-Based and Optimization-Based Perspectives (2018)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 139. Role of Deep Learning in Loop Closure Detection for Visual and Lidar SLAM: A Survey (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 140. Deep reinforcement learning for map-less goal-driven robot navigation (2021)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 141. Going Places: Place Recognition in Artificial and Natural Systems (2025)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors | visual relocalization succeeds while the path itself has changed
- Less novel: broad navigation/mapping context
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 142. TopoNav: Topological Navigation for Efficient Exploration in Sparse Reward Environments (2024)
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 143. A biology-inspired attention model with application in robot navigation (2018)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 144. Recent advances in Rapidly-exploring random tree: A review (2024)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | long-horizon navigation is limited mainly by localization drift | human activity can be approximated as uniform noise in map cells
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 145. A Heterogeneous Unmanned Ground Vehicle and Blimp Robot Team for Search and Rescue using Data-Driven Autonomy and Communication-Aware Navigation (2022)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: probabilistic belief or risk model; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: uncertainty-aware navigation baseline | learned memory/world-model framing
- Leaves open: Model when uncertainty should grow from causal exposure, not just observation age or posterior variance.

## 146. LAMP: Learning a Motion Policy to Repeatedly Navigate in an Uncertain Environment (2021)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 147. Lifelong-MonoDepth: Lifelong Learning for Multi-Domain Monocular Metric Depth Estimation (2023)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 148. Learning Spatiotemporal Occupancy Grid Maps for Lifelong Navigation in Dynamic Scenes (2021)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 149. Overview of Visual SLAM for Mobile Robots (2021)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 150. Robot Localization and Navigation Using Visible Light Positioning and SLAM Fusion (2021)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 151. Planning Reliable Paths With Pose SLAM (2013)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: SLAM/pose-graph or map-estimation machinery; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | uncertainty-aware navigation baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 152. Path Planning for Smart Car Based on Dijkstra Algorithm and Dynamic Window Approach (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 153. LT-mapper: A Modular Framework for LiDAR-based Lifelong Mapping (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map memory can be trusted or discounted as a monotone function of elapsed time | the robot's own unobserved absence does not create information about likely map changes
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 154. High-Efficiency Navigation of Nonholonomic Mobile Robots Based on Improved Hybrid A* Algorithm (2023)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 155. Monocular Vision SLAM-Based UAV Autonomous Landing in Emergencies and Unknown Environments (2018)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 156. Enhancing Machine Learning Techniques in VSLAM for Robust Autonomous Unmanned Aerial Vehicle Navigation (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 157. Autonomous Navigation System of Indoor Mobile Robots Using 2D Lidar (2023)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: SLAM/pose-graph or map-estimation machinery; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | uncertainty-aware navigation baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 158. BotanicGarden: A High-Quality Dataset for Robot Navigation in Unstructured Natural Environments (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 159. Multi-Session Visual SLAM for Illumination-Invariant Re-Localization in Indoor Environments (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 160. A Survey of Spatial Memory Representations for Efficient Robot Navigation (2026)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 161. Inverse reinforcement learning for autonomous navigation via differentiable semantic mapping and planning (2023)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: learned memory/world-model framing
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 162. Real-Time SLAM Mobile Robot and Navigation Based on Cloud-Based Implementation (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 163. UVS: underwater visual SLAM—a robust monocular visual SLAM system for lifelong underwater operations (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 164. Recent advances in evolutionary and bio-inspired adaptive robotics: Exploiting embodied dynamics (2021)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 165. Drift-Free Visual SLAM for Mobile Robot Localization by Integrating UWB Technology (2022)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 166. GOAT: GO to Any Thing (2023)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | human activity can be approximated as uniform noise in map cells | changes are stationary over deployment time
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 167. Continuous Online Semantic Implicit Representation for Autonomous Ground Robot Navigation in Unstructured Environments (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; probabilistic belief or risk model; planner or policy over the represented map; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Ignored failure modes: high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: uncertainty-aware navigation baseline | learned memory/world-model framing
- Leaves open: Model when uncertainty should grow from causal exposure, not just observation age or posterior variance.

## 168. SEG-SLAM: Dynamic Indoor RGB-D Visual SLAM Integrating Geometric and YOLOv5-Based Semantic Information (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them | semantic labels are stable enough that geometry can be updated around them
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 169. Intelligent Systems in Motion (2023)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 170. Adaptive autonomous navigation of mobile robots in unknown environments (2002)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 171. PRM-D* Method for Mobile Robot Path Planning (2023)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 172. An Episodic-Procedural Semantic Memory Model for Continuous Topological Sensorimotor Map Building (2022)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: human activity can be approximated as uniform noise in map cells | change probability is a property of places rather than of unobserved interventions that could have reached them | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 173. A State-of-the-Art Review on Mapping and Localization of Mobile Robots Using Omnidirectional Vision Sensors (2017)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: planner or policy over the represented map.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: broad navigation/mapping context
- Leaves open: Explain when old spatial memory should be distrusted during embodied operation.

## 174. Predictive and adaptive maps for long-term visual navigation in changing environments (2019)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map changes are observed at the place where they matter for the plan | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 175. Autonomous Navigation by Mobile Robot with Sensor Fusion Based on Deep Reinforcement Learning (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 176. Improving the navigation optimization of hospital logistics robots under complex lighting changes by using improved ORB-SLAM3 and deep learning visual SLAM algorithm (2025)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map changes are observed at the place where they matter for the plan | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 177. POV-SLAM: Probabilistic Object-Aware Variational SLAM in Semi-Static Environments (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 178. Efficient Laser-Based 3D SLAM for Coal Mine Rescue Robots (2018)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | sensing-before-acting baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 179. Autonomous Navigation Framework for Intelligent Robots Based on a Semantic Environment Modeling (2020)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: sensing-before-acting baseline
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 180. Semantics for Robotic Mapping, Perception and Interaction: A Survey (2020)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: learned memory/world-model framing
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 181. MakeWay: Object-Aware Costmaps for Proactive Indoor Navigation Using LiDAR (2025)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | semantic labels are stable enough that geometry can be updated around them
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: sensing-before-acting baseline
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 182. A SUPERPOINT NEURAL NETWORK IMPLEMENTATION FOR ACCURATE FEATURE EXTRACTION IN UNSTRUCTURED ENVIRONMENTS (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | closed-world maps remain valid outside the robot's recent sensor frustum
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 183. Graceful Navigation for Mobile Robots in Dynamic and Uncertain Environments. (2016)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the cost of being wrong is proportional to local reconstruction error | human activity can be approximated as uniform noise in map cells
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 184. From SLAM to Situational Awareness: Challenges and Survey (2023)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; learned representation or neural memory module.
- Hidden assumptions: semantic labels are stable enough that geometry can be updated around them | map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 185. Path planning of mobile robot based on improved TD3 algorithm in dynamic environment (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 186. A Comprehensive Review of Improved A* Path Planning Algorithms and Their Hybrid Integrations (2025)
- Problem claimed: Represent traversability or occupancy so a mobile robot can plan through partially observed space.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 187. Bridging Zero-shot Object Navigation and Foundation Models through Pixel-Guided Navigation Skill (2023)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | semantic labels are stable enough that geometry can be updated around them
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors | visual relocalization succeeds while the path itself has changed
- Less novel: learned memory/world-model framing
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 188. Integrating Large Language Models into Robotic Autonomy: A Review of Motion, Voice, and Training Pipelines (2025)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; probabilistic belief or risk model; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Ignored failure modes: high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: uncertainty-aware navigation baseline | learned memory/world-model framing
- Leaves open: Model when uncertainty should grow from causal exposure, not just observation age or posterior variance.

## 189. Fast and Comfortable Robot-to-Human Handover for Mobile Cooperation Robot System (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map changes are observed at the place where they matter for the plan | human activity can be approximated as uniform noise in map cells
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 190. From Perception to Navigation in Environments with Persons: An Indoor Evaluation of the State of the Art (2022)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: sensing-before-acting baseline
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 191. LDVI-SLAM: a lightweight monocular visual-inertial SLAM system for dynamic environments based on motion constraints (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 192. GEM: Online Globally Consistent Dense Elevation Mapping for Unstructured Terrain (2020)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | negative evidence from not seeing an obstacle should be interpreted locally | long-horizon navigation is limited mainly by localization drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 193. BotanicGarden: A High-Quality Dataset for Robot Navigation in Unstructured Natural Environments (2023)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 194. Autonomous navigation and obstacle avoidance in smart robotic wheelchairs (2024)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 195. Simultaneous Localization and Mapping (SLAM) for Autonomous Driving: Concept and Analysis (2023)
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Mechanism: SLAM/pose-graph or map-estimation machinery; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Ignored failure modes: locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | uncertainty-aware navigation baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 196. LTA-OM: Long-Term Association LiDAR-IMU Odometry and Mapping (2023)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 197. 3D Gaussian Splatting as a New Era: A Survey (2024)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 198. Human-autonomy teaming for improved diver navigation (2022)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 199. Identifying robust landmarks in feature-based maps (2019)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 200. SLAMICP Library: Accelerating Obstacle Detection in Mobile Robot Navigation via Outlier Monitoring following ICP Localization (2023)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 201. PR-SLAM: Parallel Real-Time Dynamic SLAM Method Based on Semantic Segmentation (2024)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | human activity can be approximated as uniform noise in map cells
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 202. Structured Scene Memory for Vision-Language Navigation (2021)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 203. Learning robotic navigation from experience: principles, methods and recent results (2022)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: planner or policy over the represented map; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 204. Double-Domain Adaptation Semantics for Retrieval-Based Long-Term Visual Localization (2023)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map memory can be trusted or discounted as a monotone function of elapsed time | long-horizon navigation is limited mainly by localization drift
- Fixed variables: object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | semantic persistence masks moved obstacles or closed doors | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling
- Leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 205. Mobile robotics and 3D printing: addressing challenges in path planning and scalability (2024)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 206. Oceanic Challenges to Technological Solutions: A Review of Autonomous Underwater Vehicle Path Technologies in Biomimicry, Control, Navigation, and Sensing (2024)
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Mechanism: planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: planner repeatedly commits to stale bottlenecks
- Less novel: sensing-before-acting baseline
- Leaves open: Explain when old spatial memory should be distrusted during embodied operation.

## 207. A 2.5D Map-Based Mobile Robot Localization via Cooperation of Aerial and Ground Robots (2017)
- Problem claimed: Represent traversability or occupancy so a mobile robot can plan through partially observed space.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 208. Reinforcement learning as a robotics-inspired framework for insect navigation: from spatial representations to neural implementation (2024)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 209. Integration of the Mobile Robot and Internet of Things to Monitor Older People (2020)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 210. Safe and Robust Mobile Robot Navigation in Uneven Indoor Environments (2019)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 211. Multi-UAV Path Planning for Wireless Data Harvesting With Deep Reinforcement Learning (2021)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map changes are observed at the place where they matter for the plan | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 212. RDMO-SLAM: Real-Time Visual SLAM for Dynamic Environments Using Semantic Label Prediction With Optical Flow (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them | semantic labels are stable enough that geometry can be updated around them
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 213. The Experience-Memory Q-Learning Algorithm for Robot Path Planning in Unknown Environment (2020)
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | negative evidence from not seeing an obstacle should be interpreted locally | map changes are observed at the place where they matter for the plan
- Fixed variables: route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 214. Neuromorphic Perception and Navigation for Mobile Robots: A Review (2024)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 215. Research on Multi-Sensor Fusion SLAM Algorithm Based on Improved Gmapping (2023)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift
- Fixed variables: change process behind loop closures/map factors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 216. Particle Filter and Finite Impulse Response Filter Fusion and Hector SLAM to Improve the Performance of Robot Positioning (2018)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 217. A life-long SLAM approach using adaptable local maps based on rasterized LIDAR images (2021)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: long-horizon navigation is limited mainly by localization drift | map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map
- Fixed variables: change process behind loop closures/map factors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 218. A Universal LiDAR SLAM Accelerator System on Low-Cost FPGA (2022)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 219. A Survey on Visual Navigation and Positioning for Autonomous UUVs (2022)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: generic dynamic-environment handling | learned memory/world-model framing
- Leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 220. GNSS/IMU/ODO/LiDAR-SLAM Integrated Navigation System Using IMU/ODO Pre-Integration (2020)
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Mechanism: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- Less novel: map estimation and localization novelty
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 221. A Mobile Robot Visual SLAM System With Enhanced Semantics Segmentation (2020)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them | semantic labels are stable enough that geometry can be updated around them
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 222. Navigating the Landscape for Real-Time Localization and Mapping for Robotics and Virtual and Augmented Reality (2018)
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Mechanism: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | semantic labels are stable enough that geometry can be updated around them | long-horizon navigation is limited mainly by localization drift
- Fixed variables: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Ignored failure modes: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 223. A review of UAV autonomous navigation in GPS-denied environments (2023)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Fixed variables: route-level cost of stale-map errors | physical traversability behind appearance drift
- Ignored failure modes: planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- Less novel: sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 224. Visual SLAM Based on Semantic Segmentation and Geometric Constraints for Dynamic Indoor Environments (2022)
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Mechanism: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization; occupancy/traversability grid representation.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Fixed variables: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Ignored failure modes: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- Less novel: map estimation and localization novelty | generic dynamic-environment handling
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 225. Unlocking robotic perception: comparison of deep learning methods for simultaneous localization and mapping and visual simultaneous localization and mapping in robot (2025)
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Mechanism: SLAM/pose-graph or map-estimation machinery; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift
- Fixed variables: change process behind loop closures/map factors | physical traversability behind appearance drift
- Ignored failure modes: locally consistent maps hide task-critical topology changes | visual relocalization succeeds while the path itself has changed
- Less novel: map estimation and localization novelty | sensing-before-acting baseline | learned memory/world-model framing
- Leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.
