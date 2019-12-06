import grpc

import services.simulator_pb2 as simulator_pb2
import services.simulator_pb2_grpc as simulator_pb2_grpc

class Client:
    def __init__(self, envId, grpcServerUrl='localhost:50051'):
        self.envId = envId
        self.grpcServerUrl = grpcServerUrl
    
    def Init(self):
        self.channel = grpc.insecure_channel(self.grpcServerUrl)
        self.client = simulator_pb2_grpc.SimulatorStub(self.channel)

        req = simulator_pb2.SimulatorCreateRequest(envId=self.envId)
        res = self.client.Create(req)

        self.instanceId = res.instanceId

    def Reset(self):
        req = simulator_pb2.SimulatorResetRequest(instanceId=self.instanceId)
        return self.client.Reset(req)

    def ActionSpaceSample(self):
        req = simulator_pb2.SimulatorActionSpaceSampleRequest(instanceId=self.instanceId)
        res = self.client.ActionSpaceSample(req)
        return res.action

    def ActionSpaceInfo(self):
        req = simulator_pb2.SimulatorActionSpaceInfoRequest(instanceId=self.instanceId)
        return self.client.ActionSpaceInfo(req)

    def ObservationSpaceInfo(self):
        req = simulator_pb2.SimulatorObservationSpaceInfoRequest(instanceId=self.instanceId)
        return self.client.ObservationSpaceInfo(req)

    def Step(self, action):
        req = simulator_pb2.SimulatorStepRequest(instanceId=self.instanceId, action=action)
        return self.client.Step(req)

    def MonitorStart(self):
        req = simulator_pb2.BaseRequest(instanceId=self.instanceId)
        self.client.MonitorStart(req)

    def MonitorStop(self):
        req = simulator_pb2.BaseRequest(instanceId=self.instanceId)
        self.client.MonitorStop(req)