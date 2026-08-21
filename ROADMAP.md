# FaultAdapt-Gym: 24-Week CPU-First Research Roadmap

## Objective

Build and evaluate a reproducible benchmark for adaptive control under hidden and time-varying robot faults. The primary scientific comparison is **implicit adaptation through policy memory versus explicit online system identification**.

## Hypotheses

- **H1:** History-conditioned policies outperform feed-forward policies when hidden dynamics can be inferred from recent state-action transitions.
- **H2:** Training with episode-level randomization is insufficient for abrupt faults introduced mid-episode.
- **H3:** Explicit identification is more interpretable and may generalize better to fault severities outside training.
- **H4:** Long memory can hurt after abrupt changes because stale context delays adaptation.

## Scope

### Primary environments

1. Pendulum-v1 for infrastructure and debugging.
2. MuJoCo Reacher for the primary robotic experiment.
3. At most one optional environment after the Reacher study is complete.

### Fault families

- actuator authority loss: fixed, sudden, and gradual;
- action latency and jitter;
- observation noise and encoder bias;
- payload/mass and friction mismatch;
- optional stuck or asymmetric actuator faults where the environment supports them.

### Baselines

1. Classical controller.
2. Feed-forward PPO.
3. Recurrent PPO.
4. Explicit online system identification plus controller/policy.
5. Optional GPU-only transformer/AMAGO extension after the core study.

### Metrics

Task success/return, tracking error, recovery time, adaptation time, worst-case performance, control effort, safety violations, inference latency, training time, and—for explicit identification—parameter-estimation error and convergence time.

## CPU rules

- Use low-dimensional observations, small MLP/GRU networks, and vectorized CPU environments.
- Debug with one or two seeds; reserve five-seed runs for frozen final protocols.
- Cache raw results and never rerun completed configurations without a documented reason.
- Do not add image observations, VLAs, RoboCasa, or humanoid-scale simulation to the critical path.

## Stage gates

### Week 4

Proceed only if one complete seeded pilot runs within the available compute budget and the proposal specifies variables, baselines, metrics, and exclusions.

### Week 8

Release v0.1 only if another user can install the package, run tests, and reproduce a baseline fault sweep.

### Week 12

Keep only experiments that answer the four hypotheses. Remove extra fault types or environments before adding compute.

### Week 18

A clean environment must reproduce at least one headline comparison from committed configuration and result files.

## Optional later extensions

When GPU access arrives, add one controlled transformer-memory or AMAGO-style comparison. If safe hardware access arrives, validate only one fault/latency condition using motor telemetry or hardware-in-the-loop. Neither extension is required for the core report.

## Publication standard

The target is a rigorous 6–8 page report and reproducible benchmark release. A workshop, undergraduate symposium, or reproducibility submission is attempted only if mentor review supports the novelty and evidence. Negative results—such as memory slowing recovery—are valid when the protocol is sound.
