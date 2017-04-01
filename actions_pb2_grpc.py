# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import actions_pb2 as actions__pb2


class PiActionStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.IsMonitoringHealthy = channel.unary_unary(
        '/action.PiAction/IsMonitoringHealthy',
        request_serializer=actions__pb2.MonitoringRequest.SerializeToString,
        response_deserializer=actions__pb2.MonitoringReply.FromString,
        )


class PiActionServicer(object):

  def IsMonitoringHealthy(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PiActionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'IsMonitoringHealthy': grpc.unary_unary_rpc_method_handler(
          servicer.IsMonitoringHealthy,
          request_deserializer=actions__pb2.MonitoringRequest.FromString,
          response_serializer=actions__pb2.MonitoringReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'action.PiAction', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))