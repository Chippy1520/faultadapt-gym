# Research Log

Use one entry per meaningful experiment or design decision.

## Entry template

### YYYY-MM-DD — Short title

- **Question / hypothesis:**
- **Configuration and commit:**
- **Independent variables:**
- **Dependent variables / metrics:**
- **Seeds and evaluation episodes:**
- **Result:**
- **Interpretation:**
- **Limitations / possible confounds:**
- **Next action:**
- **Artifact links:**

## 2026-08-21 — CPU-first scope and executable fault-injection pilot

- **Question / hypothesis:** Can the benchmark represent hidden, time-varying actuator faults and timing disturbances reproducibly without GPU or robot access?
- **Configuration and commit:** Pendulum-v1, deterministic PD controller, sudden actuator scale from 1.0 to 0.5 at step 50, two-step action delay, observation noise standard deviation 0.01.
- **Independent variables:** Episode seed (7 and 8 in the smoke run); the fault profile is fixed for this infrastructure check.
- **Dependent variables / metrics:** Episode length, active-fault steps, and return.
- **Seeds and evaluation episodes:** Two 200-step episodes, seeds 7 and 8.
- **Result:** Both episodes completed; each logged 150 active-fault steps. Returns were -1402.596 and -1492.690.
- **Interpretation:** The initial wrappers compose and preserve hidden fault ground truth in `info`; this is an infrastructure result, not evidence for any research hypothesis.
- **Limitations / possible confounds:** No learned policy, no recovery metric, one environment, and no nominal comparison.
- **Next action:** Add a reproducible nominal-versus-fault sweep and define the Week 1 compute inventory and scope document.
- **Artifact links:** `src/faultadapt_gym/wrappers.py`, `src/faultadapt_gym/smoke.py`, and `tests/`.
