from __future__ import annotations

import gymnasium as gym
import numpy as np
from gymnasium.spaces import Box

from faultadapt_gym import (
    ActionDelayWrapper,
    ActuatorFaultWrapper,
    FaultSchedule,
    ObservationFaultWrapper,
)


class RecordingEnv(gym.Env):
    action_space = Box(low=-2.0, high=2.0, shape=(1,), dtype=np.float32)
    observation_space = Box(low=-10.0, high=10.0, shape=(1,), dtype=np.float32)

    def __init__(self) -> None:
        self.last_action = np.zeros(1, dtype=np.float32)

    def reset(self, *, seed=None, options=None):  # type: ignore[no-untyped-def]
        super().reset(seed=seed)
        return np.zeros(1, dtype=np.float32), {}

    def step(self, action):  # type: ignore[no-untyped-def]
        self.last_action = np.asarray(action, dtype=np.float32)
        return np.zeros(1, dtype=np.float32), 0.0, False, False, {}


def test_sudden_and_linear_fault_schedules() -> None:
    sudden = FaultSchedule(kind="sudden", faulty_scale=0.4, onset_step=3)
    assert [sudden.scale(step) for step in range(5)] == [1.0, 1.0, 1.0, 0.4, 0.4]

    linear = FaultSchedule(kind="linear", faulty_scale=0.0, onset_step=2, transition_steps=4)
    np.testing.assert_allclose([linear.scale(step) for step in range(6)], [1, 1, 0.75, 0.5, 0.25, 0])


def test_actuator_fault_scales_action_and_logs_ground_truth() -> None:
    base = RecordingEnv()
    env = ActuatorFaultWrapper(base, FaultSchedule(kind="fixed", faulty_scale=0.25))
    env.reset(seed=1)
    _, _, _, _, info = env.step(np.asarray([2.0], dtype=np.float32))
    np.testing.assert_allclose(base.last_action, [0.5])
    assert info["faultadapt/actuator_scale"] == 0.25
    assert info["faultadapt/fault_active"]


def test_action_delay_executes_commands_in_order() -> None:
    base = RecordingEnv()
    env = ActionDelayWrapper(base, delay_steps=2)
    env.reset(seed=1)
    env.step(np.asarray([1.0], dtype=np.float32))
    np.testing.assert_allclose(base.last_action, [0.0])
    env.step(np.asarray([2.0], dtype=np.float32))
    np.testing.assert_allclose(base.last_action, [0.0])
    env.step(np.asarray([-1.0], dtype=np.float32))
    np.testing.assert_allclose(base.last_action, [1.0])


def test_observation_noise_is_seed_reproducible() -> None:
    env_a = ObservationFaultWrapper(RecordingEnv(), noise_std=0.2, bias=0.1)
    env_b = ObservationFaultWrapper(RecordingEnv(), noise_std=0.2, bias=0.1)
    obs_a, _ = env_a.reset(seed=42)
    obs_b, _ = env_b.reset(seed=42)
    np.testing.assert_allclose(obs_a, obs_b)
