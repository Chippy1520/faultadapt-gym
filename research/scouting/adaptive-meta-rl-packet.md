> Bot-produced scouting packet. It is evidence support, not a student-verified literature review or novelty decision.

# FaultAdapt-Gym: evidence-first literature scouting packet

**Scope.** Adaptive/meta reinforcement learning and adjacent online identification methods for **hidden, fixed, sudden, and time-varying actuator faults**. The packet is designed to support, not replace, the student's reading and interpretation.

## Evidence conventions

- **Evidence** reports what a primary paper actually implements, tests, or states.
- **Scope boundary** is an observable omission in that paper's experiments; it is not proof that the broader literature lacks the feature.
- **Candidate gap** is a hypothesis to test with further searching and reading, not a research conclusion.
- “Official code” means author/paper-linked code. A third-party reimplementation is not presented as official.

## At-a-glance relevance map

| # | Primary paper | Adaptation mechanism | Fault/dynamics regime actually tested | Direct relevance |
|---|---|---|---|---|
| 1 | Yu et al. (2017), UP-OSI | Explicit online system identification + conditioned universal policy | Unknown parameters; responsiveness to changing dynamics | Explicit-ID comparator |
| 2 | Duan et al. (2016), RL² | Recurrent policy learns an implicit fast RL algorithm | Hidden task/MDP; not actuator faults | Recurrent-policy foundation |
| 3 | Nagabandi et al. (2019) | Gradient- or recurrence-adapted dynamics model + MPC | Disabled joints/crippled legs, including mid-rollout changes | Sudden hidden damage |
| 4 | Rakelly et al. (2019), PEARL | Probabilistic latent context inference | Task and dynamics variation fixed at task/episode scale | Explicit latent inference |
| 5 | Zintgraf et al. (2020), VariBAD | Recurrent variational belief + policy | Hidden task/system parameters fixed per task | Belief-based recurrent adaptation |
| 6 | Ahmed et al. (2020), C-MRL | MAML-style policy update using a complement/library of prior fault policies | Abrupt novel faults | Fault-adaptive meta-RL |
| 7 | Ahmed et al. (2020), mixed on-policy FTC | Online PPO plus periodic model-assisted offline updates | Progressive/incidental degradation | Gradual time variation |
| 8 | Yel & Bezzo (2021) | MAML-adapted predictor + trajectory-reference correction | Unseen actuator loss/bias; runtime re-learning | Explicit predictive adaptation |
| 9 | Dai et al. (2022) | Multiple meta-DDPG initializations + situation embedding + online fine-tuning | Sudden wheel loss-of-effectiveness faults | Direct actuator FTC |
| 10 | Kumar et al. (2021), RMA | History-to-latent adaptation module + conditioned PPO base policy | Parameters resampled within episode; terrain/payload/motor strength | Rapid implicit adaptation |
| 11 | Wu et al. (2023), Adapt | Transformer history model distilled from fault-conditioned PPO teachers | Sudden continuous joint torque degradation | Direct actuator degradation |

---

## 1) Preparing for the Unknown: Learning a Universal Policy with Online System Identification (UP-OSI)

**Citation.** Wenhao Yu, Jie Tan, C. Karen Liu, and Greg Turk. “Preparing for the Unknown: Learning a Universal Policy with Online System Identification.” *Robotics: Science and Systems*, 2017.  
Paper: https://arxiv.org/abs/1702.02453 · PDF: https://arxiv.org/pdf/1702.02453

**Evidence — contribution.** Learns (i) a universal policy conditioned on physical model parameters and (ii) an online system-identification network mapping a short state-action history to those parameters. OSI training is iterated using “bad cases” generated when estimated and true parameters differ, reducing compounding closed-loop identification error.

**Evidence — experiments/settings.** PyDART/DART simulation at a 0.002 s timestep; TRPO; two 64-unit hidden layers for the universal policy; OSI hidden layers 256/128/64 with dropout 0.1; history length 3; 500 TRPO updates and five OSI iterations. Tasks include double inverted pendulum (unknown centre of mass), block throwing (unknown object mass), Hopper (friction coefficient 0.3–1.0), and cart-pole swing-up (pole length and attached mass). The paper also evaluates test parameters outside training ranges and discusses responsiveness to sudden parameter changes.

