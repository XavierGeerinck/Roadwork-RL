const GRPCHelper = require('grpc-helper').GRPCHelper;

class Client {
    constructor(envId) {
        this.envId = envId;
        this.instanceId = null;
    }

    async init() {
        const client = new GRPCHelper({
            packageName: 'roadwork.services.simulator_service',
            serviceName: 'Simulator',
            protoPath: `${__dirname}/../../protobuf-definitions/services/simulator.proto`,
            sdUri: 'static://localhost:50051'
        });
    
        await client.waitForReady();

        this.client = client;

        // Create the envrionment
        const res = await client.Create({ envId: 'CartPole-v0' });
        this.instanceId = res.instanceId;
    
        return client;
    }

    async Reset() {
        return this.client.Reset({ instanceId: this.instanceId });
    }

    async ActionSpaceSample() {
        return this.client.ActionSpaceSample({ instanceId: this.instanceId });
    }

    async ObservationSpaceInfo() {
        return this.client.ObservationSpaceInfo({ instanceId: this.instanceId });
    }
    
    async ActionSpaceInfo() {
        return this.client.ActionSpaceInfo({ instanceId: this.instanceId });
    }

    async Step(action) {
        return this.client.Step({
            instanceId: this.instanceId,
            action
        });
    }

    async MonitorStart() {
        return this.client.MonitorStart({ instanceId: this.instanceId });
    }

    async MonitorStop() {
        return this.client.MonitorStop({ instanceId: this.instanceId });
    }
}

module.exports = Client;
