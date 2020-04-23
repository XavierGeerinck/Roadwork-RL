# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto_compiled.dapr_pb2 as dapr__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DaprStub(object):
  """Dapr definitions
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PublishEvent = channel.unary_unary(
        '/dapr.Dapr/PublishEvent',
        request_serializer=dapr__pb2.PublishEventEnvelope.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InvokeService = channel.unary_unary(
        '/dapr.Dapr/InvokeService',
        request_serializer=dapr__pb2.InvokeServiceEnvelope.SerializeToString,
        response_deserializer=dapr__pb2.InvokeServiceResponseEnvelope.FromString,
        )
    self.InvokeBinding = channel.unary_unary(
        '/dapr.Dapr/InvokeBinding',
        request_serializer=dapr__pb2.InvokeBindingEnvelope.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetState = channel.unary_unary(
        '/dapr.Dapr/GetState',
        request_serializer=dapr__pb2.GetStateEnvelope.SerializeToString,
        response_deserializer=dapr__pb2.GetStateResponseEnvelope.FromString,
        )
    self.GetSecret = channel.unary_unary(
        '/dapr.Dapr/GetSecret',
        request_serializer=dapr__pb2.GetSecretEnvelope.SerializeToString,
        response_deserializer=dapr__pb2.GetSecretResponseEnvelope.FromString,
        )
    self.SaveState = channel.unary_unary(
        '/dapr.Dapr/SaveState',
        request_serializer=dapr__pb2.SaveStateEnvelope.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteState = channel.unary_unary(
        '/dapr.Dapr/DeleteState',
        request_serializer=dapr__pb2.DeleteStateEnvelope.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class DaprServicer(object):
  """Dapr definitions
  """

  def PublishEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InvokeService(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InvokeBinding(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSecret(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DaprServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PublishEvent': grpc.unary_unary_rpc_method_handler(
          servicer.PublishEvent,
          request_deserializer=dapr__pb2.PublishEventEnvelope.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InvokeService': grpc.unary_unary_rpc_method_handler(
          servicer.InvokeService,
          request_deserializer=dapr__pb2.InvokeServiceEnvelope.FromString,
          response_serializer=dapr__pb2.InvokeServiceResponseEnvelope.SerializeToString,
      ),
      'InvokeBinding': grpc.unary_unary_rpc_method_handler(
          servicer.InvokeBinding,
          request_deserializer=dapr__pb2.InvokeBindingEnvelope.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetState': grpc.unary_unary_rpc_method_handler(
          servicer.GetState,
          request_deserializer=dapr__pb2.GetStateEnvelope.FromString,
          response_serializer=dapr__pb2.GetStateResponseEnvelope.SerializeToString,
      ),
      'GetSecret': grpc.unary_unary_rpc_method_handler(
          servicer.GetSecret,
          request_deserializer=dapr__pb2.GetSecretEnvelope.FromString,
          response_serializer=dapr__pb2.GetSecretResponseEnvelope.SerializeToString,
      ),
      'SaveState': grpc.unary_unary_rpc_method_handler(
          servicer.SaveState,
          request_deserializer=dapr__pb2.SaveStateEnvelope.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteState': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteState,
          request_deserializer=dapr__pb2.DeleteStateEnvelope.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dapr.Dapr', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