**Evidence — limitations/scope.** All reported results are simulated. The unknown quantities are selected physical/task parameters rather than a general unstructured fault state. The policy requires a parameterization chosen by the designer. **Scope boundary:** no fixed-vs-sudden-vs-gradual actuator-efficiency protocol and no feed-forward/recurrent/adaptive-ID comparison under one fault benchmark.

**Official code.** No author-linked repository was located in the paper/project search; do not substitute an unofficial implementation without labeling it.

**Student questions.**
1. Is OSI accuracy itself necessary, or is control return the only meaningful criterion when parameters are not identifiable?
2. Which actuator-fault variables in FaultAdapt-Gym would be identifiable from a three-step state-action history?
3. How should an explicit-ID baseline be penalized or credited for privileged parameter labels during training?

---

## 2) RL²: Fast Reinforcement Learning via Slow Reinforcement Learning

**Citation.** Yan Duan, John Schulman, Xi Chen, Peter L. Bartlett, Ilya Sutskever, and Pieter Abbeel. “RL²: Fast Reinforcement Learning via Slow Reinforcement Learning.” 2016/ICLR 2017 workshop-era paper.  
Paper: https://arxiv.org/abs/1611.02779 · PDF: https://arxiv.org/pdf/1611.02779

**Evidence — contribution.** Trains an RNN with a “slow” RL optimizer so that its hidden-state dynamics implement a “fast” learning algorithm. At each step it receives state/observation, previous action, reward, and termination flag; recurrent state persists across episodes of the same sampled MDP.

**Evidence — experiments/settings.** GRU policy optimized with TRPO (and optional GAE). Evaluated on Bernoulli multi-armed bandits (5, 10, 50 arms; interaction horizons 10, 100, 500), random tabular MDPs (10 states, 5 actions, horizon 10), and a vision-based navigation POMDP. It is not a locomotion/fault study.

**Evidence — limitations/scope.** The authors report a performance gap in the hardest 50-arm/500-step setting and attribute room for improvement to the slow RL optimizer. **Scope boundary:** no continuous actuator fault, no system-identification target, and the original benchmark assumes a task/MDP grouping across which recurrent memory is retained.

**Official code.** No dedicated author repository was located. The paper is foundational evidence for recurrent meta-RL, not an off-the-shelf FaultAdapt implementation.

**Student questions.**
1. In a single long episode with a mid-episode fault, what signals let the recurrent policy distinguish a fault from stochastic noise?
2. Should recurrent state reset at episode boundaries, fault boundaries, neither, or both—and what information would each choice leak?
3. Is recurrent PPO in the proposed study genuinely meta-RL, or merely a POMDP policy trained under randomized faults?

---

## 3) Learning to Adapt in Dynamic, Real-World Environments Through Meta-Reinforcement Learning

**Citation.** Anusha Nagabandi, Ignasi Clavera, Simin Liu, Ronald S. Fearing, Pieter Abbeel, Sergey Levine, and Chelsea Finn. “Learning to Adapt in Dynamic, Real-World Environments Through Meta-Reinforcement Learning.” *ICLR*, 2019.  
Paper: https://arxiv.org/abs/1803.11347 · Official code: https://github.com/iclavera/learning_to_adapt

**Evidence — contribution.** Meta-learns a dynamics-model prior that adapts from recent transitions, then uses MPC. GrBAL adapts by gradient updates; ReBAL adapts through recurrence. Crucially, meta-training also performs the same online-adaptation procedure used at test time.

**Evidence — experiments/settings.** MuJoCo Half-Cheetah with a disabled joint, slopes, and floating “pier” blocks; Ant with a crippled leg. Tests include a joint/leg not disabled during training and faults switched on during a rollout. Models are 3×512 ReLU Gaussian dynamics networks; MPPI is used in simulation. Comparators: TRPO, MAML-RL, nonadaptive model-based RL, and model-based dynamic evaluation. Model-based meta-training used the equivalent of 1.5–3 hours of experience; model-free methods were trained much longer. A real legged millirobot was tested with a missing leg, terrain/slope changes, pose-estimation error, and payloads; random shooting was used there.

