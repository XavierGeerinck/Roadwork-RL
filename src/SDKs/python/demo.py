import Client from Client

client = new Client('CartPole-v0')
client.MonitorStart()
client.Reset()

for _ in range(1000):
    actionSpaceSample = client.ActionSpaceSample()
    client.Step(actionSpaceSample)

client.MonitorStop()


# # Original
# env = gym.make('CartPole-v0')
# env.reset()

# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample())
    
# env.close()

# # Javascript
# const client = new Client('CartPole-v0');
# await client.init();
# await client.MonitorStart();
# await client.Reset();

# for (let i = 0; i < 1000; i++) {
#   actionSpaceSample = await client.ActionSpaceSample();

#   const resStep = await client.Step(actionSpaceSample.action);  
# }

# await client.MonitorStop();