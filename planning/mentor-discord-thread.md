# Mentor Discussion: 24-Week Robotics/RL Research Plan

Hi! I am Chathuka Elapatha, a third-year Electronic and Telecommunication Engineering undergraduate at the University of Moratuwa. My longer-term goal is graduate study and research/engineering work in robotics, reinforcement learning, and embodied AI.

I would appreciate feedback on the following 24-week plan. It is deliberately CPU-first and simulation-heavy because I currently have limited GPU and robot access. The intended outcome is one rigorous, reproducible research artifact—not several shallow projects.

**Repository:** https://github.com/Chippy1520/faultadapt-gym  
**Project board:** https://github.com/users/Chippy1520/projects/3

## Working research direction

**FaultAdapt-Gym:** a Gymnasium-compatible platform for studying when a robot should adapt after observing evidence of a physical change.

**Working question:**

> When should a robot adapt to an observed physical change, and when would adaptation cause more harm than continuing, retrying, or waiting for more evidence?

Examples include sudden or gradual actuator-authority loss, temporary or persistent action latency, payload/friction changes, and transient disturbances that should not trigger adaptation.

The proposed contribution is not merely another collection of fault wrappers. Existing work such as Robust Gymnasium, DynaMITE-RL, UP-OSI, Nagabandi et al., and RMA already covers important parts of robustness and adaptation. The intended focus is a controlled evaluation of **adaptation decisions** under transient versus persistent change.

Candidate decision rules:

1. never adapt;
2. always adapt after an anomaly;
3. fixed uncertainty-threshold gating;
4. evidence-accumulation or expected-adaptation-value gating;
5. oracle gating using true persistence/change information, used only as a diagnostic ceiling.

Feed-forward PPO, recurrent PPO, and explicit online system identification are candidate mechanisms/estimators and baselines—not assumed novel contributions.

## Feasibility constraints

- Approximately **8–12 focused hours per week**, adjustable around university workload.
- CPU-first, low-dimensional state observations, small models, and vectorized environments.
- Pendulum for debugging and observability studies; MuJoCo Reacher as the primary robot-control environment.
- One or two seeds during development; five seeds only after the protocol is frozen.
- GPU, vision, transformer/VLA, and real-hardware experiments are optional later extensions, not critical-path requirements.
- Publication is a target, not a promise; the minimum success criterion is a rigorous report and reproducible release.

## 24-week plan

### Phase 1 — Foundations and proposal: Weeks 1–4

**Week 1 — Scope and compute audit**
- Confirm the primary question, exclusions, available compute, and weekly time budget.
- Run the existing fault-wrapper smoke experiment.
- Produce a one-page scope and risk statement.
- Ask a UoM controls/robotics/ML mentor for one bounded critique.

**Week 2 — Reproduce foundations**
- Review MDPs, PPO, partial observability, recurrent policies, and online system identification.
- Reproduce a deterministic Pendulum control/RL baseline.
- Save the environment lock, seed, configuration, and first plot.

**Week 3 — Literature and duplication matrix**
- Read 6–8 anchor papers, starting with Robust Gymnasium, Nagabandi et al., UP-OSI, DynaMITE-RL, and RMA.
- Record each paper's hidden variable, adaptation method, protocol, metrics, limitations, and overlap.
- Discuss the possible gap with a postgraduate student or faculty member.

**Week 4 — Proposal and pilot gate**
- Write a two-page proposal specifying hypotheses, variables, baselines, metrics, compute cap, risks, and exclusions.
- Run one seeded sudden-fault/transient-disturbance pilot.
- Mentor go/no-go decision: proceed, narrow, or reformulate.

**Stage gate:** proceed only if one complete pilot fits the compute budget and the question is distinguishable from existing benchmarks.

### Phase 2 — Reproducible infrastructure: Weeks 5–8

**Week 5 — Fault models and deterministic harness**
- Test fixed, sudden, and gradual actuator loss; action delay; noise; and bias.
- Add deterministic rollout and evaluation tests.
- Separate hidden ground truth used for evaluation from policy observations.

**Week 6 — Classical baseline and provenance**
- Implement the environment-appropriate classical controller.
- Log configuration, seed, commit, runtime, hardware, raw results, and fault schedule.
- Evaluate nominal behavior and an initial fault sweep.

**Week 7 — Feed-forward PPO baseline**
- Train a small PPO baseline under a declared tuning and compute budget.
- Compare nominal, persistent-change, and transient-disturbance behavior.
- Ask an RL practitioner to critique evaluation fairness rather than tune the model for me.

**Week 8 — FaultAdapt-Gym v0.1**
- Clean installation, documented API, result schema, plotting, tests, and one reproducible fault sweep.
- Ask another person to reproduce the baseline from the README.
- Publish a short technical progress update with one precise question.

**Stage gate:** release v0.1 only if another user can install it and reproduce one baseline plot.

### Phase 3 — Adaptation and decision mechanisms: Weeks 9–12

**Week 9 — History-based estimator/adaptation mechanism**
- Add a small recurrent model or RecurrentPPO that uses recent interaction history without receiving true fault labels.
- Verify that hidden fault state does not leak into observations.

