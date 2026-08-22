# FaultAdapt-Gym

**CPU-first research benchmark for adaptive robot control under hidden and time-varying faults.**

This undergraduate research project asks whether history-conditioned policies can infer changes in actuator health and dynamics from recent interaction and adapt more effectively than feed-forward RL and explicit online system identification.

## Research question

> Can lightweight recurrent policies adapt to hidden actuator degradation, latency, bias, payload, and friction changes—and when does memory make adaptation worse?

## Core comparisons

1. Classical controller appropriate to the environment.
2. Feed-forward PPO.
3. Recurrent PPO with GRU/LSTM memory.
4. Explicit online system identification plus controller/policy.
5. Optional later GPU extension: compact transformer or AMAGO-style memory.

## Current executable artifact

The first release includes composable Gymnasium wrappers for:

- fixed, sudden, and gradual actuator-authority loss;
- action delay;
- observation noise and bias;
- hidden fault ground truth retained in `info` for evaluation.

A CPU-only Pendulum smoke experiment exercises a PD controller under a 50% actuator fault, observation noise, and two-step action delay.

## Install and run

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e '.[dev]'
.venv/Scripts/python -m pytest
.venv/Scripts/python -m faultadapt_gym.smoke --episodes 2
```

Install the later RL dependency only when baseline work begins:

```bash
.venv/Scripts/python -m pip install -e '.[rl]'
```

## Evaluation principles

- State/proprioceptive observations first; no pixel-based training on the critical path.
- At least five seeds for final claims; one or two while debugging.
- Held-out fault levels and abrupt mid-episode changes.
- Recovery time, worst-case performance, safety violations, control effort, and adaptation time—not reward alone.
- Identical evaluation episodes and logged compute budgets.
- Hardware and GPU experiments are optional extensions after the CPU benchmark is complete.

## Project management

- [GitHub Project board](https://github.com/users/Chippy1520/projects/3)
- `COLLABORATION.md` — human-in-the-loop agent roles, decision ownership, and handoff protocol
- `ROADMAP.md` — research design and stage gates
- `planning/board-import.csv` — source of truth for the 24 weekly issues
- `planning/setup_board.py` — idempotent GitHub board synchronization
- `research-log.md` — hypothesis and experiment log

## Status

Week 1: scope, reproducible environment, compute audit, and pilot fault wrapper.
