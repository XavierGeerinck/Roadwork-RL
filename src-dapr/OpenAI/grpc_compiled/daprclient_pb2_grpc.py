# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpc_compiled.daprclient_pb2 as daprclient__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DaprClientStub(object):
  """User Code definitions
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.OnInvoke = channel.unary_unary(
        '/daprclient.DaprClient/OnInvoke',
        request_serializer=daprclient__pb2.InvokeEnvelope.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_any__pb2.Any.FromString,
        )
    self.GetTopicSubscriptions = channel.unary_unary(
        '/daprclient.DaprClient/GetTopicSubscriptions',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=daprclient__pb2.GetTopicSubscriptionsEnvelope.FromString,
        )
    self.GetBindingsSubscriptions = channel.unary_unary(
        '/daprclient.DaprClient/GetBindingsSubscriptions',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=daprclient__pb2.GetBindingsSubscriptionsEnvelope.FromString,
        )
    self.OnBindingEvent = channel.unary_unary(
        '/daprclient.DaprClient/OnBindingEvent',
        request_serializer=daprclient__pb2.BindingEventEnvelope.SerializeToString,
        response_deserializer=daprclient__pb2.BindingResponseEnvelope.FromString,
        )
    self.OnTopicEvent = channel.unary_unary(
        '/daprclient.DaprClient/OnTopicEvent',
        request_serializer=daprclient__pb2.CloudEventEnvelope.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class DaprClientServicer(object):
  """User Code definitions
  """

  def OnInvoke(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTopicSubscriptions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBindingsSubscriptions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OnBindingEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OnTopicEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DaprClientServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'OnInvoke': grpc.unary_unary_rpc_method_handler(
          servicer.OnInvoke,
          request_deserializer=daprclient__pb2.InvokeEnvelope.FromString,
          response_serializer=google_dot_protobuf_dot_any__pb2.Any.SerializeToString,
      ),
      'GetTopicSubscriptions': grpc.unary_unary_rpc_method_handler(
          servicer.GetTopicSubscriptions,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=daprclient__pb2.GetTopicSubscriptionsEnvelope.SerializeToString,
      ),
      'GetBindingsSubscriptions': grpc.unary_unary_rpc_method_handler(
          servicer.GetBindingsSubscriptions,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=daprclient__pb2.GetBindingsSubscriptionsEnvelope.SerializeToString,
      ),
      'OnBindingEvent': grpc.unary_unary_rpc_method_handler(
          servicer.OnBindingEvent,
          request_deserializer=daprclient__pb2.BindingEventEnvelope.FromString,
          response_serializer=daprclient__pb2.BindingResponseEnvelope.SerializeToString,
      ),
      'OnTopicEvent': grpc.unary_unary_rpc_method_handler(
          servicer.OnTopicEvent,
          request_deserializer=daprclient__pb2.CloudEventEnvelope.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'daprclient.DaprClient', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
