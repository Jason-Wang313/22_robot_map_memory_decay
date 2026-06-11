# Hostile Prior Work Set

These are the 100 papers most likely to make a map-memory-decay paper look incremental. Each entry records the problem, mechanism, hidden assumptions, fixed variables, ignored failures, novelty pressure, and remaining opening from the metadata-driven sweep.

## 1. Robot localization and mapping in complex scenarios (2026)

- Authors: Matteo Scucchia
- Venue/source: AMS Dottorato Institutional Doctoral Theses Repository (University of Bologna)
- URL/DOI: https://doi.org/10.48676/unibo/amsdottorato/12653
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map memory can be trusted or discounted as a monotone function of elapsed time | map update and route choice can be separated without losing optimality
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 2. Long-term 3D map maintenance in dynamic environments (2014)

- Authors: François Pomerleau, Philipp Krüsi, Francis Colas, Paul Furgale, Roland Siegwart
- Venue/source: https://doi.org/10.1109/icra.2014.6907397
- URL/DOI: https://doi.org/10.1109/icra.2014.6907397
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 3. A Comprehensive Survey of Visual SLAM Technology: Methods, Challenges, and Perspectives (2025)

- Authors: Aidos Ibrayev, Amanzhol Bektemessov
- Venue/source: International Journal of Advanced Computer Science and Applications
- URL/DOI: https://doi.org/10.14569/ijacsa.2025.0161040
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 4. Probabilistic Mapping and Navigation: A Survey of Bayesian Meta-Learning for Autonomous Robots (2025)

- Authors: Sreejib Pal, Soumitra Keshari Nayak
- Venue/source: Journal of Intelligent & Robotic Systems
- URL/DOI: https://doi.org/10.1007/s10846-025-02283-8
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | environment changes are locally independent once the map cell or edge is represented | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 5. Generalized Simultaneous Localization and Mapping (G-SLAM) as unification framework for natural and artificial intelligences: towards reverse engineering the hippocampal/entorhinal system and principles of high-level cognition (2022)

- Authors: Adam Safron, Ozan Çatal, Tim Verbelen
- Venue/source: Frontiers in Systems Neuroscience
- URL/DOI: https://doi.org/10.3389/fnsys.2022.787659
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | change probability is a property of places rather than of unobserved interventions that could have reached them
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 6. Generalized Simultaneous Localization and Mapping (G-SLAM) as unification framework for natural and artificial intelligences: towards reverse engineering the hippocampal/entorhinal system and principles of high-level cognition (2021)

- Authors: Adam Safron, Ozan Çatal, Tim Verbelen
- Venue/source: https://doi.org/10.31234/osf.io/tdw82
- URL/DOI: https://doi.org/10.31234/osf.io/tdw82
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | change probability is a property of places rather than of unobserved interventions that could have reached them
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 7. AI-Driven Visual Navigation for Smart Lab Tour Guide Robot (2025)

- Authors: Vinod Chandrakant Todkari, Avinash P. Kaldate, Shrikrishna Kolhar, Arvind M. Jagtap, Nilesh P. Sable
- Venue/source: Journal Européen des Systèmes Automatisés
- URL/DOI: https://doi.org/10.18280/jesa.581214
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 8. A Comprehensive Review of Mobile Robot Navigation Using Deep Reinforcement Learning Algorithms in Crowded Environments (2024)

- Authors: Hoangcong Le, Saeed Saeedvand, Chen‐Chien Hsu
- Venue/source: Journal of Intelligent & Robotic Systems
- URL/DOI: https://doi.org/10.1007/s10846-024-02198-w
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 9. Multi-Object Navigation with dynamically learned neural implicit representations (2022)

- Authors: Pierre Marza, Laëtitia Matignon, Olivier Simonin, Christian Wolf
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2210.05129
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | change probability is a property of places rather than of unobserved interventions that could have reached them | topological connectivity changes are rare compared with metric pose drift
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 10. SLAM-RAMU: 3D LiDAR-IMU lifelong SLAM with relocalization and autonomous map updating for accurate and reliable navigation (2024)

- Authors: Bushi Chen, Xunyu Zhong, Han Xie, Pengfei Peng, Huosheng Hu, Xungao Zhong, et al.
- Venue/source: Industrial Robot the international journal of robotics research and application
- URL/DOI: https://doi.org/10.1108/ir-09-2023-0223
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | environment changes are locally independent once the map cell or edge is represented
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 11. Toward lifelong visual localization and mapping (2013)

- Authors: Hordur Johannsson
- Venue/source: https://doi.org/10.1575/1912/5980
- URL/DOI: https://doi.org/10.1575/1912/5980
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | changes are stationary over deployment time
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 12. Lifelong Localization in Semi-Dynamic Environment (2021)

- Authors: Shifan Zhu, Xinyu Zhang, Shichun Guo, Jun Li, Huaping Liu
- Venue/source: https://doi.org/10.1109/icra48506.2021.9561584
- URL/DOI: https://doi.org/10.1109/icra48506.2021.9561584
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 13. Vision-Based Navigation and Perception for Autonomous Robots: Sensors, SLAM, Control Strategies, and Cross-Domain Applications—A Review (2025)

