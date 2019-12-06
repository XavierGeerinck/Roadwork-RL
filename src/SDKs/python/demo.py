from Client import Client

client = Client('CartPole-v0')
client.Init()
client.MonitorStart()
client.Reset()


actionSpaceSample = client.ActionSpaceSample()
stepRes = client.Step(actionSpaceSample)

while not stepRes.isDone:
    actionSpaceSample = client.ActionSpaceSample()
    stepRes = client.Step(actionSpaceSample)

client.MonitorStop()

print("Done")