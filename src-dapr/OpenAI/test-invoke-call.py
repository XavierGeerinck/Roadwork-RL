import grpc
import grpc_compiled.dapr_pb2 as dapr_messages
import grpc_compiled.dapr_pb2_grpc as dapr_services
import grpc_compiled.daprclient_pb2 as daprclient_messages
import grpc_compiled.daprclient_pb2_grpc as daprclient_services

from google.protobuf.any_pb2 import Any
import os

# Get port from environment variable.
port = os.getenv('DAPR_GRPC_PORT', '5001')
daprUri = 'localhost:' + port
channel = grpc.insecure_channel(daprUri)

# Start a gRPC client
client = dapr_services.DaprStub(channel)

data = Any(value='ACTION=1')
metadata = Any()
client.InvokeService(dapr_messages.InvokeServiceEnvelope(id="1", method="my_method", data=data, metadata=metadata))
print('Invoked!')


# key = 'mykey'
# storeName = 'statestore'
# req = dapr_messages.StateRequest(key=key, value=Any(value='my state'.encode('utf-8')))
# state = dapr_messages.SaveStateEnvelope(storeName=storeName, requests=[req])
# client.SaveState(state)
# print('Saved!')
# resp = client.GetState(dapr_messages.GetStateEnvelope(storeName=storeName, key=key))
# print('Got!')
# print(resp)
# resp = client.DeleteState(dapr_messages.DeleteStateEnvelope(storeName=storeName, key=key))
# print('Deleted!')

channel.close()