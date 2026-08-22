> Bot-produced scouting packet. It is evidence support, not a student-verified literature review or novelty decision.

## Outcome

FaultAdapt-Gym sits in a **crowded intersection** of robust RL, contextual/meta-RL, non-stationary latent dynamics, continual robot learning, and fault-adaptive control. Several proposed ingredients already appear separately—and sometimes together—in prior work. The strongest potential contribution is therefore a **carefully standardized, CPU-first evaluation protocol**, not the mere presence of actuator faults or hidden changing dynamics.

## Comparison matrix

| Work | Main setting / interface | Dynamics or fault variation | Hidden and time-varying? | Adaptation/evaluation emphasis | Potential duplication with FaultAdapt-Gym |
|---|---|---|---|---|---|
| **Robust Gymnasium** (ICLR 2025) | Gymnasium-compatible control, MuJoCo, Box2D, manipulation, safety, dexterous and multi-agent tasks | Perturbations to observations, rewards, actions, and environment dynamics; random/adversarial/arbitrary disruptions | Supports step-wise perturbations at configurable times; not specifically organized around hidden actuator-health inference | Robustness and domain adaptation across a large modular task collection | **Very high wrapper-level overlap:** action corruption, dynamics shifts, Gymnasium API, robot-control tasks, and temporal disruptions already exist. FaultAdapt must show more than a smaller fault wrapper suite. |
| **CARL** (2021/2023) | Contextual extensions to classic control, Box2D, Brax, `dm_control`, etc. | Gravity, friction, joint strength, torso mass and other configurable physics contexts | Context changes are normally selected on reset and, by default, included in observations; features can be restricted to construct less-observed settings | Intra-task generalization over contextual instances | **High overlap** for payload, friction, actuator strength and train/test context splits. FaultAdapt’s distinction would need to be hidden, within-episode degradation and adaptation metrics—not contextual parameter variation itself. |
| **ODRL** (NeurIPS Datasets & Benchmarks 2024) | Unified benchmark for off-dynamics RL | Broad source/target dynamics mismatches; online/offline source and target combinations | Primarily source-to-target domain mismatch, rather than a hidden fault trajectory within one rollout | Transfer/adaptation to a target dynamics domain; unified algorithm baselines | **High overlap** if FaultAdapt is framed merely as adaptation to changed dynamics. A temporal fault process and fault-specific metrics would be needed to separate it. |
| **DynaMITE-RL** (NeurIPS 2024) | Gridworld, continuous control, and simulated assistive-robot tasks | Latent environment state evolves at varying rates; episode divided into sessions in which latent state is fixed | **Yes:** latent state changes within an episode/session sequence and must be inferred | History-based temporal meta-RL and latent inference under non-stationarity | **Very high conceptual overlap** with hidden, time-varying degradation and memory-based adaptation. Fault semantics alone are not enough unless protocols and metrics differ materially. |
| **SunBlaze / Assessing Generalization in DRL** (2018) | Gym-style benchmark and experimental protocol | Parameterized environment variants for in-distribution and out-of-distribution generalization | Generally fixed environment instance/parameters rather than an online fault process | Controlled train/test generalization assessment | **Moderate overlap** for parameter ranges and held-out dynamics. Its main lesson is that FaultAdapt needs explicit in-range, interpolation and extrapolation splits. |
| **UP-OSI: Universal Policy with Online System Identification** (RSS 2017) | Cart-pole, double inverted pendulum, hopper locomotion, manipulator block throwing | Mass, inertia, friction and unknown manipulated-object mass; responsive to sudden changes | Dynamics parameters are unknown and inferred from recent state-action history | Explicit online system identification feeding a dynamics-conditioned universal policy | **Direct duplication of the proposed explicit-OSI baseline and comparison question.** FaultAdapt cannot present “memory versus online identification” as an unexplored idea; it can standardize and extend the comparison to fault processes. |
| **Error-Aware Policy Learning** (RSS 2021) | Assistive walking device plus standard RL control tasks | Unobserved robot/environment parameters and biomechanical differences | Hidden parameters; an error predictor summarizes their effect | Zero-shot adaptation using predicted future-state error | **Moderate-to-high overlap** with history/error-based implicit identification. This is an important non-recurrent adaptation baseline or conceptual comparator. |
| **Complementary Meta-RL for Fault-Adaptive Control** (PHM 2020) | Aircraft fuel-transfer control | Abrupt system faults | Abrupt changes; controller evaluates a library of policies after a fault | Rapid fault adaptation using a MAML-derived policy library | **Direct fault-tolerant-RL overlap.** It is domain-specific rather than a reusable Gymnasium robot benchmark, but blocks broad claims that meta-RL fault adaptation is new. |
| **Continual World** (NeurIPS 2021) | Sequence of Meta-World robotic manipulation tasks; CW20 uses 20 tasks with one-million-step budgets per task | Sequential task changes rather than actuator-health changes | Task identity changes across long training stages, not typically hidden within an episode | Forward transfer, forgetting and continual-learning performance | **Moderate overlap** if FaultAdapt claims continual adaptation broadly. Less direct if FaultAdapt freezes policy weights and evaluates fast within-rollout adaptation. |
| **Meta-World** (CoRL 2019) | 50 simulated manipulation tasks for multi-task and meta-RL | Task/object-position variation; not principally actuator faults | Task-conditioned/meta-learning protocols | Fast acquisition and generalization to held-out behaviors | Mostly neighboring infrastructure. It already covers robot meta-RL, so FaultAdapt should avoid claiming to introduce robot-control meta-adaptation generally. |

