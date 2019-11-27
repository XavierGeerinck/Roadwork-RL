const GRPCHelper = require('grpc-helper').GRPCHelper;

const main = async () => {
    const client = new GRPCHelper({
        packageName: 'roadwork.services.simulator_service',
        serviceName: 'Simulator',
        protoPath: `${__dirname}/../../protobuf-definitions/services/simulator.proto`,
        sdUri: 'static://localhost:50051'
    });

    await client.waitForReady();

    try { 
        // Create Gym
        const res = await client.Create({
            // envId: 'Blackjack-v0'
            envId: 'CartPole-v0'
        });

        console.log(res);

        // ObservationSpace Info
        const resObservationSpace = await client.ObservationSpaceInfo({ instanceId: res.instanceId });

        console.log('\nObservation Space')
        console.log(resObservationSpace)

        // ActionSpace Info
        const resActionSpace = await client.ActionSpaceInfo({ instanceId: res.instanceId });

        console.log('\nAction Space')
        console.log(resActionSpace)

        let actionSpaceSample = await client.ActionSpaceSample({ instanceId: res.instanceId });
        console.log('\nActionSpace Sample');
        console.log(actionSpaceSample);

        // Step
        await client.MonitorStart({ instanceId: res.instanceId });

        // Reset
        const resReset = await client.Reset({ instanceId: res.instanceId });
        console.log('\nReset')
        console.log(resReset);

        let isDone = false;
        let i = 1;

        while (!isDone) {
            console.log(`Iteration: ${i}`);
            // await client.Render({ instanceId: res.instanceId });

            actionSpaceSample = await client.ActionSpaceSample({ instanceId: res.instanceId });
            console.log(actionSpaceSample.action);

            console.log('Taking Step');
            const resStep = await client.Step({
                instanceId: res.instanceId,
                action: actionSpaceSample.action
            });
            console.log(resStep);

            isDone = resStep.isDone;
            i++;
        }
        
        await client.MonitorStop({ instanceId: res.instanceId });
    } catch (e) {
        console.log(e);
    }

}

main();


// import gym

// env = gym.make('CartPole-v0')
// env.reset()

// for _ in range(1000):
//     env.render()
//     env.step(env.action_space.sample())
    
// env.close()