**Evidence — limitations/scope.** The authors explicitly report suboptimal asymptotic performance for model-based control on crippled Ant and identify this as a known model-based limitation. The official code is old (TensorFlow, MuJoCo 1.31), creating reproducibility friction. **Scope boundary:** disabled joints and crippled legs are abrupt/binary; continuous gradual actuator-efficiency ramps are not a reported controlled factor.

**Student questions.**
1. What makes the disabled-joint test a hidden-context POMDP rather than a fully observed MDP?
2. Which comparison is fair if MPC receives a known reward model while PPO policies do not receive fault parameters?
3. What metrics in Fig. 5 capture adaptation delay separately from post-adaptation return?

---

## 4) Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables (PEARL)

**Citation.** Kate Rakelly, Aurick Zhou, Deirdre Quillen, Chelsea Finn, and Sergey Levine. “Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables.” *ICML*, 2019.  
Paper: https://arxiv.org/abs/1903.08254 · Official code: https://github.com/katerakelly/oyster

**Evidence — contribution.** Separates probabilistic task inference from control: an encoder infers a posterior over latent context from transitions, while an off-policy actor-critic policy is conditioned on a sampled context. Posterior sampling supports temporally extended exploration and replay improves meta-training sample efficiency.

**Evidence — experiments/settings.** Six MuJoCo meta-RL families, horizon 200: Half-Cheetah forward/back, velocity, Ant forward/back and goal, Humanoid direction, and Walker-2D with randomized system parameters. Comparisons include ProMP, MAML-TRPO, and an RL² implementation using PPO; three seeds. Test performance is reported after aggregating two adaptation trajectories. The paper reports 20–100× meta-training sample efficiency and evaluates sparse 2-D navigation separately.

**Evidence — limitations/scope.** For sparse navigation, dense reward is assumed during meta-training. Its adaptation protocol is trajectory-level and benchmark tasks are sampled as task instances; it does not directly test a latent that changes continuously inside a trajectory. The official repository notes old MuJoCo dependencies and that it reproduces “most” continuous-control results. **Scope boundary:** no actuator-fault experiments.

**Student questions.**
1. Does PEARL’s unordered transition context lose information needed to infer gradual fault rates?
2. Would posterior uncertainty be calibrated under out-of-distribution fault magnitudes or fault types?
3. Why is reporting only return after two adaptation trajectories inadequate for sudden-fault recovery?

---

## 5) VariBAD: A Very Good Method for Bayes-Adaptive Deep RL via Meta-Learning

**Citation.** Luisa Zintgraf, Kyriacos Shiarlis, Maximilian Igl, Sebastian Schulze, Yarin Gal, Katja Hofmann, and Shimon Whiteson. “VariBAD: A Very Good Method for Bayes-Adaptive Deep RL via Meta-Learning.” *ICLR*, 2020.  
Paper: https://arxiv.org/abs/1910.08348 · Official code: https://github.com/lmzintgraf/varibad

**Evidence — contribution.** Uses a recurrent variational encoder/decoder to infer an approximate belief over the unknown task and trains a policy on that belief, approximating Bayes-adaptive behavior and explicitly valuing information gathered during an episode.

**Evidence — experiments/settings.** A 5×5 sparse-reward gridworld (15-step episodes, four episodes per Bayes-adaptive trial, latent dimension 5) and four MuJoCo tasks: Ant direction, Half-Cheetah direction/velocity, and Walker with randomized system parameters. Five seeds are used for MuJoCo test curves. VariBAD and RL² adapt within the first rollout in these experiments.

**Evidence — limitations/scope.** The authors explicitly state that their BAMDP formulation treats the hidden task as fixed per task; they contrast this with filtering a hidden state that changes each timestep. They also warn that out-of-distribution tasks can invalidate both inference and the policy’s interpretation of the posterior. **Scope boundary:** this formulation does not directly cover a time-varying actuator health latent.

**Student questions.**
1. Which mathematical assumption in VariBAD is violated by a gradual health ramp or a second sudden fault?
2. Could resetting or filtering the latent fix that violation without changing the training objective?
3. What evidence would show that a learned latent tracks health rather than merely predicts reward?

---

## 6) Complementary Meta-Reinforcement Learning for Fault-Adaptive Control