## Where the proposal most likely duplicates prior work

1. **Generic Gym/Gymnasium perturbation wrappers:** Robust Gymnasium already perturbs actions and dynamics with configurable timing across many control and robot environments.
2. **Parameterized physics contexts:** CARL and SunBlaze already provide structured train/test variation of friction, mass, strength and other dynamics.
3. **Hidden temporal context inference:** DynaMITE-RL already studies latent variables changing at different rates inside episodes.
4. **Explicit online system identification:** UP-OSI already estimates hidden dynamics from recent state/action history and feeds the estimate to a universal policy, including sudden changes.
5. **Fault-adaptive meta-RL:** Complementary Meta-RL already treats abrupt faults and rapid policy adaptation.
6. **Continual robot adaptation:** Continual World already provides standardized robot-control sequences and transfer/forgetting metrics, although its changes are task-level rather than actuator-health trajectories.

Thus, a package that only adds `action *= health`, latency queues, payload/friction randomization, and an LSTM-versus-identifier experiment would likely be viewed as a **recombination of established components**.

## Three sharply scoped, CPU-feasible differentiators

### 1. Fault identifiability benchmark, not just a perturbation suite

Use only lightweight environments—Pendulum, CartPole continuous control, Acrobot, and one simple planar two-link arm—and construct **matched hidden contexts that are behaviorally ambiguous without informative actions**.

Example pairs:

- actuator gain loss versus increased payload;
- command bias versus constant external load;
- one-step latency versus actuator low-pass response.

Require evaluation under:

- passive task execution;
- a fixed diagnostic action prefix;
- learned active probing with a small probe-energy budget.

Report context-estimation error, uncertainty calibration, task regret, probe cost, and recovery time. This creates a focused question—**when can a controller identify the cause of degraded behavior?**—that generic robustness suites do not standardize.

### 2. Held-out temporal fault-grammar protocol

Define a small, versioned grammar for trajectories such as:

- abrupt gain loss;
- linear or exponential wear;
- intermittent dropout;
- bias drift;
- latency jumps;
- fault recovery;
- two-stage and simultaneous fault combinations.

Train on single faults and fixed change rates; test on **unseen compositions, orderings, severities and change rates**. Keep the underlying task and reward unchanged. Publish exact seeds and schedules.

Core metrics should be change-point-aligned:

- pre-fault return;
- worst post-change return;
- recovery half-life;
- cumulative recovery regret;
- stability/failure rate;
- performance after a second change.