- Authors: Eder A. Rodríguez-Martínez, Wendy Flores‐Fuentes, Farouk Achakir, Oleg Sergiyenko, Fabián N. Murrieta-Rico
- Venue/source: Eng—Advances in Engineering
- URL/DOI: https://doi.org/10.3390/eng6070153
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | human activity can be approximated as uniform noise in map cells | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 14. Stability Analysis and Navigational Techniques of Wheeled Mobile Robot: A Review (2023)

- Authors: Kailash Kumar Borkar, Turki Aljrees, Saroj Kumar Pandey, Ankit Kumar, Mukesh Singh, Anurag Sinha, et al.
- Venue/source: Processes
- URL/DOI: https://doi.org/10.3390/pr11123302
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 15. LONG–TERM AUTONOMY OF MOBILE ROBOTS IN CHANGING ENVIRONMENTS (2018)

- Authors: Tomáš Krajník
- Venue/source: Cvut DSpace (Czech Technical University)
- URL/DOI: https://openalex.org/W2797326841
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan | change probability is a property of places rather than of unobserved interventions that could have reached them
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 16. A Survey of Computer Vision Detection, Visual SLAM Algorithms, and Their Applications in Energy-Efficient Autonomous Systems (2024)

- Authors: Lu Chen, Gun Li, Weisi Xie, Jie Tan, Yang Li, Junfeng Pu, et al.
- Venue/source: Energies
- URL/DOI: https://doi.org/10.3390/en17205177
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 17. CausalNav: A Long-term Embodied Navigation System for Autonomous Mobile Robots in Dynamic Outdoor Scenarios (2026)

- Authors: Hongbo Duan, Shangyi Luo, Zhiyuan Deng, Yanbo Chen, Yuanhao Chiang, Yi Liu, et al.
- Venue/source: ArXiv.org
- URL/DOI: http://arxiv.org/abs/2601.01872
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | semantic labels are stable enough that geometry can be updated around them | map changes are observed at the place where they matter for the plan
- Variables treated as fixed: route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 18. FreMEn: Frequency Map Enhancement for Long-Term Mobile Robot Autonomy in Changing Environments (2017)

- Authors: Tomáš Krajník, Jaime Pulido Fentanes, João Santos, Tom Duckett
- Venue/source: IEEE Transactions on Robotics
- URL/DOI: https://doi.org/10.1109/tro.2017.2665664
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 19. OFM-SLAM: A Visual Semantic SLAM for Dynamic Indoor Environments (2021)

- Authors: Xiong Zhao, Tao Zuo, Xinyu Hu
- Venue/source: Mathematical Problems in Engineering
- URL/DOI: https://doi.org/10.1155/2021/5538840
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 20. Obstacle Persistent Adaptive Map Maintenance for Autonomous Mobile Robots using Spatio-temporal Reasoning (2019)

- Authors: Meredith L. Pitschl, Mitch Pryor
- Venue/source: https://doi.org/10.1109/coase.2019.8843095
- URL/DOI: https://doi.org/10.1109/coase.2019.8843095
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map memory can be trusted or discounted as a monotone function of elapsed time | map changes are observed at the place where they matter for the plan
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 21. BioSLAM: A Bio-inspired Lifelong Memory System for General Place Recognition (2022)

- Authors: Peng Yin, Abulikemu Abuduweili, Shiqi Zhao, Changliu Liu, Sebastian Scherer
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2208.14543
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: appearance drift is the main source of long-term navigation failure | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the robot's own unobserved absence does not create information about likely map changes
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 22. REAL-TIME METRIC-SEMANTIC VISUAL SLAM FOR DYNAMIC AND CHANGING ENVIRONMENTS (2022)

- Authors: JOAO CARLOS VIRGOLINO SOARES
- Venue/source: https://doi.org/10.17771/pucrio.acad.59878
- URL/DOI: https://doi.org/10.17771/pucrio.acad.59878
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | human activity can be approximated as uniform noise in map cells
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 23. Lightweight Visual Odometry for Autonomous Mobile Robots (2018)

- Authors: Mohamed Aladem, Samir A. Rawashdeh
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s18092837
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: map estimation and localization novelty
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 24. Visual-Inertial SLAM for Unstructured Outdoor Environments: Benchmarking the Benefits and Computational Costs of Loop Closing (2024)

- Authors: Fabian Schmidt, Constantin Blessing, Markus Enzweiler, Abhinav Valada
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2408.01716
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 25. HPPRM: Hybrid Potential Based Probabilistic Roadmap Algorithm for Improved Dynamic Path Planning of Mobile Robots (2020)

- Authors: Ankit A. Ravankar, Abhijeet Ravankar, Takanori Emaru, Yukinori Kobayashi
- Venue/source: IEEE Access
- URL/DOI: https://doi.org/10.1109/access.2020.3043333
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 26. 3-D Scan Registration Using Normal Distributions Transform with Supervoxel Segmentation (2015)

- Authors: 김지웅
- Venue/source: Seoul National University Open Repository (Seoul National University)
- URL/DOI: http://hdl.handle.net/10371/123138
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | environment changes are locally independent once the map cell or edge is represented | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 27. Advances in Inference and Representation for Simultaneous Localization and Mapping (2021)

