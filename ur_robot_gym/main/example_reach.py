import gym
import ur_robot_gym


env = gym.make("UR10Reach-v1", render=True)

obs = env.reset()
for _ in range(500):
    env.render()
    action = env.action_space.sample()
    env.step(action)

env.close()
