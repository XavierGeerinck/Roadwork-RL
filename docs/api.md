# API Definition

* **Create:** Create a new environment
  * `@returns`: instanceId (string - represents the spawned instance that we can interact with)
* **Step:** Execute one timestep within the environment
  * `@returns`: reward (the reward received)
  * `@returns`: observation (the next observation)
  * `@returns`: isDone (bool - is the instance finished? if yes we need to call reset())
* **Reset:** Reset the environment for the next use
* **MonitorStart:** Start monitoring the environment, the result is being saved as a video
* **MonitorStop:** Stop monitoring the environment
* **Seed:** Sets the seed for this environment's random number generated

We can see this in action in the [SDKs](./sdks.md)