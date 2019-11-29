# SDKs

## Python

### Example - OpenAI Cartpole - Random Agent

@todo: not implemented yet
```python
import gym

env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
    
env.close()
```

## Node.js

### Example - OpenAI Cartpole - Random Agent

```javascript
const client = new Client('CartPole-v0');
await client.init();
await client.MonitorStart();
await client.Reset();

for (let i = 0; i < 1000; i++) {
  actionSpaceSample = await client.ActionSpaceSample();

  const resStep = await client.Step(actionSpaceSample.action);  
}

await client.MonitorStop();
```

### Example - OpenAI Cartpole - Q-Learning

Currently a Node.js Cartpole agent that is utilizing Q-Learning has been implemented at `src/SDKs/nodejs/examples/OpenAI-CartPole`. To run this, do the following:

1. Install the OpenAI Gym (see `Simulators - OpenAI`)
2. Install Node.js
3. Run `python server.py` under `src/SimulatorIntegrations/OpenAI-Gym`
4. Run `node index.js` under `src/SDKs/nodejs/examples/OpenAI-CartPole`

## Python

## Custom

To write your own simulator, the main thing to take into account is compatiblity with [grpc.io](https://grpc.io). For example code, feel free to take a look at the [grpc tutorials](https://grpc.io/docs/tutorials/) to see on how you are able to utilize this for your own language.

Once you are able to get started with grpc.io, the next thing is to implement the API as defined earlier.