- Authors: David M. Rosen, Kevin Doherty, Antonio Terán Espinoza, John J. Leonard
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2103.05041
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 28. The Simultaneous Localization and Mapping (SLAM)-An Overview (2021)

- Authors: Bashar Alsadik, Samer Karam
- Venue/source: Journal of Applied Science and Technology Trends
- URL/DOI: https://doi.org/10.38094/jastt204117
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: map estimation and localization novelty | sensing-before-acting baseline | learned memory/world-model framing
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 29. Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation (2022)

- Authors: Tomáš Vintr, J. Blaha, Martin Rektoris, J. Ulrich, Tomáš Rouček, George Broughton, et al.
- Venue/source: Frontiers in Robotics and AI
- URL/DOI: https://doi.org/10.3389/frobt.2022.890013
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 30. Place recognition meet multiple modalities: a comprehensive review, current challenges and future development (2025)

- Authors: Zhenyu Li, Tianyi Shang, Pengjie Xu, Zhaojun Deng
- Venue/source: Artificial Intelligence Review
- URL/DOI: https://doi.org/10.1007/s10462-025-11367-8
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 31. YG-SLAM: Enhancing Visual SLAM in Dynamic Environments With YOLOv8 and Geometric Constraints (2023)

- Authors: Guoming Chu, Peng Yan, Xuhong Luo, Jing Gong
- Venue/source: IEEE Access
- URL/DOI: https://doi.org/10.1109/access.2023.3342080
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 32. Map Making in Social Indoor Environment Through Robot Navigation Using Active SLAM (2022)

- Authors: Kiran Jot Singh, Divneet Singh Kapoor, Khushal Thakur, Anshul Sharma, Anand Nayyar, Shubham Mahajan, et al.
- Venue/source: IEEE Access
- URL/DOI: https://doi.org/10.1109/access.2022.3230989
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 33. Continual SLAM: Beyond Lifelong Simultaneous Localization and Mapping Through Continual Learning (2022)

- Authors: Niclas Vödisch, Daniele Cattaneo, Wolfram Burgard, Abhinav Valada
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2203.01578
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | changes are stationary over deployment time
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 34. Online Mapping and Motion Planning Under Uncertainty for Safe Navigation in Unknown Environments (2021)

- Authors: Èric Pairet, Juan David Hernández, Marc Carreras, Yvan Pétillot, Morteza Lahijanian
- Venue/source: IEEE Transactions on Automation Science and Engineering
- URL/DOI: https://doi.org/10.1109/tase.2021.3118737
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | closed-world maps remain valid outside the robot's recent sensor frustum | uncertainty is enough to decide when memory should be distrusted
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 35. Towards Persistent Localization and Mapping with a Continuous Appearance-based Topology (2012)

- Authors: William Maddern, Michael Milford, Gordon Wyeth
- Venue/source: https://doi.org/10.15607/rss.2012.viii.036
- URL/DOI: https://doi.org/10.15607/rss.2012.viii.036
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | map update and route choice can be separated without losing optimality | map memory can be trusted or discounted as a monotone function of elapsed time
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 36. SLAM algorithm applied to robotics assistance for navigation in unknown environments (2010)

- Authors: Fernando Auat Cheein, Natalia M. López, Carlos Soria, Fernando A di Sciascio, Фернандо Лобо Перейра, Ricardo Carelli
- Venue/source: Journal of NeuroEngineering and Rehabilitation
- URL/DOI: https://doi.org/10.1186/1743-0003-7-10
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 37. YES-SLAM: YOLOv7-enhanced-semantic visual SLAM for mobile robots in dynamic scenes (2023)

- Authors: Hang Liu, Jingwen Luo
- Venue/source: Measurement Science and Technology
- URL/DOI: https://doi.org/10.1088/1361-6501/ad14e7
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 38. Navigation Engine Design for Automated Driving Using INS/GNSS/3D LiDAR-SLAM and Integrity Assessment (2020)

- Authors: Kai‐Wei Chiang, Guang-Je Tsai, Yu-Hua Li, You Li, Naser El‐Sheimy
- Venue/source: Remote Sensing
- URL/DOI: https://doi.org/10.3390/rs12101564
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | long-horizon navigation is limited mainly by localization drift
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 39. Are We Ready for Service Robots? The OpenLORIS-Scene Datasets for Lifelong SLAM (2019)

- Authors: Xuesong Shi, Dongjiang Li, Pengpeng Zhao, Qinbin Tian, Yuxin Tian, Qiwei Long, et al.
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.1911.05603
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map memory can be trusted or discounted as a monotone function of elapsed time | long-horizon navigation is limited mainly by localization drift
- Variables treated as fixed: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 40. A Review of Deep Reinforcement Learning Algorithms for Mobile Robot Path Planning (2023)

- Authors: Ramanjeet Singh, Jing Ren, Xianke Lin
- Venue/source: Vehicles
- URL/DOI: https://doi.org/10.3390/vehicles5040078
- Problem claimed: Learn map, memory, or navigation policies from data instead of hand-engineered map updates.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 41. Development and Testing of an Autonomous Mobile Robot for Material Handling Using SLAM and Nav2 (2025)

