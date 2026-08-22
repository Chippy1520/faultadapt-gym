> Bot-produced scouting packet. It is evidence support, not a student-verified literature review or novelty decision.

## Outcome

### Recommended minimal CPU-first stack

Use one maintained ecosystem for the core comparisons:

- **Python 3.12**
- **Gymnasium 1.3.0**
- **MuJoCo via `gymnasium[mujoco]`**
- **PyTorch CPU**
- **Stable-Baselines3 2.9.0**
- **SB3-Contrib 2.9.0**
- NumPy implementation of a small online estimator; optionally use [River](https://riverml.xyz/) if a packaged streaming regressor is preferred.

A real `pip --dry-run` on this Windows/Python 3.12 host successfully resolved:

```text
stable-baselines3==2.9.0
sb3-contrib==2.9.0
gymnasium[mujoco]==1.3.0
torch==2.13.0
mujoco==3.12.0
```

Python 3.12 Windows wheels were available for PyTorch and MuJoCo. SB3 2.9 explicitly accepts `gymnasium>=0.29.1,<2.0`, so Gymnasium 1.3 is compatible.

## Method comparison

| Baseline | Practical implementation | Fault adaptation mechanism | Risk | CPU feasibility |
|---|---|---|---|---|
| **Feed-forward PPO** | [SB3 PPO `MlpPolicy`](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html) | None intrinsically; train under fault/domain randomization | **Low** | **Excellent** |
| **Recurrent PPO** | [SB3-Contrib `RecurrentPPO`](https://sb3-contrib.readthedocs.io/en/master/modules/ppo_recurrent.html) | LSTM hidden state infers fault from transition history | **Low–medium** | **Good** |
| **GRU-PPO specifically** | Custom recurrent SB3 policy/buffer, or larger framework | GRU hidden state | **High** relative to dissertation value | **Good at runtime**, expensive to implement/debug |
| **Online system identification + PPO** | Small NumPy RLS/EWMA estimator in a Gymnasium observation wrapper; optional [River online regression](https://riverml.xyz/latest/api/linear-model/LinearRegression/) | Explicitly estimates changed action effectiveness/dynamics and appends estimate/confidence to observation | **Medium** | **Excellent** |
| **Finite-memory PPO** | SB3 `VecFrameStack`, e.g. 4 frames | Fixed recent history lets MLP detect changed response | **Low** | **Excellent** |
| **Full meta-RL/PEARL** | Historically available in [garage](https://github.com/rlworkgroup/garage) | Learned latent task/fault context | **Very high** | Training may fit CPU, but engineering/sample cost is poor |

### Important recurrent finding

SB3-Contrib provides **LSTM**, not GRU. It supports continuous `Box` observations/actions, multiprocessing, and the same PPO behavior as core SB3. Correct evaluation must carry both `lstm_states` and `episode_start` so state is reset at episode boundaries.

For an undergraduate CPU-first project, treat **LSTM-PPO as the practical recurrent/GRU-class baseline**. Implement a literal GRU only if architectural parity is an explicit research requirement. Changing only LSTM to GRU is not scientifically important enough to justify custom recurrent rollout code unless approved.

### Online system-identification design

A practical first version should be deliberately small:

1. Keep a short transition history containing `(observation, commanded_action, next_observation)`.
2. Estimate either:
   - one gain per actuator, or
   - a small local linear transition model,
   using recursive least squares or exponentially weighted regression.
3. Append the estimate, confidence/sample count, and optionally prediction-error EWMA to the policy observation.
4. Reset estimator state on episode reset and maintain one independent estimator per vectorized environment.
5. Never provide the simulator’s true fault parameter to this baseline during evaluation.

For Reacher, a per-joint actuator-effectiveness estimate is more interpretable than a generic high-dimensional neural predictor. Because target position and uncontrolled state evolution also affect transitions, identifying gains from raw observation differences will require careful feature selection or a nominal healthy transition model.

[River](https://github.com/online-ml/river) is maintained, supports Python 3.12, and provides `learn_one`, streaming linear regression, and online/rolling scaling. Nevertheless, a compact NumPy RLS implementation is likely easier to checkpoint, explain, and keep synchronized across vector environments.

## Minimal experiment ladder

Recommended default—not a final decision:

1. **PPO-MLP, current observation**
   - Establish healthy and faulted performance.
   - Same network and training budget for all comparisons.
2. **PPO-MLP with 4-frame stack**
   - Cheap finite-memory control.
   - SB3 itself recommends starting with frame stacking because it is simpler, faster, and often competitive with recurrent PPO.
3. **RecurrentPPO with one small LSTM**
   - Suggested initial hidden size: 64 or 128, one layer.
4. **PPO-MLP with online fault/system-ID context**
   - Reuse the feed-forward PPO configuration; only observation wrapper changes.
5. Run a full meta-RL baseline only if time remains and the research question demands it.

This gives a clean comparison among no memory, fixed memory, learned memory, and explicit adaptation without maintaining multiple RL frameworks.

## Environment and CPU notes

- [SB3 custom-environment guide](https://stable-baselines3.readthedocs.io/en/master/guide/custom_env.html): FaultAdapt-Gym should use the Gymnasium API:
  - `reset(...) -> (observation, info)`
  - `step(...) -> (observation, reward, terminated, truncated, info)`
  - Validate using `stable_baselines3.common.env_checker.check_env`.
- [Reacher-v5](https://gymnasium.farama.org/environments/mujoco/reacher/) is a small continuous task:
  - Action: `Box(-1, 1, (2,), float32)`
  - Observation: 10-dimensional `float64`
  - Default episode: 50 steps
  - This is very reasonable on 12 logical CPU threads and 15.6 GB RAM.
- Start with **1–4 `DummyVecEnv` environments**. Benchmark **4 or 8 `SubprocVecEnv`** instances later; short MuJoCo episodes and Windows process communication may make subprocesses slower.
- Windows `SubprocVecEnv` requires:

  ```python
  if __name__ == "__main__":
      ...
  ```

  See [SB3 vectorized environments](https://stable-baselines3.readthedocs.io/en/master/guide/vec_envs.html).

- PPO MLP is explicitly described by SB3 as primarily a CPU algorithm. Small MLP/LSTM policies should remain well within RAM.
- Avoid running rendering during training.
- Use separate healthy, seen-fault, and unseen-fault evaluation environments and several seeds.

## Library assessment

- **Stable-Baselines3 / SB3-Contrib:** best fit; active repositories and June 2026 releases; direct Gymnasium support.
- **CleanRL:** useful readable reference—its repository includes a Gymnasium continuous-action PPO script—but its PyPI package is stale (`Python <3.11`, old pinned dependencies), and its included LSTM PPO targets discrete Atari rather than continuous control. Do not use the PyPI package as the project foundation.
- **Ray RLlib:** actively maintained and Python 3.12 wheels exist, but installation/runtime architecture and recurrent customization are excessive for a single-machine undergraduate baseline suite.
- **garage/PEARL:** not recommended. Latest PyPI release is from 2021, repository code was last pushed in 2023, and its MuJoCo setup uses old `mujoco-py` constraints rather than current Gymnasium MuJoCo.
- **River:** maintained and suitable for streaming regression/scaling, but optional rather than necessary.

## Decisions requiring student/main-planner approval

1. Whether **SB3 LSTM** is acceptable as the recurrent/“GRU-class” baseline, or a literal GRU is mandatory.
2. Whether the optional memory baseline is **4-frame stacking** or a much riskier true meta-RL method.
3. Which fault families are in scope: actuator gain/loss, bias, delay, sensor faults, or physical-parameter changes.
4. Whether faults occur only at reset or can appear mid-episode.
5. Whether the system-ID estimator is:
   - reset every episode,
   - warm-started from healthy data, or
   - persistent across episodes.
6. Whether system ID may use simulator state during development. For fair final evaluation, it should use only policy-available observations/actions.
7. Exact frame-stack depth, LSTM size, training budget, number of seeds, and CPU runtime ceiling.
8. Whether all methods receive identical domain-randomized training distributions.
9. Whether a true meta-RL baseline is sufficiently central to justify its implementation risk.

## Files and issues

- **Files created/modified:** none.
- **Issue encountered:** the general web-search backend rate-limited. I used official documentation, PyPI metadata, GitHub repository metadata/raw sources, and a real pip dependency-resolution check instead.
