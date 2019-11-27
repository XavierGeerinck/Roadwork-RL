const CartPoleAgent = require('./Agent');
const MathUtil = require('../../RL-Utils/MathUtil');

class Experiment {
  constructor(simulatorClient, episodeCount = 1000, maxTimeSteps = 250) {
    this.env = null; // { instanceId: "" }
    this.actionSpaceInfo = null;
    this.agent = null;
    this.sim = simulatorClient;
    this.episodeCount = episodeCount;
    this.maxTimeSteps = maxTimeSteps;
  }

  async initialize() {
    // Create our environment
    this.env = await this.sim.Create({ envId: 'CartPole-v0' });

    // Our ActionSpace
    // For CartPole-v0 this returns: { info: { n: 2, name: 'Discrete' } }
    this.actionSpaceInfo = await this.sim.ActionSpaceInfo({ instanceId: this.env.instanceId });

    // Our ObservationSpace
    // For CartPole-v0 this returns: { info: { high: [XXX], low: [XXX], name: 'Box', shape: [ 4 ] } }
    this.observationSpaceInfo = await this.sim.ObservationSpaceInfo({
        instanceId: this.env.instanceId
    });

    // Rebind our velocity and angular velocity parameters, the pole should stand still as much as possible
    this.observationSpaceInfo.typeBox.high[1] = 0.5;
    this.observationSpaceInfo.typeBox.low[1] = -0.5;
    this.observationSpaceInfo.typeBox.high[3] = MathUtil.radians(50);
    this.observationSpaceInfo.typeBox.low[3] = -MathUtil.radians(50);

    // Set our learning agent
    console.log('Action Space: ');
    console.log(this.actionSpaceInfo);
    console.log('Observation Space: ');
    console.log(this.observationSpaceInfo);

    this.agent = new CartPoleAgent(
      this.actionSpaceInfo.typeDiscrete.n,
      this.observationSpaceInfo.typeBox.shape[0],
      this.observationSpaceInfo.typeBox
    );
  }

  async run() {
    let oldObservation = [];

    await this.initialize();

    // Start Monitoring
    await this.sim.MonitorStart({
        instanceId: this.env.instanceId
    });

    // For every episode
    for (let episode = 0; episode < this.episodeCount; episode++) {
      // Reset the whole environment to start over
      let environment = {
        done: false,
        info: {},
        observation: await this.sim.Reset({
            instanceId: this.env.instanceId
        }),
        reward: 0
      };

      // Keep executing while we can:
      // if state.done = true, then that means the pole tipped to far, or we died
      // if t >= maxTimeSteps, then we did not solve it fast enough
      let t = 0;
      while (!environment.done && t < this.maxTimeSteps) {
        environment = await this.agent.act(
          this.sim,
          this.env.instanceId,
          episode,
          environment.observation
        );
        t++;
      }

      console.log(`Episode ${episode} ended after ${t} timesteps`);
    }

    // Stop Monitoring
    await this.sim.MonitorStop({
        instanceId: this.env.instanceId
    });
    console.log(outDir);
  }
}

module.exports = Experiment;
