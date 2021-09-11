

from gym.envs.registration import register

for reward_type in ["sparse", "dense"]:
    suffix = "Dense" if reward_type == "dense" else ""
    kwargs = {
        "reward_type": reward_type,
    }

    register(
        id="UR10Reach{}-v1".format(suffix),
        entry_point="ur_robot_gym.envs:UR10ReachEnv",
        kwargs=kwargs,
        max_episode_steps=50,
    )
