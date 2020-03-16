import gym



class DQN:
	def __init__(self):
		pass

# We initalize the Q table with random values, in the first step the agent is gonna explore to adjust the vlaues
# Convert the continous values of states unto descrite values, basically we want to bucket this information 







if __name__ == "__main__":
	env = gym.make("MountainCar-v0")
	env.reset()

	print(env.observation_space.high)
	print(env.observation_space.low)
	print(env.action_space.n)

	DISCRETE_OBESERVATION_SIZE = [20] * len(env.observation_space.high)
	descrite_observation_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OBESERVATION_SIZE

	print(descrite_observation_win_size)
	

	done = False

	while not done:
		action = 2
		new_state, reward, done, _ = env.step(action)
		# getting position and velocity
		# print(new_state)
		env.render(action)

		

	env.close()
