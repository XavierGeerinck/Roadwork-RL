import grpc
import grpc_compiled.dapr_pb2 as dapr_messages
import grpc_compiled.dapr_pb2_grpc as dapr_services
import grpc_compiled.daprclient_pb2 as daprclient_messages
import grpc_compiled.daprclient_pb2_grpc as daprclient_services

# Our server methods
class DaprClientServicer(daprclient_services.DaprClientServicer):
    def OnInvoke(self, request, context):
      print(request)
      print(context)
      print("INVOKED SOMETHING")
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

# Create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
daprclient_services.add_DaprClientServicer_to_server(DaprClientServicer(), server)

# Start the gRPC server
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)