**Citation.** Ibrahim Ahmed, Marcos Quiñones-Grueiro, and Gautam Biswas. “Complementary Meta-Reinforcement Learning for Fault-Adaptive Control.” *Annual Conference of the PHM Society*, 2020. DOI: https://doi.org/10.36001/phmconf.2020.v12i1.1289  
Preprint: https://arxiv.org/abs/2009.12634 · PDF: https://arxiv.org/pdf/2009.12634

**Evidence — contribution.** Extends first-order MAML/PPO with a bounded “complement” of diverse policies learned under previous faults. Candidate policies are evaluated using a learned process model or importance weighting over buffered data; KL divergence is used to retain diverse policies. The selected/meta-updated initialization then continues online RL after a novel fault.

**Evidence — experiments/settings.** Simulated aircraft fuel-transfer system. Objective balances centre of gravity, fuel-distribution variance, and valve use. A nominal policy is trained for 50,000 steps; random abrupt faults include increased valve resistance and engine fuel-consumption faults. A three-policy complement is trained on faults in tanks 1, 3, and 5 without engine faults, then tested under random novel faults; empty-complement and standard continued-learning baselines are shown.

**Evidence — limitations/scope.** Authors state MAML sensitivity to architecture/task/hyperparameters and call for convergence/optimality analysis. Results are from one simulated process and figures emphasize episodic reward rather than a standardized physical recovery-time metric. **Scope boundary:** not a robotic actuator torque-loss benchmark; code was not directly linked from this paper in the sources inspected.

**Student questions.**
1. Does policy-library selection amount to fault classification, and what happens between represented modes?
2. How does complement size affect adaptation time and memory/compute cost?
3. Is importance weighting reliable immediately after a large fault when old-policy and new-condition distributions barely overlap?

---

## 7) Fault-Tolerant Control of Degrading Systems with On-Policy Reinforcement Learning

**Citation.** Ibrahim Ahmed, Marcos Quiñones-Grueiro, and Gautam Biswas. “Fault-Tolerant Control of Degrading Systems with On-Policy Reinforcement Learning.” *IFAC-PapersOnLine*, 2020. DOI: https://doi.org/10.1016/j.ifacol.2020.12.878  
Preprint: https://arxiv.org/abs/2008.04407 · Paper-linked code: https://git.isis.vanderbilt.edu/ahmedi/airplanefaulttolerance/-/tree/ifac2020

**Evidence — contribution.** Combines online on-policy control updates with periodic offline policy updates inside a data-driven model that is repeatedly re-fit as the system degrades. It does not require a preceding fault-detection/isolation decision.

**Evidence — experiments/settings.** Simulated six-tank C-130 fuel transfer. Ten online intervals of 512 steps; degradation is applied after each interval; each offline phase uses 2,048 model interactions. PPO is the on-policy method. The system model is a 2×64 ReLU network (reported cross-validated R² 0.996). Tests include linearly increasing degradation of one engine, combined engine/tank degradation, and 20 random trials with a valve and engine-pump degradation factor sampled from 10–30.

**Evidence — limitations/scope.** The authors explicitly leave abrupt faults, reward/model architecture choices, and convergence guarantees for future work. The method assumes sufficient cache memory, model re-fitting, and background offline interaction. **Scope boundary:** gradual changes occur only between 512-step intervals, not as a per-step continuous actuator-efficiency schedule; the process is not a robot simulator.

**Student questions.**
1. Is this method “online system identification,” “Dyna-style RL,” or both? Define the distinction from the paper.
2. How much adaptation benefit comes from extra simulated interactions rather than better identification?
3. What wall-clock and sample budgets would make comparison with recurrent PPO fair?

---

## 8) A Meta-Learning-Based Trajectory Tracking Framework for UAVs under Degraded Conditions

**Citation.** Esen Yel and Nicola Bezzo. “A Meta-Learning-Based Trajectory Tracking Framework for UAVs under Degraded Conditions.” *IEEE/RSJ IROS*, 2021.  
Paper: https://arxiv.org/abs/2104.15081 · PDF: https://arxiv.org/pdf/2104.15081

**Evidence — contribution.** Meta-learns a dynamics predictor with MAML, adapts it from a small runtime dataset, and uses predictions to modify the reference trajectory supplied to an unchanged low-level controller. A monitor triggers re-learning when prediction error exceeds a threshold; k-means retains a bounded, representative online dataset.

