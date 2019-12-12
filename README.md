# Roadwork
A Reinforcement Learning library that act as an abstraction layer between different simulation environments and languages, allowing for simulator &amp; code agnostic reinforcement learning research to be done.

Following diagram tries to explain this in more detail:

![/assets/architecture-high-level.png](./assets/architecture-high-level.png)

The API that is being utilized to interact with the different simulators, is the one as defined by the [`OpenAI` API specification](https://github.com/openai/gym/blob/master/gym/core.py) enriched by extra methods (such as the `Create` one). 

We enrich this API since OpenAI has a good basis but can also utilize extra methods for multi-environment management.

## Dependencies Utilized

- [grpc.io](https://grpc.io)
- [OpenAI](https://github.com/openai/gym)
- [Protobuf](https://github.com/protocolbuffers/protobuf)

## References

* [Protobuf Serialization](./docs/protobuf.md)
* [Spaces](./docs/spaces.md)
* [SDKs](./docs/sdks.md)
* [Simulators](./docs/simulators.md)

## TODO

* Integrate [Facebook ReAgent](https://github.com/facebookresearch/ReAgent) on top of this
    * Simulation Observation Downloader
    * Trainer On-Policy & Off-Policy
* Add [Project Malmo](https://www.microsoft.com/en-us/research/project/project-malmo/)
* Add [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents)
* Create a custom language for state describing
    * Currently we can describe a state as shown before: `Tuple([ Box(0, 255, shape=(64, 64, 3)), Box(-50, 50, shape=(3, )) ])`. This might be too abstract or language dependent and could be done easier + more efficient. E.g. think of a Robotic arm, where we should be able to describe each join independently.
* Performance Benchmarks (what is the impact of this library compared to a vanilla implemented)