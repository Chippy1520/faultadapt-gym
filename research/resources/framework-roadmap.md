# Framework Learning Roadmap

## Learn now — required for FaultAdapt-Gym

1. **Python scientific stack:** NumPy, SciPy, pandas, Matplotlib, JupyterLab.
2. **Gymnasium:** environment API, wrappers, spaces, seeding, vector environments.
3. **MuJoCo:** models, state/action semantics, contacts, actuator parameters, deterministic stepping.
4. **Stable-Baselines3:** PPO, callbacks, evaluation, checkpointing, and vectorized environments.
5. **SB3-Contrib:** RecurrentPPO and recurrent-state handling.
6. **PyTorch fundamentals:** tensors, modules, optimizers, recurrent networks, CPU profiling, and reproducibility.
7. **python-control and system identification concepts:** state-space models, LQR, observers, recursive least squares, and parameter identifiability.
8. **Git, pytest, Ruff, TensorBoard:** reproducibility and engineering discipline.

## Learn next — useful after the CPU benchmark works

1. **robosuite:** MuJoCo manipulation tasks and robot-learning interfaces.
2. **ROS 2 Jazzy + Gazebo Harmonic:** nodes, topics, actions, TF2, ros2_control, simulation bridges, and bags.
3. **Hydra or a lightweight config system:** only when experiment configurations become numerous.
4. **CasADi:** optimization/MPC if the explicit adaptation baseline needs it.
5. **Docker:** clean reproduction and lab deployment after the local workflow stabilizes.

## Defer until suitable GPU access

1. **Isaac Sim:** photorealistic and sensor-rich NVIDIA simulation.
2. **Isaac Lab:** massively parallel GPU robot-learning workflows on Isaac Sim.
3. **LeRobot/SmolVLA:** dataset tooling and vision-language-action policy evaluation/fine-tuning.
4. **Pixel-based robosuite/RoboCasa:** visual manipulation experiments.

## Official resources

- Gymnasium: https://gymnasium.farama.org/
- MuJoCo: https://mujoco.readthedocs.io/
- Stable-Baselines3: https://stable-baselines3.readthedocs.io/
- SB3-Contrib RecurrentPPO: https://sb3-contrib.readthedocs.io/en/master/modules/ppo_recurrent.html
- PyTorch tutorials: https://pytorch.org/tutorials/
- python-control: https://python-control.readthedocs.io/
- robosuite: https://robosuite.ai/docs/
- ROS 2 Jazzy: https://docs.ros.org/en/jazzy/
- Gazebo with ROS: https://gazebosim.org/docs/latest/ros_installation/
- Isaac Sim: https://docs.isaacsim.omniverse.nvidia.com/
- Isaac Lab: https://isaac-sim.github.io/IsaacLab/main/
- LeRobot: https://huggingface.co/docs/lerobot/en/index
