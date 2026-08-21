# Robust Sim-to-Real Control Under Faults, Noise, and Latency

A 24-week research project studying whether curriculum-based domain randomization produces robot controllers that degrade more gracefully than nominal reinforcement-learning and classical-control baselines under actuator faults, observation noise, latency, and model mismatch.

## Research question

> Can curriculum-based domain randomization improve graceful degradation under held-out robot faults and disturbances?

## Planned comparisons

- Classical/reference controller
- PPO
- SAC
- PPO or SAC with curriculum domain randomization

## Evaluation

- At least five random seeds
- Held-out fault levels and identical evaluation episodes
- Success rate, return, tracking error, time, energy/control effort, worst-case performance, and recovery after fault onset
- Confidence intervals, ablations, failure taxonomy, and logged compute budgets

## Project board

The GitHub Project board contains one issue for each week, including technical work, an exit criterion, a relationship/public action, phase, and calendar dates.

## Repository map

- `ROADMAP.md` — complete 24-week strategy
- `research-log.md` — running hypothesis/experiment/interpretation log
- `planning/board-import.csv` — portable backup of the board tasks
- `docs/` — reports, figures, and project-page material
- `src/` — implementation
- `tests/` — tests

## Current status

Planning and environment setup.

## Scope rule

Finish the reproducible Bronze simulation study before attempting hardware-in-the-loop or real-system extensions.