**Week 10 — Explicit online identification baseline**
- Estimate actuator scale or selected dynamics parameters from transitions.
- Log estimator error, confidence, convergence time, and task performance.
- Ask a controls mentor to critique identifiability assumptions.

**Week 11 — Adaptation-decision baselines**
- Implement never-adapt, always-adapt, threshold, evidence-accumulation, and oracle gates around a controlled adaptation mechanism.
- Compare transient/sham events against persistent physical changes.
- Measure false adaptation, delay, immediate damage, recovery, and retained nominal competence.

**Week 12 — Midpoint replication and scope cut**
- Reproduce one result from a clean run.
- Remove weak environments, fault families, or mechanisms.
- Produce a three-page midpoint report, limitations list, and revised compute forecast.

**Stage gate:** retain only experiments that genuinely distinguish adaptation decisions; cut scope before adding compute.

### Phase 4 — Frozen final experiments: Weeks 13–18

**Week 13 — Freeze protocol**
- Pre-specify hypotheses, metrics, held-out severities, onset distributions, seed count, exclusions, and stopping rules.
- Commit the protocol before final experiments.

**Week 14 — Final batch A**
- Run final nominal and in-distribution comparisons with automatic provenance.
- Use identical episodes and matched budgets where possible.

**Week 15 — Held-out generalization**
- Evaluate unseen fault severities, onset times, persistence, temporal profiles, and selected dynamics changes.
- Report confidence intervals and all planned seeds.

**Week 16 — Failure-mode analysis**
- Analyze false adaptation, delayed adaptation, stale memory, wrong-cause updates, and catastrophic post-adaptation behavior.
- Build a quantified failure taxonomy with representative rollouts.
- Share an honest mixed or negative result publicly.

**Week 17 — At most one justified extension**
- Choose one only if the core study is complete: second environment, learned adaptation-value estimator, or safe hardware/HIL validation.
- Otherwise use the week to strengthen analysis and documentation.

**Week 18 — Independent clean reproduction**
- Reinstall from scratch and reproduce at least one headline comparison from committed configs.
- Confirm results match the expected tolerance.

**Stage gate:** no paper claim proceeds unless a clean environment reproduces a headline result.

### Phase 5 — Report, review, and release: Weeks 19–22

**Week 19 — Paper structure and methods**
- Draft the abstract, introduction, related work, setup, methods, and protocol.
- Create placeholders for every planned figure/table and map claims to evidence.

**Week 20 — Results, discussion, and limitations**
- Complete results, statistical reporting, failure cases, safety discussion, compute statement, and reproducibility checklist.
- Produce draft v1 with no invented or placeholder results.

**Week 21 — External review and necessary reruns**
- Obtain one controls review and one RL/ML review.
- Maintain a response-to-feedback log.
- Rerun only experiments required to resolve a documented concern.

**Week 22 — FaultAdapt-Gym v1.0**
- Release code, configs, allowed data, tests, report, citation file, project page, and a 3–5 minute demo.
- Produce a rigorous 6–8 page report.
- Attempt a workshop, undergraduate symposium, or reproducibility submission only if mentor review supports the evidence and novelty.

### Phase 6 — Portfolio and research network: Weeks 23–24

**Week 23 — Application and outreach package**
- Prepare an academic CV, industry résumé, research-statement paragraph, project one-pager, and contact tracker.
- Contact only 2–3 relevant researchers/engineers with distinct, evidence-based reasons and a concrete artifact or technical question.

**Week 24 — Portfolio integration and next six months**
- Add the project to the portfolio with a concise problem/method/result/demo presentation.
- Give a mock research talk and conduct a retrospective.
- Choose the next controlled extension: stronger simulation, GPU-based memory method, or hardware/HIL validation.
- Thank contributors and update people whose feedback materially changed the project.

## Expected outputs after 24 weeks

1. Reproducible open-source FaultAdapt-Gym v1.0.
2. Tested fault/change wrappers and deterministic evaluation harness.
3. Classical, feed-forward, history-based, explicit-identification, and adaptation-decision baselines within the final approved scope.
4. Frozen evaluation protocol and provenance-tracked results.
5. A 6–8 page research report with limitations and negative results included.
6. A 3–5 minute technical demo and portfolio case study.
7. A mentor-reviewed decision on whether/where to submit.
8. A small network built through technical discussions and feedback—not generic cold messages.
9. Academic CV, industry résumé, project one-pager, and research-talk material.

## Mentor feedback requested

I would especially value feedback on these questions:

1. Is the adaptation-decision question scientifically meaningful and sufficiently distinct from robust/adaptive RL benchmarks?
2. Should I begin with Pendulum and Reacher, or use a different primary control environment?
3. Which adaptation operator should be held fixed when comparing decision gates?
4. Are the proposed baselines and metrics fair and sufficient?
5. Which fault/change families should be removed to keep the project publishable within 24 weeks?
6. What would constitute a credible minimum contribution for an undergraduate workshop/symposium report?
7. Could we have short reviews around Weeks 4, 12, 17, and 21 rather than requiring frequent supervision?

## Definition of success

The project succeeds even without a publication if it produces a technically defensible question, reproducible experiments, honest findings, strong documentation, and evidence that I can conduct and communicate research. Publication and hardware/GPU extensions are stretch outcomes that should follow evidence rather than drive premature scope expansion.
