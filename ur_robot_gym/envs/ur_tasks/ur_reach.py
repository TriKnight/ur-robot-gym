from ur_robot_gym.envs.core import RobotTaskEnv
from ur_robot_gym.pybullet_gym import PyBullet_gym
from ur_robot_gym.envs.robots import UR10
from ur_robot_gym.envs.tasks import Reach


class UR10ReachEnv(RobotTaskEnv):
    """Reach task wih Panda robot.

    Args:
        render (bool, optional): Activate rendering. Defaults to False.
        reward_type (str, optional): "sparse" or "dense". Defaults to "sparse".
    """

    def __init__(self, render=False, reward_type="sparse"):
        self.sim = PyBullet_gym(render=render)
        self.robot = UR10(self.sim, block_gripper=True, base_position=[-0.6, 0.0, 0.0])
        self.task = Reach(
            self.sim,
            reward_type=reward_type,
            get_ee_position=self.robot.get_ee_position,
        )
        RobotTaskEnv.__init__(self)
