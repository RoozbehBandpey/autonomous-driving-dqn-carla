import gym



class DQN:
	def __init__(self):
		pass




if __name__ == "__main__":
	env = gym.make("MountainCar-v0")
	env.reset()

	done = False

	while not done:
		action = 2
		new_state, reward, done, _ = env.step(action)
		# getting position and velocity
		print(new_state)
		env.render(action)

		

	env.close()