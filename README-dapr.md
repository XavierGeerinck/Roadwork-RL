# Installation Progress

1. Install Dapr CLI
    * https://github.com/dapr/docs/blob/master/getting-started/environment-setup.md
    * Note: installed standalone one
2. Init Dapr with `dapr init`

# Running OpenAI Gym Environment
cd SimulatorIntegrations-Dapr\OpenAI-Gym
pip install -r requirements.txt

# Idea on Actor mapping
Actor is self defined
This means that we create one, and we can run sims on it

> Note: seems that Actors are not implemented in Python-SDK....

Therefor following methods could be called:
curl http://localhost:50002/v1.0/actors/sim-openai/1/method/step
* http://localhost:50002/v1.0/actors/SimActor/OpenAI_CartPole_1/method/Step
--> SimActor, OpenAI_CartPole (<Simulator>_<Env>), Step
curl http://localhost:50002/v1.0/actors/sim-openai/1/method/step

# Examples HTTP

## Actor Step Act 

```bash
http://localhost:50002/v1.0/actors/SimActor/OpenAI_CartPole_1/method/Step
# --> SimActor, OpenAI_CartPole (<Simulator>_<Env>), Step
```

## Invoke Direct Method on Dapr App

```bash
http://localhost:<daprPort>/v1.0/invoke/<appId>/method/<method-name>

# Example
curl http://localhost:3500/v1.0/invoke/python-grpc/method/test
```

# Examples

## Python POST Call

```python
def Step():
    Simulator = "OpenAI"
    SimulatorEnv = "CartPole"
    SimulatorId = f'{Simulator}_{SimulatorEnv}'

    daprUrl = f'http://localhost:50002/v1.0/actors/SimActor/{SimulatorId}/method/Step'
    header  = { "Content-Type": "application/json" }
    data    = {
        "Key": "Some_Value"
    }

    r = requests.post(daprUrl, json=data, headers=header)
    return
```