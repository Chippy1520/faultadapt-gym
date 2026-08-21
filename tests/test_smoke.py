from faultadapt_gym.smoke import run_episode


def test_cpu_smoke_episode() -> None:
    result = run_episode(seed=3)
    assert result["steps"] == 200
    assert result["active_fault_steps"] == 150
    assert isinstance(result["return"], float)
