"""Verify that the dedicated CPU research environment is operational."""

from __future__ import annotations

import json
import platform

import control
import gymnasium as gym
import jupyterlab
import matplotlib
import mujoco
import numpy as np
import pandas as pd
import scipy
import stable_baselines3
import torch
from sb3_contrib import RecurrentPPO
from stable_baselines3 import PPO


def main() -> None:
    env = gym.make("Reacher-v5")
    observation, _ = env.reset(seed=7)
    action = env.action_space.sample()
    next_observation, reward, terminated, truncated, _ = env.step(action)
    env.close()

    training_env = gym.make("Pendulum-v1")
    model = PPO(
        "MlpPolicy",
        training_env,
        n_steps=32,
        batch_size=32,
        n_epochs=1,
        learning_rate=3e-4,
        seed=7,
        device="cpu",
        verbose=0,
    )
    model.learn(total_timesteps=32)
    training_env.close()

    system = control.ss([[0.0, 1.0], [-1.0, -0.2]], [[0.0], [1.0]], [[1.0, 0.0]], 0.0)
    result = {
        "python": platform.python_version(),
        "packages": {
            "control": control.__version__,
            "gymnasium": gym.__version__,
            "jupyterlab": jupyterlab.__version__,
            "matplotlib": matplotlib.__version__,
            "mujoco": mujoco.__version__,
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scipy": scipy.__version__,
            "stable_baselines3": stable_baselines3.__version__,
            "torch": torch.__version__,
        },
        "torch_cuda_available": torch.cuda.is_available(),
        "recurrent_ppo_import": RecurrentPPO.__name__,
        "reacher": {
            "observation_shape": list(observation.shape),
            "next_observation_shape": list(next_observation.shape),
            "reward_is_finite": bool(np.isfinite(reward)),
            "terminated": bool(terminated),
            "truncated": bool(truncated),
        },
        "control_state_dimension": int(system.nstates),
        "ppo_cpu_smoke_timesteps": 32,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