**Evidence — experiments/settings.** Simulation: 12-D quadrotor with nominal PID; training faults are 60%/80% commanded thrust on propellers 1 or 2; tests include 70% thrust on propeller 2 and 60% on propeller 4. A 2×40 neural predictor and K=20 initial samples are used. Average path deviation falls from 18.17 cm to 2.24 cm in one test and 27.05 cm to 2.61 cm in another. Hardware: AscTec Hummingbird with Vicon; roll-command biases train at five values and speeds 0.25/0.35/0.45 m/s; tests include unseen biases/speeds with K=50 samples. Reported examples reduce deviation from 55.78 to 8.09 cm and from 79.73 to 12.39 cm.

**Evidence — limitations/scope.** Runtime results depend on a baseline PID and reference-correction gains; Vicon supplies external state. Fault semantics differ between simulation (propeller thrust loss) and hardware (roll-command bias). The method adapts the planner/reference, not an RL policy. **Scope boundary:** no recurrent-policy baseline and no controlled gradual fault ramp.

**Student questions.**
1. Which parts of the improvement are due to MAML rather than the PID-style reference correction?
2. Is roll-command bias an adequate hardware proxy for actuator loss of effectiveness?
3. How should re-learning count and inference latency be reported alongside tracking error?

---

## 9) Fault-Tolerant Control of Skid Steering Vehicles Based on Meta-Reinforcement Learning with Situation Embedding

**Citation.** Huatong Dai, Pengzhan Chen, and Hui Yang. “Fault-Tolerant Control of Skid Steering Vehicles Based on Meta-Reinforcement Learning with Situation Embedding.” *Actuators* 11(3):72, 2022.  
Article/DOI: https://doi.org/10.3390/act11030072 · Full text: https://www.mdpi.com/2076-0825/11/3/72

**Evidence — contribution.** Trains multiple meta-DDPG initial models for different fault families plus a transition-based situation embedding model. At runtime, recent data select the most likely initialization, which is then gradient fine-tuned.

**Evidence — experiments/settings.** Four-wheel skid-steer simulation; actual torque is desired torque times loss-of-effectiveness ε∈[0,1]. Test faults: front-left ε=0.2; and simultaneous front-left/front-right ε=0.3. Straight and cornering scenarios; faults occur at 100 s in the straight case. Meta-DDPG actor 4×512×512×4, critic 8×512×512×1; embedding model 13×100×100×4. Runs use Python/TensorFlow 2 on an Intel Core i5. Compared with DDPG and single-initialization meta-DDPG. Situation embedding reaches comparable tracking with about 100 fine-tuning steps versus 200 for meta-DDPG; fine-tuning plots average five repeats.

**Evidence — limitations/scope.** The paper assumes fault information can be obtained through fault diagnosis/detection, while the embedding selects among meta-trained models from transition data—this interface needs careful interpretation. Validation is simulation-only; only two test fault cases and step-like persistent faults are reported. Data availability is “not applicable,” and no official code was located.

**Student questions.**
1. Exactly what fault information is assumed known online, and what remains hidden?
2. Does a 100-vs-200 gradient-step comparison translate to wall-clock adaptation latency?
3. Would nearest-mode model selection behave smoothly under gradual ε(t), or repeatedly switch modes?

---

## 10) RMA: Rapid Motor Adaptation for Legged Robots

**Citation.** Ashish Kumar, Zipeng Fu, Deepak Pathak, and Jitendra Malik. “RMA: Rapid Motor Adaptation for Legged Robots.” *Robotics: Science and Systems*, 2021.  
Paper: https://arxiv.org/abs/2107.04034 · Project: https://ashish-kmr.github.io/rma-legged-robots/

**Evidence — contribution.** Two-phase method: PPO trains a base policy conditioned on a privileged latent encoding of environment factors; supervised learning then trains a temporal adaptation module to predict that latent from recent proprioceptive state-action history. At deployment only proprioception/history is used.