- Authors: Prince Panta, Nirmal Prasad Panta, Pawan Shrestha, Saki Basnet, Surya Prasad Adhikari
- Venue/source: Journal of Advanced Mechanical Engineering Applications
- URL/DOI: https://doi.org/10.30880/jamea.2025.06.01.003
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 42. Occupancy Grid Models for Robot Mapping in Changing Environments (2021)

- Authors: Daniel Meyer-Delius, Maximilian Beinhofer, Wolfram Burgard
- Venue/source: Proceedings of the AAAI Conference on Artificial Intelligence
- URL/DOI: https://doi.org/10.1609/aaai.v26i1.8377
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 43. Robot Navigation and Map Construction Based on SLAM Technology (2024)

- Authors: Zihan Li, Chao Fan, Weike Ding, Kun Qian
- Venue/source: Journal of improved oil and gas recovery technology.
- URL/DOI: https://doi.org/10.53469/wjimt.2024.07(03).02
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: map estimation and localization novelty
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 44. Exploration and mapping with mobile robots (2006)

- Authors: Cyrill Stachniss
- Venue/source: FreiDok plus (Universitätsbibliothek Freiburg)
- URL/DOI: https://openalex.org/W195773586
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | a robot can repair stale beliefs only by revisiting the stale location
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 45. Loop Closure Detection for Visual SLAM Based on Deep Learning (2017)

- Authors: Hang Hu, Yunzhou Zhang, Qiang Duan, Meiyu Hu, Linzhuo Pang
- Venue/source: https://doi.org/10.1109/cyber.2017.8446473
- URL/DOI: https://doi.org/10.1109/cyber.2017.8446473
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 46. A Comparative Review on Enhancing Visual Simultaneous Localization and Mapping with Deep Semantic Segmentation (2024)

- Authors: Xiwen Liu, Yong He, Jue Li, Rui Yan, Xiaoyu Li, Hui Huang
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s24113388
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 47. Continuous shared control of a mobile robot with brain–computer interface and autonomous navigation for daily assistance (2023)

- Authors: Baoguo Xu, Deping Liu, Muhui Xue, Minmin Miao, Cong Hu, Aiguo Song
- Venue/source: Computational and Structural Biotechnology Journal
- URL/DOI: https://doi.org/10.1016/j.csbj.2023.07.033
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 48. Recent Advances in Visual SLAM: Taxonomy, Comparative Analysis, and Open Challenges (2025)

- Authors: Aidos Ibrayev, Батырхан Омаров
- Venue/source: Engineering Technology & Applied Science Research
- URL/DOI: https://doi.org/10.48084/etasr.13116
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | learned memory modules implicitly discover when to forget spatial facts
- Variables treated as fixed: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 49. STEP: Stochastic Traversability Evaluation and Planning for Risk-Aware Off-road Navigation (2021)

- Authors: David P. Fan, Kyohei Otsu, Y. Kubo, Anushri Dixit, Joel W. Burdick, Ali‐akbar Agha‐mohammadi
- Venue/source: https://doi.org/10.15607/rss.2021.xvii.021
- URL/DOI: https://doi.org/10.15607/rss.2021.xvii.021
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 50. Efficient navigation based on the Landmark-Tree map and the Z&lt;inf&gt;&amp;#x221E;&lt;/inf&gt; algorithm using an omnidirectional camera (2013)

- Authors: Bastian Jäger, Elmar Mair, Christoph Brand, Wolfgang Stürzl, Michael Suppa
- Venue/source: https://doi.org/10.1109/iros.2013.6696612
- URL/DOI: https://doi.org/10.1109/iros.2013.6696612
- Problem claimed: Represent traversability or occupancy so a mobile robot can plan through partially observed space.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | topological connectivity changes are rare compared with metric pose drift
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 51. Safe and Robust Map Updating For Long-Term Operations in Dynamic Environments (2023)

- Authors: Elisa Stefanini, Enrico Ciancolini, Alessandro Settimi, Lucia Pallottino
- Venue/source: Preprints.org
- URL/DOI: https://doi.org/10.20944/preprints202305.1387.v1
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map changes are observed at the place where they matter for the plan | environment changes are locally independent once the map cell or edge is represented
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 52. Autonomous Navigation for Differential Drive Robots: Grid-Based Fastslam with AMCL in ROS2 (2025)

- Authors: Victor Nosakhare Oriakhi
- Venue/source: International Journal of Latest Technology in Engineering Management & Applied Science
- URL/DOI: https://doi.org/10.51583/ijltemas.2025.1401016
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: map estimation and localization novelty | sensing-before-acting baseline
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 53. Aerial and Ground Robot Collaboration for Autonomous Mapping in Search and Rescue Missions (2020)

- Authors: Dimitrios Chatziparaschis, Michail G. Lagoudakis, Panagiotis Partsinevelos
- Venue/source: Drones
- URL/DOI: https://doi.org/10.3390/drones4040079
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module; occupancy/traversability grid representation.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: map estimation and localization novelty | learned memory/world-model framing
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 54. Development of a Service Robot for Hospital Environments in Rehabilitation Medicine with LiDAR-Based Simultaneous Localization and Mapping (2024)

