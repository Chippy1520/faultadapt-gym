"""CPU-only smoke experiment for the initial FaultAdapt-Gym wrappers."""

from __future__ import annotations

import argparse
import json
from math import atan2

import gymnasium as gym
import numpy as np

from .wrappers import (
    ActionDelayWrapper,
    ActuatorFaultWrapper,
    FaultSchedule,
    ObservationFaultWrapper,
)


def pendulum_pd_action(observation: np.ndarray) -> np.ndarray:
    """Small deterministic controller used only to exercise the benchmark."""
    cos_theta, sin_theta, angular_velocity = observation
    theta = atan2(float(sin_theta), float(cos_theta))
    torque = -2.0 * theta - 0.5 * float(angular_velocity)
    return np.asarray([np.clip(torque, -2.0, 2.0)], dtype=np.float32)


def run_episode(seed: int) -> dict[str, float | int]:
    env = gym.make("Pendulum-v1")
    env = ActionDelayWrapper(env, delay_steps=2)
    env = ActuatorFaultWrapper(
        env,
        FaultSchedule(kind="sudden", nominal_scale=1.0, faulty_scale=0.5, onset_step=50),
    )
    env = ObservationFaultWrapper(env, noise_std=0.01)
    observation, _ = env.reset(seed=seed)
    total_reward = 0.0
    active_fault_steps = 0
    steps = 0
    while True:
        action = pendulum_pd_action(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += float(reward)
        active_fault_steps += int(bool(info["faultadapt/fault_active"]))
        steps += 1
        if terminated or truncated:
            break
    env.close()
    return {
        "seed": seed,
        "steps": steps,
        "active_fault_steps": active_fault_steps,
        "return": round(total_reward, 3),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=2)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    if args.episodes <= 0:
        raise SystemExit("--episodes must be positive")
    result = {
        "benchmark": "Pendulum-v1",
        "controller": "PD",
        "fault": "50% actuator authority after step 50",
        "delay_steps": 2,
        "episodes": [run_episode(args.seed + index) for index in range(args.episodes)],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