**Evidence — experiments/settings.** Unitree A1; base policy 3×128 MLP, 30-D state + previous 12-D action + 8-D latent; adaptation network uses an MLP and 1-D CNN; adaptation at 10 Hz, base policy at 100 Hz. Training reports 1.2 billion simulator steps/24 GPU-hours plus 80 million steps/3 GPU-hours. Randomized factors include mass, centre of mass, friction, terrain height, and motor strength. During simulation testing, parameters are resampled inside an episode with probability 0.01 per step; 3 policy seeds × 1,000 episodes. RMA success is 73.5% versus 62.4% robust domain randomization and 56.5% direct SysID; real tests include payloads, slippery ground, deformable/rough terrain, and stairs.

**Evidence — limitations/scope.** The paper explicitly notes failures under large perturbations and the limitations of blind proprioception. Its direct SysID baseline performs poorly, but that is one estimator/design and is not evidence that explicit identification generally fails. The original training is GPU-heavy. **Code note:** the project page links https://github.com/antonilo/rl_locomotion, but that repository says it *builds on* RMA for a later cross-modal-supervision project; treat it as project-page-linked derivative code, not an exact original release.

**Student questions.**
1. Is RMA’s latent “system identification” if it is not required to equal physical parameters?
2. What does per-step random resampling test that fixed-per-episode domain randomization does not?
3. Is the published direct-SysID baseline comparable in network capacity, supervision, and temporal context?

---

## 11) Adaptive Control Strategy for Quadruped Robots in Actuator Degradation Scenarios (Adapt)

**Citation.** Xinyuan Wu, Wentao Dong, Hang Lai, Yong Yu, and Ying Wen. “Adaptive Control Strategy for Quadruped Robots in Actuator Degradation Scenarios.” *DAI ’23*, 2023.  
DOI/full text: https://doi.org/10.1145/3627676.3627686 · Official code: https://github.com/WentDong/Adapt

**Evidence — contribution.** Defines continuous per-joint degradation d∈[0,1] via applied torque = desired torque ×(1−d). Twelve fault-conditioned PPO teachers (one per joint) generate trajectories; a 1.2M-parameter transformer student behavior-clones state, degradation, and action sequences and uses history to adapt at deployment.

**Evidence — experiments/settings.** Unitree A1/Isaac Gym, 48-D proprioceptive state and 12-D joint-position action through PD control. Teacher data: 12×20,000 trajectories, each 500 transitions; transformer context 20, six blocks. Each teacher uses 4,096 parallel environments on an RTX 3080; student training reports 500 million updates/20 hours on an RTX 3080. Evaluation averages 1,024 parallel simulation runs per joint/degradation setting with random initial state, command, and fault time; baselines are a unified RL policy, MLP student, and teacher oracle. Real A1 tests attenuate commanded torque; the paper reports that unified/MLP baselines fail at severe degradation (≥0.9) while Adapt can transition gait. Multi-joint faults are also tested in simulation.

**Evidence — limitations/scope.** Authors explicitly limit the work to one quadruped platform and identify integrated fault detection as future work. Training uses privileged degradation labels in teacher policies and student trajectories, even though deployment is described as internal-sensor-only; the student must inspect the implementation to determine exactly which tokens are available at inference. Training requires Isaac Gym/NVIDIA hardware. **Scope boundary:** main tests emphasize sudden faults and severity sweeps; no systematic fixed/sudden/gradual protocol against feed-forward PPO, recurrent PPO, and explicit online ID.

**Student questions.**
1. Is degradation d supplied to the transformer at deployment, masked, predicted, or only present in training sequences? Verify from code, not prose alone.
2. Does Adapt’s advantage come from history/attention, privileged distillation, twelve specialist teachers, or all three?
3. Are real-world “faults” physical degradation or software torque attenuation, and what claims does that distinction permit?

---

# Three candidate gaps to investigate (not conclusions)

## Candidate gap A — Controlled adaptation comparison under identical hidden actuator-fault schedules

**Evidence motivating the question.** The papers compare different combinations of robust policies, recurrent/meta policies, latent inference, system ID, MPC, or specialist teachers, but use different simulators, task budgets, fault observability, and adaptation allowances. The direct-fault papers above do not report one common comparison of feed-forward PPO, recurrent PPO, and explicit online identification under fixed, sudden, and gradual actuator-efficiency schedules.

