import os
from concurrent import futures
import time

import grpc
import proto_compiled.dapr_pb2 as dapr_messages
import proto_compiled.dapr_pb2_grpc as dapr_services
import proto_compiled.daprclient_pb2 as daprclient_messages
import proto_compiled.daprclient_pb2_grpc as daprclient_services
import proto_compiled.roadwork_pb2 as roadwork_messages

import protobuf_helpers

from google.protobuf.any_pb2 import Any

# Import OpenAI
from OpenAIEnv import Envs
# import gym
envs = Envs()

# Start a gRPC client
port = os.getenv('DAPR_GRPC_PORT')
channel = grpc.insecure_channel(f"localhost:{port}")
client = dapr_services.DaprStub(channel)
print(f"Started gRPC client on DAPR_GRPC_PORT: {port}")

# Our server methods
class DaprClientServicer(daprclient_services.DaprClientServicer):
    # def DaprUnpack(self, pb_type, any_pb):
    #     msg = pb_type()

    #     print(res)
    #     print(res.DESCRIPTOR)
    #     print(res.DESCRIPTOR.name)
    #     # # Unpack the response
    #     # res = roadwork_messages.ActionSpaceSampleResponse()
    #     # response.data.type_url = "type.googleapis.com/roadwork.ActionSpaceSampleResponse"
    #     # response.data.Unpack(res)

    def OnInvoke(self, request, context):
        response = ""

        print(request)

        if request.method == 'create':
            req = protobuf_helpers.from_any_pb(roadwork_messages.CreateRequest, request.data)
            response = roadwork_messages.CreateResponse(instanceId=envs.create(req.envId))
            response = protobuf_helpers.to_any_pb(response)
        elif request.method == 'reset':
            req = protobuf_helpers.from_any_pb(roadwork_messages.ResetRequest, request.data)
            response = roadwork_messages.ResetResponse(observation=envs.reset(req.instanceId))
            response = protobuf_helpers.to_any_pb(response)
        elif request.method == 'action-space-sample':
            req = protobuf_helpers.from_any_pb(roadwork_messages.ActionSpaceSampleRequest, request.data)
            response = roadwork_messages.ActionSpaceSampleResponse(action=envs.get_action_space_sample(req.instanceId))
            response = protobuf_helpers.to_any_pb(response)
        else:
            response = Any(value='METHOD_NOT_SUPPORTED'.encode('utf-8'))

        # Debug
        # print(response.DESCRIPTOR.name)
        # print(response.type_url) # Needed to know how to Unpack

        return response

# Create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
daprclient_services.add_DaprClientServicer_to_server(DaprClientServicer(), server)

# Start the gRPC server
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# Since server.start() doesn't block, we need to do a sleep loop
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)