import os
def getDataPath():
  resdir = os.path.join(os.path.dirname(__file__))
  return resdir

from  ur_robot_gym.envs.robots.ur10 import UR10