**What must be checked before calling it a gap.** Search benchmark and fault-tolerant RL papers citing Nagabandi, RMA, Adapt, and Dai; check recent Gymnasium/MuJoCo actuator-fault suites; document any study that controls architecture size, observations, training distribution, and interaction budget.

## Candidate gap B — Adaptation-transient metrics for time-varying faults

**Evidence motivating the question.** Many papers emphasize final return, tracking error integrated over a long run, or post-adaptation trajectories. Nagabandi tests mid-rollout failure; RMA resamples parameters in-episode; Yel reports re-learning counts; however, the set does not establish a shared measurement protocol for detection/recovery delay, return deficit after change, worst transient deviation, and steady-state recovery across sudden versus gradual changes.

**What must be checked before calling it a gap.** Look for nonstationary-RL evaluation standards and control/PHM metrics such as settling time, integrated absolute error, regret after changepoints, false adaptation under no fault, and survival/fall rate.

## Candidate gap C — CPU-reproducible fault adaptation with observability and supervision ablations

**Evidence motivating the question.** Several robot-scale methods use old licensed MuJoCo stacks or NVIDIA/Isaac Gym and very large simulation budgets. The literature also mixes privileged fault labels (UP-OSI targets, RMA environment factors, Adapt teacher data), inferred latents (PEARL/VariBAD), and raw recurrent memory (RL²), making supervision—not only architecture—a confound.

**What must be checked before calling it a gap.** Search lightweight classic-control and low-dimensional robotics studies; benchmark actual CPU wall-clock/sample cost; identify whether open implementations permit matched observation histories, labels, parameter counts, and rollout budgets.

---

# Cross-paper reading questions for the undergraduate

1. **Fault definition:** Is the fault a torque multiplier, locked joint, free joint, bias, delay, saturation, friction change, or structural damage? Which are comparable?
2. **Observability:** Is fault identity/severity directly observed, available only during training, inferred from transitions, or assumed available from a detector?
3. **Timescale:** Is the latent fixed per episode/task, switched once, resampled repeatedly, or drifting continuously? Does the method’s mathematical formulation allow that timescale?
4. **Adaptation action:** What actually changes online—RNN hidden state, latent context, model weights, policy weights, selected policy, reference trajectory, or MPC plan?
5. **Cost accounting:** How many real/environment samples, model-generated samples, gradient steps, and milliseconds are consumed after a fault?
6. **Fairness:** Do baselines share observations, history length, network capacity, training fault distribution, reward, simulator steps, and privileged labels?
7. **Metric:** Can the reported metric separate pre-fault nominal quality, transient loss, recovery delay, post-fault quality, and catastrophic failure?
8. **Generalization:** Are held-out tests new magnitudes of a known fault, new actuators, new fault types, new schedules, or combinations? These are not equivalent.
9. **Statistics:** How many seeds/trials are used, and are confidence intervals or raw runs available?
10. **Reproducibility:** Is code exact, derivative, or absent? Are simulator/version/hardware requirements practical for a CPU-first undergraduate study?
11. **Interpretability:** Does a latent estimate correspond to true actuator health, and is that correspondence required for good control?
12. **Claim discipline:** Which findings are simulation evidence, software-injected hardware evidence, or physical-damage evidence?

# Suggested reading order (workflow suggestion, not project direction)

1. Read **Nagabandi**, **RMA**, and **Adapt** first for direct hidden-dynamics/fault adaptation.
2. Read **UP-OSI** beside **RL²** to contrast explicit identification with recurrent implicit adaptation.
3. Read **Dai**, **Ahmed C-MRL**, **Ahmed degrading systems**, and **Yel & Bezzo** for fault-tolerant-control assumptions and metrics.
4. Use **PEARL** and **VariBAD** to interrogate latent-context and fixed-task assumptions rather than treating them as direct fault benchmarks.

# Source and code audit note

Primary full texts, not reviews, were used for the entries. Paper-linked code was verified for Nagabandi, PEARL, VariBAD, Ahmed’s IFAC study, and Adapt. The RMA project page’s linked repository explicitly describes itself as later code that builds on RMA. No exact author repository was located for UP-OSI, RL², C-MRL, Yel & Bezzo, or Dai during this scout; this means “not located,” not “does not exist.”