- Authors: Sayat Ibrayev, Arman Ibrayeva, Bekzat Amanov, Serik Tolenov
- Venue/source: International Journal of Advanced Computer Science and Applications
- URL/DOI: https://doi.org/10.14569/ijacsa.2024.01511102
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 55. From Machinery to Biology: A Review on Mapless Autonomous Underwater Navigation (2025)

- Authors: Wenxi Zhu, Weicheng Cui
- Venue/source: Journal of Marine Science and Engineering
- URL/DOI: https://doi.org/10.3390/jmse13112202
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 56. Lidar SLAM for Mobile Robot in an Indoor Environment (2025)

- Authors: Kambire Sie Stephane
- Venue/source: International Journal for Research in Applied Science and Engineering Technology
- URL/DOI: https://doi.org/10.22214/ijraset.2025.71701
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 57. General Place Recognition Survey: Towards Real-World Autonomy (2024)

- Authors: Peng Yin, J. B. Jiao, Shiqi Zhao, Lingyun Xu, Guoquan Huang, Howie Choset, et al.
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2405.04812
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 58. Combining Hector SLAM and Artificial Potential Field for Autonomous Navigation Inside a Greenhouse (2018)

- Authors: El Houssein Chouaib Harik, Audun Korsæth
- Venue/source: Robotics
- URL/DOI: https://doi.org/10.3390/robotics7020022
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 59. Learning Composable Behavior Embeddings for Long-Horizon Visual Navigation (2021)

- Authors: Xiangyun Meng, Xiang Yu, Dieter Fox
- Venue/source: IEEE Robotics and Automation Letters
- URL/DOI: https://doi.org/10.1109/lra.2021.3060649
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 60. BDGS-SLAM: A Probabilistic 3D Gaussian Splatting Framework for Robust SLAM in Dynamic Environments (2025)

- Authors: Tianyu Yang, Shuangfeng Wei, Jingxuan Nan, Mingyang Li, Mingrui Li
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s25216641
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | environment changes are locally independent once the map cell or edge is represented
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 61. A Review of Dynamic Object Filtering in SLAM Based on 3D LiDAR (2024)

- Authors: Hongrui Peng, Ziyu Zhao, Liguan Wang
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s24020645
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure.
- Hidden assumptions: long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Variables treated as fixed: change process behind loop closures/map factors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 62. Robot Path Planning Navigation for Dense Planting Red Jujube Orchards Based on the Joint Improved A* and DWA Algorithms under Laser SLAM (2022)

- Authors: Yufeng Li, Jingbin Li, Wenhao Zhou, Qingwang Yao, Jing Nie, Xiaochen Qi
- Venue/source: Agriculture
- URL/DOI: https://doi.org/10.3390/agriculture12091445
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 63. Learning Composable Behavior Embeddings for Long-horizon Visual\n Navigation (2021)

- Authors: Xiangyun Meng, Xiang Yu, Dieter Fox
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2102.09781
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 64. Building an Integrated Mobile Robotic System for Real-Time Applications in Construction (2018)

- Authors: Khashayar Asadi, Hariharan Ramshankar, Harish Pullagurla, Aishwarya Bhandare, Suraj Shanbhag, Pooja Mehta, et al.
- Venue/source: Proceedings of the ... ISARC
- URL/DOI: https://doi.org/10.22260/isarc2018/0063
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: map estimation and localization novelty | sensing-before-acting baseline
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 65. Semi-direct RGB-D slam algorithm for mobile robot In dynamic indoor environments (2018)

- Authors: Rui Tian, Yunzhou Zhang, Chengqiang Gao, Yi Deng, Hao Jiang
- Venue/source: Electronic scientific archive of UrFU (Ural Federal University)
- URL/DOI: http://rep.bntu.by/handle/data/52767
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 66. A Systematic Literature Review on Long-Term Localization and Mapping for Mobile Robots (2022)

- Authors: Ricardo B. Sousa, Héber Sobreira, Antonio Moreira
- Venue/source: https://doi.org/10.22541/au.166739295.55264285/v1
- URL/DOI: https://doi.org/10.22541/au.166739295.55264285/v1
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map memory can be trusted or discounted as a monotone function of elapsed time | long-horizon navigation is limited mainly by localization drift | the robot's own unobserved absence does not create information about likely map changes
- Variables treated as fixed: change process behind loop closures/map factors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | visual relocalization succeeds while the path itself has changed
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 67. Leveraging Pedestrian Detection and Tracking in Robotics Navigation: A Survey With Practical Illustrations (2025)

- Authors: N. Picello, F. Herrero, S. Hernández, A. López, Àngel Santamaria‐Navarro
- Venue/source: IEEE Access
- URL/DOI: https://doi.org/10.1109/access.2025.3607191
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 68. Safe-Nav: learning to prevent PointGoal navigation failure in unknown environments (2022)

- Authors: Sheng Jin, Qing‐Hao Meng, Xu-Yang Dai, Hui-Rang Hou
- Venue/source: Complex & Intelligent Systems
- URL/DOI: https://doi.org/10.1007/s40747-022-00648-2
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | uncertainty-aware navigation baseline | learned memory/world-model framing
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 69. Visual Place Recognition: A Survey (2015)

