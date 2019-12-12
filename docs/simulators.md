# Simulators

The supported simulators out of the box are situated in `src/SimulatorIntegrations`. The code existing here is the code that is being utilized to hook the simulator onto a [GRPC.io](https://grpc.io) communication server.

## Integrated Simulators

We pre-integrate certain simulators for you, the once integrated can be found below. To correctly document these the following structure is maintained:

```bash
# Project Malmo

## Prerequisites

## Installation

## Running the example
```

**Integrated Simulators:**

* [OpenAI Gym](./simlators-openai.md)
* [Project Malmo](./simlators-malmo.md)

## Writing your own

To integrate your own custom simulator, a couple of steps have to be followed. As a high level overview, the following has to be done:

1. Installation of the simulator
2. Coding a handler that interacts with the simulator based on the `OpenAI` API
3. A serializer has to be written 
