import gym

env = gym.make('CartPole-v0')
print(env)
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
    
env.close()