This differs more clearly from static contextual generalization and from continual task sequences, while remaining cheap to run.

### 3. Mechanism-matched adaptation bake-off

Standardize four controllers with approximately matched parameter counts and identical training data:

1. history-free robust policy;
2. recurrent/history policy;
3. explicit online identifier plus parameter-conditioned policy;
4. oracle policy given the true hidden fault state.

Freeze all policy weights at evaluation; only recurrent state or online estimates may update. Evaluate history-window length, identifier misspecification, observation noise, and rapid versus slow changes. Include a tiny linear or least-squares identifier wherever possible so every baseline runs on CPU.

The differentiator is the **controlled benchmark protocol and diagnostic gap decomposition**, not the novelty of either recurrent adaptation or OSI. Useful reported gaps would be:

- robust-policy → adaptive-policy gain;
- recurrent → explicit-identification gap;
- adaptive → oracle gap;
- in-distribution → held-out fault-grammar gap.

## What must be verified before making any novelty statement

- Inspect Robust Gymnasium’s current code and supplement to determine whether it already implements actuator gain loss, stuck/dead actuators, command bias, latency queues, and within-episode fault schedules—not merely generic action noise.
- Inspect CARL’s current selectors and observation configuration to establish exactly which contexts can change within an episode and how fully context can be hidden.
- Inspect ODRL task definitions for actuator-strength changes, crippled-agent tasks, and online target adaptation protocols.
- Inspect DynaMITE-RL’s continuous-control configurations and session-generation code for overlap with fault onset, drift, recurrence and recovery.
- Search the citation graph and 2025–2026 robotics/control literature for “crippled robot,” “actuator degradation,” “motor failure,” “fault-adaptive RL,” “temporal meta-RL,” and “active system identification.” This landscape check cannot establish absence.
- Separate claims carefully: novelty of **environments**, **fault process**, **metrics**, **protocol**, and **baseline comparison** are different claims.
- Verify that every planned task genuinely runs under the claimed CPU budget and current Gymnasium API, with reproducible wall-clock and sample budgets.

## Primary-source evidence packet

- **Robust Gymnasium paper:** https://arxiv.org/abs/2502.19652  
  **Code:** https://github.com/SafeRL-Lab/Robust-Gymnasium
- **CARL paper:** https://arxiv.org/abs/2110.02102  
  **Code/docs:** https://github.com/automl/CARL
- **ODRL paper:** https://arxiv.org/abs/2410.20750  
  **Code:** https://github.com/OffDynamicsRL/off-dynamics-rl
- **DynaMITE-RL:** https://arxiv.org/abs/2402.15957
- **SunBlaze/generalization benchmark:** https://arxiv.org/abs/1810.12282
- **UP-OSI, RSS primary proceedings:** https://www.roboticsproceedings.org/rss13/p48.html
- **Error-Aware Policy Learning, RSS primary proceedings:** https://www.roboticsproceedings.org/rss17/p065.html
- **Complementary Meta-RL for Fault-Adaptive Control:** https://arxiv.org/abs/2009.12634
- **Continual World:** https://arxiv.org/abs/2105.10919  
  **Code:** https://github.com/awarelab/continual_world
- **Meta-World:** https://arxiv.org/abs/1910.10897  
  **Code:** https://github.com/Farama-Foundation/Metaworld

## Bottom line

Do **not** claim that FaultAdapt-Gym is the first benchmark for dynamics shifts, hidden contexts, online adaptation, actuator disruption, or fault-tolerant RL. A defensible project could instead be framed as:

> A CPU-first, Gymnasium-compatible diagnostic protocol for comparing implicit-memory and explicit-identification controllers under hidden, compositional actuator-fault trajectories, with change-point-aligned recovery and identifiability metrics.

No workspace files were created or modified. The main research issue was intermittent web-extraction rate limiting; primary pages, repositories, arXiv metadata, and RSS proceedings were checked through direct source access as a fallback.