- Authors: Stephanie Lowry, Niko Sünderhauf, Paul Newman, John J. Leonard, David Cox, Peter Corke, et al.
- Venue/source: IEEE Transactions on Robotics
- URL/DOI: https://doi.org/10.1109/tro.2015.2496823
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map changes are observed at the place where they matter for the plan | change probability is a property of places rather than of unobserved interventions that could have reached them | appearance drift is the main source of long-term navigation failure
- Variables treated as fixed: route-level cost of stale-map errors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 70. LCPF: A Particle Filter Lidar SLAM System With Loop Detection and Correction (2020)

- Authors: Fuyu Nie, Weimin Zhang, Zhuo Yao, Yongliang Shi, Fangxing Li, Qiang Huang
- Venue/source: IEEE Access
- URL/DOI: https://doi.org/10.1109/access.2020.2968353
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 71. Obstacle Detection System for Agricultural Mobile Robot Application Using RGB-D Cameras (2021)

- Authors: Magda Skoczeń, Marcin Ochman, Krystian Spyra, Maciej Nikodem, Damian Krata, Marcin Panek, et al.
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s21165292
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: route-level cost of stale-map errors | hazard model connecting uncertainty to physical change | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 72. A Survey on Active Simultaneous Localization and Mapping: State of the Art and New Frontiers (2023)

- Authors: Julio A. Placed, Jared Strader, Henry Carrillo, Nikolay Atanasov, Vadim Indelman, Luca Carlone, et al.
- Venue/source: IEEE Transactions on Robotics
- URL/DOI: https://doi.org/10.1109/tro.2023.3248510
- Problem claimed: Plan robot motion when the map, state, or traversability model is uncertain.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | uncertainty-aware navigation baseline | sensing-before-acting baseline
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 73. Robust Visual Robot Localization Across Seasons Using Network Flows (2014)

- Authors: Tayyab Naseer, Luciano Spinello, Wolfram Burgard, Cyrill Stachniss
- Venue/source: Proceedings of the AAAI Conference on Artificial Intelligence
- URL/DOI: https://doi.org/10.1609/aaai.v28i1.9057
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 74. Real-Time Object Navigation With Deep Neural Networks and Hierarchical Reinforcement Learning (2020)

- Authors: Aleksey Staroverov, Dmitry Yudin, Ilya Belkin, Vasily Adeshkin, Yaroslav Solomentsev, Aleksandr I. Panov
- Venue/source: IEEE Access
- URL/DOI: https://doi.org/10.1109/access.2020.3034524
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: learned memory/world-model framing
- What it leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 75. Simultaneous Localization and Mapping (SLAM) and Data Fusion in Unmanned Aerial Vehicles: Recent Advances and Challenges (2022)

- Authors: Abhishek Gupta, Xavier Fernando
- Venue/source: Drones
- URL/DOI: https://doi.org/10.3390/drones6040085
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: map estimation and localization novelty
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 76. Deep Learning for Visual SLAM: The State-of-the-Art and Future Trends (2023)

- Authors: Margarita N. Favorskaya
- Venue/source: Electronics
- URL/DOI: https://doi.org/10.3390/electronics12092006
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | map changes are observed at the place where they matter for the plan | learned memory modules implicitly discover when to forget spatial facts
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 77. Vision-Based Mobile Robotics Obstacle Avoidance With Deep Reinforcement Learning (2021)

- Authors: Patrick Wenzel, Torsten Schön, Laura Leal-Taixé, Daniel Cremers
- Venue/source: https://doi.org/10.1109/icra48506.2021.9560787
- URL/DOI: https://doi.org/10.1109/icra48506.2021.9560787
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: learned memory/world-model framing
- What it leaves open: Expose a mechanism that a learned memory can be tested against under controlled stale-map hazards.

## 78. AEKF-SLAM: A New Algorithm for Robotic Underwater Navigation (2017)

- Authors: Xin Yuan, José-Fernán Martí­nez-Ortega, José María Rodríguez Fernández, Martina Eckert
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s17051174
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | long-horizon navigation is limited mainly by localization drift | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 79. Multiple map hypotheses for planning and navigating in non-stationary environments (2014)

- Authors: Timothy Morris, Feras Dayoub, Peter Corke, Gordon Wyeth, Ben Upcroft
- Venue/source: https://doi.org/10.1109/icra.2014.6907255
- URL/DOI: https://doi.org/10.1109/icra.2014.6907255
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the robot's own unobserved absence does not create information about likely map changes | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 80. Generation of Indoor Open Street Maps for Robot Navigation from CAD Files (2025)

- Authors: Jiajie Zhang, Sifan Wu, Xu Ma, Sören Schwertfeger
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2507.00552
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: topological connectivity changes are rare compared with metric pose drift | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 81. Classical and Heuristic Approaches for Mobile Robot Path Planning: A Survey (2023)

- Authors: Jaafar Ahmed Abdulsaheb, Dheyaa Jasim Kadhim
- Venue/source: Robotics
- URL/DOI: https://doi.org/10.3390/robotics12040093
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 82. Comparing LiDAR and IMU-based SLAM approaches for 3D robotic mapping (2023)

- Authors: Diego Tiozzo Fasiolo, Lorenzo Scalera, Eleonora Maset
- Venue/source: Robotica
- URL/DOI: https://doi.org/10.1017/s026357472300053x
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 83. OGM2PGBM: Robust BIM-based 2D-LiDAR localization for lifelong indoor navigation (2023)

