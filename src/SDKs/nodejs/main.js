const GRPCHelper = require('grpc-helper').GRPCHelper;

class Client {
    async initialize() {
        const client = new GRPCHelper({
            packageName: 'roadwork.services.simulator_service',
            serviceName: 'Simulator',
            protoPath: `${__dirname}/../../protobuf-definitions/services/simulator.proto`,
            sdUri: 'static://localhost:50051'
        });
    
        await client.waitForReady();
    
        return client;
    }
}

module.exports = new Client();
