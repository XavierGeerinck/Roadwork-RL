import grpc

import grpc_compiled.services.simulator.service_pb2 as simulator_pb2
import grpc_compiled.services.simulator.service_pb2_grpc as simulator_pb2_grpc
import grpc_compiled.services.simulator.request_pb2 as simulator_request_pb2
import grpc_compiled.system.base_request_pb2 as system_request_pb2

class Client:
    def __init__(self, envId, grpcServerUrl='localhost:50051'):
        self.envId = envId
        self.grpcServerUrl = grpcServerUrl
    
    def Init(self):
        self.channel = grpc.insecure_channel(self.grpcServerUrl)
        self.client = simulator_pb2_grpc.SimulatorStub(self.channel)

        req = simulator_request_pb2.CreateRequest(envId=self.envId)
        res = self.client.Create(req)

        self.instanceId = res.instanceId

    def Reset(self):
        req = simulator_request_pb2.ResetRequest(instanceId=self.instanceId)
        return self.client.Reset(req)

    def ActionSpaceSample(self):
        req = simulator_request_pb2.ActionSpaceSampleRequest(instanceId=self.instanceId)
        res = self.client.ActionSpaceSample(req)
        return res.action

    def ActionSpaceInfo(self):
        req = simulator_request_pb2.ActionSpaceInfoRequest(instanceId=self.instanceId)
        return self.client.ActionSpaceInfo(req)

    def ObservationSpaceInfo(self):
        req = simulator_request_pb2.ObservationSpaceInfoRequest(instanceId=self.instanceId)
        return self.client.ObservationSpaceInfo(req)

    def Step(self, action):
        req = simulator_request_pb2.StepRequest(instanceId=self.instanceId, action=action)
        return self.client.Step(req)

    def MonitorStart(self):
        req = system_request_pb2.BaseRequest(instanceId=self.instanceId)
        self.client.MonitorStart(req)

    def MonitorStop(self):
        req = system_request_pb2.BaseRequest(instanceId=self.instanceId)
        self.client.MonitorStop(req)