- Authors: Miguel Arturo Vega Torres, Alexander Braun, A. Borrmann
- Venue/source: https://doi.org/10.1201/9781003354222-72
- URL/DOI: https://doi.org/10.1201/9781003354222-72
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: environment changes are locally independent once the map cell or edge is represented | topological connectivity changes are rare compared with metric pose drift | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 84. Learning Forward Dynamics Model and Informed Trajectory Sampler for Safe Quadruped Navigation (2022)

- Authors: Yunho Kim, Chanyoung Kim, Jemin Hwangbo
- Venue/source: https://doi.org/10.15607/rss.2022.xviii.069
- URL/DOI: https://doi.org/10.15607/rss.2022.xviii.069
- Problem claimed: Choose sensing or exploration actions that improve map quality for navigation.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | sensing-before-acting baseline | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 85. SLAM, Path Planning Algorithm and Application Research of an Indoor Substation Wheeled Robot Navigation System (2022)

- Authors: Jianxin Ren, Tao Wu, Xiaohua Zhou, Congcong Yang, Jiahui Sun, Mingshuo Li, et al.
- Venue/source: Electronics
- URL/DOI: https://doi.org/10.3390/electronics11121838
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map; occupancy/traversability grid representation.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | the same trust policy is appropriate for exploratory detours and mission-critical route edges | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 86. Hybrid, metric - topological, mobile robot navigation (2001)

- Authors: Nicola Tomatis
- Venue/source: Infoscience (Ecole Polytechnique Fédérale de Lausanne)
- URL/DOI: https://doi.org/10.5075/epfl-thesis-2444
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; probabilistic belief or risk model; planner or policy over the represented map.
- Hidden assumptions: the cost of being wrong is proportional to local reconstruction error | map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 87. Visual Localization and Mapping in Dynamic and Changing Environments (2023)

- Authors: João Carlos Virgolino Soares, Vivian Suzano Medeiros, Gabriel Fischer Abati, Marcelo Becker, Glauco A. P. Caurin, Marcelo Gattass, et al.
- Venue/source: Journal of Intelligent & Robotic Systems
- URL/DOI: https://doi.org/10.1007/s10846-023-02019-6
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Variables treated as fixed: change process behind loop closures/map factors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | high entropy in harmless regions distracts from low-entropy dangerous stale edges
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | uncertainty-aware navigation baseline
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 88. Language, Environment, and Robotic Navigation (2024)

- Authors: Johnathan E. Avery
- Venue/source: arXiv (Cornell University)
- URL/DOI: https://doi.org/10.48550/arxiv.2404.03049
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | learned memory modules implicitly discover when to forget spatial facts | closed-world maps remain valid outside the robot's recent sensor frustum
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: map estimation and localization novelty | learned memory/world-model framing
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 89. An Efficient Guiding Manager for Ground Mobile Robots in Agriculture (2023)

- Authors: Luis Emmi, Roemí Fernández, P. González de Santos
- Venue/source: Robotics
- URL/DOI: https://doi.org/10.3390/robotics13010006
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Actual mechanism introduced: planner or policy over the represented map.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors
- Failure modes ignored: planner repeatedly commits to stale bottlenecks
- What it makes less novel: broad navigation/mapping context
- What it leaves open: Explain when old spatial memory should be distrusted during embodied operation.

## 90. Exploration-Based SLAM (e-SLAM) for the Indoor Mobile Robot Using Lidar (2022)

- Authors: Hasan Ismail, Rohit Roy, Long-Jye Sheu, Wei-Hua Chieng, Li‐Chuan Tang
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s22041689
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; information-gain driven sensing/exploration.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 91. YDD-SLAM: Indoor Dynamic Visual SLAM Fusing YOLOv5 with Depth Information (2023)

- Authors: Peichao Cong, Junjie Liu, Jiaxing Li, Yixuan Xiao, Xilai Chen, Xinjie Feng, et al.
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s23239592
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 92. Comparison of DSO and ORB‐SLAM3 in Low‐Light Environments With Auxiliary Lighting and Deep Learning Based Image Enhancing (2025)

- Authors: Francesco Crocetti, Raffaele Brilli, Alberto Dionigi, Mario Luca Fravolini, Gabriele Costante, Paolo Valigi
- Venue/source: Journal of Field Robotics
- URL/DOI: https://doi.org/10.1002/rob.22595
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map; visual place-recognition or appearance-invariant localization; learned representation or neural memory module.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: map estimation and localization novelty | learned memory/world-model framing
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 93. SGC-VSLAM: A Semantic and Geometric Constraints VSLAM for Dynamic Indoor Environments (2020)

- Authors: Shiqiang Yang, Guohao Fan, Lele Bai, Cheng Zhao, Dexin Li
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s20082432
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: long-horizon navigation is limited mainly by localization drift | dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them
- Variables treated as fixed: change process behind loop closures/map factors | object persistence and affordance dynamics | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 94. Visual Place Recognition for Autonomous Mobile Robots (2017)

