"""FaultAdapt-Gym: fault-injection wrappers for adaptive robot-control research."""

from .wrappers import (
    ActionDelayWrapper,
    ActuatorFaultWrapper,
    FaultSchedule,
    ObservationFaultWrapper,
)

__all__ = [
    "ActionDelayWrapper",
    "ActuatorFaultWrapper",
    "FaultSchedule",
    "ObservationFaultWrapper",
]

__version__ = "0.1.0"
