"""Composable Gymnasium wrappers for hidden robot faults and timing disturbances."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Literal

import gymnasium as gym
import numpy as np
from gymnasium.spaces import Box

ScheduleKind = Literal["fixed", "sudden", "linear"]


@dataclass(frozen=True)
class FaultSchedule:
    """Defines how actuator authority changes during an episode.

    The scale is deliberately absent from observations. It is added to ``info``
    for evaluation and can therefore be hidden from the policy while retained
    as ground truth for adaptation analysis.
    """

    kind: ScheduleKind = "sudden"
    nominal_scale: float = 1.0
    faulty_scale: float = 0.5
    onset_step: int = 100
    transition_steps: int = 50

    def __post_init__(self) -> None:
        if self.kind not in {"fixed", "sudden", "linear"}:
            raise ValueError(f"Unsupported schedule kind: {self.kind}")
        if self.nominal_scale < 0 or self.faulty_scale < 0:
            raise ValueError("Actuator scales must be non-negative")
        if self.onset_step < 0:
            raise ValueError("onset_step must be non-negative")
        if self.transition_steps <= 0:
            raise ValueError("transition_steps must be positive")

    def scale(self, step: int) -> float:
        """Return the actuator scale at a zero-based environment step."""
        if step < 0:
            raise ValueError("step must be non-negative")
        if self.kind == "fixed":
            return self.faulty_scale
        if step < self.onset_step:
            return self.nominal_scale
        if self.kind == "sudden":
            return self.faulty_scale
        progress = min(1.0, (step - self.onset_step + 1) / self.transition_steps)
        return self.nominal_scale + progress * (self.faulty_scale - self.nominal_scale)


class ActuatorFaultWrapper(gym.Wrapper):
    """Scale selected continuous action dimensions according to a fault schedule."""

    def __init__(
        self,
        env: gym.Env,
        schedule: FaultSchedule,
        affected_dimensions: tuple[int, ...] | None = None,
    ) -> None:
        super().__init__(env)
        if not isinstance(env.action_space, Box):
            raise TypeError("ActuatorFaultWrapper requires a continuous Box action space")
        self.schedule = schedule
        self.affected_dimensions = affected_dimensions
        self.elapsed_steps = 0
        flat_size = int(np.prod(env.action_space.shape))
        if affected_dimensions is not None and any(
            index < 0 or index >= flat_size for index in affected_dimensions
        ):
            raise ValueError("affected_dimensions contains an invalid action index")

    def reset(self, **kwargs):  # type: ignore[no-untyped-def]
        self.elapsed_steps = 0
        return self.env.reset(**kwargs)

    def step(self, action):  # type: ignore[no-untyped-def]
        original = np.asarray(action, dtype=self.action_space.dtype)
        applied = original.copy().reshape(-1)
        scale = self.schedule.scale(self.elapsed_steps)
        indices = self.affected_dimensions or tuple(range(applied.size))
        applied[list(indices)] *= scale
        applied = applied.reshape(original.shape)
        applied = np.clip(applied, self.action_space.low, self.action_space.high)
        observation, reward, terminated, truncated, info = self.env.step(applied)
        info = dict(info)
        info["faultadapt/actuator_scale"] = scale
        info["faultadapt/fault_active"] = not np.isclose(scale, self.schedule.nominal_scale)
        info["faultadapt/commanded_action"] = original.copy()
        info["faultadapt/applied_action"] = applied.copy()
        self.elapsed_steps += 1
        return observation, reward, terminated, truncated, info


class ActionDelayWrapper(gym.Wrapper):
    """Apply actions after a fixed number of environment steps."""

    def __init__(self, env: gym.Env, delay_steps: int = 1) -> None:
        super().__init__(env)
        if not isinstance(env.action_space, Box):
            raise TypeError("ActionDelayWrapper requires a continuous Box action space")
        if delay_steps < 0:
            raise ValueError("delay_steps must be non-negative")
        self.delay_steps = delay_steps
        self._queue: deque[np.ndarray] = deque()

    def reset(self, **kwargs):  # type: ignore[no-untyped-def]
        zero = np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
        self._queue = deque(zero.copy() for _ in range(self.delay_steps))
        return self.env.reset(**kwargs)

    def step(self, action):  # type: ignore[no-untyped-def]
        commanded = np.asarray(action, dtype=self.action_space.dtype)
        if self.delay_steps == 0:
            applied = commanded
        else:
            applied = self._queue.popleft()
            self._queue.append(commanded.copy())
        observation, reward, terminated, truncated, info = self.env.step(applied)
        info = dict(info)
        info["faultadapt/action_delay_steps"] = self.delay_steps
        info["faultadapt/delayed_action"] = applied.copy()
        return observation, reward, terminated, truncated, info


class ObservationFaultWrapper(gym.ObservationWrapper):
    """Add fixed bias and seeded Gaussian noise to Box observations."""

    def __init__(
        self,
        env: gym.Env,
        noise_std: float = 0.0,
        bias: float | np.ndarray = 0.0,
    ) -> None:
        super().__init__(env)
        if not isinstance(env.observation_space, Box):
            raise TypeError("ObservationFaultWrapper requires a Box observation space")
        if noise_std < 0:
            raise ValueError("noise_std must be non-negative")
        self.noise_std = float(noise_std)
        self.bias = np.asarray(bias, dtype=env.observation_space.dtype)

    def observation(self, observation):  # type: ignore[no-untyped-def]
        value = np.asarray(observation, dtype=self.observation_space.dtype)
        if self.noise_std:
            noise = self.np_random.normal(0.0, self.noise_std, size=value.shape)
        else:
            noise = 0.0
        corrupted = value + self.bias + noise
        return np.clip(corrupted, self.observation_space.low, self.observation_space.high).astype(
            self.observation_space.dtype
        )
