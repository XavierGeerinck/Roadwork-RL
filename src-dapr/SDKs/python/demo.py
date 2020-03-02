from Client import Client

client = Client('openai-server-1', 'CartPole-v0')
client.Init()
# client.MonitorStart()
client.Reset()


actionSpaceSample = client.ActionSpaceSample()
print(actionSpaceSample)
# stepRes = client.Step(actionSpaceSample)

# while not stepRes.isDone:
#     actionSpaceSample = client.ActionSpaceSample()
#     stepRes = client.Step(actionSpaceSample)

# client.MonitorStop()

# print("Done")