- Authors: Michael Horst, Ralf Möller
- Venue/source: Robotics
- URL/DOI: https://doi.org/10.3390/robotics6020009
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map changes are observed at the place where they matter for the plan | appearance drift is the main source of long-term navigation failure | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 95. Mobile Robot Navigation for Person Following in Indoor Environments (2013)

- Authors: Ninad Pradhan
- Venue/source: TigerPrints (Clemson University)
- URL/DOI: https://tigerprints.clemson.edu/all_dissertations/1186
- Problem claimed: Recognize places and recover localization despite visual appearance changes.
- Actual mechanism introduced: change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error | replanning after a failure is an acceptable substitute for modeling stale-map hazard
- Variables treated as fixed: route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | planner repeatedly commits to stale bottlenecks | visual relocalization succeeds while the path itself has changed
- What it makes less novel: generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 96. Key Technologies for Real-time Localization and Scene Semantic Segmentation of Mobile Robots in Dynamic Environments (2025)

- Authors: Long-Xue Cheng, Junxia Han
- Venue/source: 電腦學刊
- URL/DOI: https://doi.org/10.63367/199115992025103605026
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; semantic/object-level map structure; planner or policy over the represented map; learned representation or neural memory module.
- Hidden assumptions: dynamic objects are nuisance measurements to remove from a static map | change probability is a property of places rather than of unobserved interventions that could have reached them | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling | learned memory/world-model framing
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 97. Collaborative Mobile Robotics for Semantic Mapping: A Survey (2022)

- Authors: Abdessalem Achour, Hiba Al-Assaad, Yohan Dupuis, Madeleine El Zaher
- Venue/source: Applied Sciences
- URL/DOI: https://doi.org/10.3390/app122010316
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: semantic/object-level map structure; planner or policy over the represented map.
- Hidden assumptions: closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges | the cost of being wrong is proportional to local reconstruction error
- Variables treated as fixed: route-level cost of stale-map errors | object persistence and affordance dynamics
- Failure modes ignored: planner repeatedly commits to stale bottlenecks | semantic persistence masks moved obstacles or closed doors
- What it makes less novel: broad navigation/mapping context
- What it leaves open: Use semantic activity affordances to predict which old map facts deserve distrust.

## 98. Simultaneous localization and mapping of mobile robots with multi-sensor fusion (2023)

- Authors: Kui Zhang, Haihua Cui, Xiaomei Yan
- Venue/source: Applied Mathematics and Nonlinear Sciences
- URL/DOI: https://doi.org/10.2478/amns.2023.2.00488
- Problem claimed: Reuse prior spatial experience or map memory for later robot navigation.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; planner or policy over the represented map.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors
- Failure modes ignored: locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty
- What it leaves open: Separate pose/map estimation confidence from whether a stale spatial fact remains action-worthy.

## 99. Adaptive Monocular Visual–Inertial SLAM for Real-Time Augmented Reality Applications in Mobile Devices (2017)

- Authors: Jin-Chun Piao, Shin‐Dug Kim
- Venue/source: Sensors
- URL/DOI: https://doi.org/10.3390/s17112567
- Problem claimed: Maintain localization and maps when the robot's environment changes over long deployments.
- Actual mechanism introduced: SLAM/pose-graph or map-estimation machinery; change handling or dynamic-object filtering; planner or policy over the represented map; visual place-recognition or appearance-invariant localization.
- Hidden assumptions: map update and route choice can be separated without losing optimality | closed-world maps remain valid outside the robot's recent sensor frustum | the same trust policy is appropriate for exploratory detours and mission-critical route edges
- Variables treated as fixed: change process behind loop closures/map factors | route-level cost of stale-map errors | physical traversability behind appearance drift
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | locally consistent maps hide task-critical topology changes | planner repeatedly commits to stale bottlenecks
- What it makes less novel: map estimation and localization novelty | generic dynamic-environment handling
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.

## 100. PLGRIM: Hierarchical Value Learning for Large-scale Exploration in Unknown Environments (2021)

- Authors: Sung-Kyun Kim, Amanda Bouman, Gautam Salhotra, David D. Fan, Kyohei Otsu, Joel W. Burdick, et al.
- Venue/source: Proceedings of the International Conference on Automated Planning and Scheduling
- URL/DOI: https://doi.org/10.1609/icaps.v31i1.16014
- Problem claimed: Use semantic or object-level structure to support embodied navigation and map reasoning.
- Actual mechanism introduced: change handling or dynamic-object filtering; semantic/object-level map structure; probabilistic belief or risk model; planner or policy over the represented map; information-gain driven sensing/exploration; learned representation or neural memory module.
- Hidden assumptions: change probability is a property of places rather than of unobserved interventions that could have reached them | the cost of being wrong is proportional to local reconstruction error | uncertainty is enough to decide when memory should be distrusted
- Variables treated as fixed: route-level cost of stale-map errors | object persistence and affordance dynamics | hazard model connecting uncertainty to physical change
- Failure modes ignored: unobserved reachable changes invalidate an old shortcut | high entropy in harmless regions distracts from low-entropy dangerous stale edges | planner repeatedly commits to stale bottlenecks
- What it makes less novel: generic dynamic-environment handling | uncertainty-aware navigation baseline | sensing-before-acting baseline
- What it leaves open: Tie memory distrust to unobserved physical opportunities for change and downstream route consequence.
