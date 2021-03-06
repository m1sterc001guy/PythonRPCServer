# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import zwaveactions_pb2 as zwaveactions__pb2


class ZWaveActionStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ToggleLight = channel.unary_unary(
        '/zwave.ZWaveAction/ToggleLight',
        request_serializer=zwaveactions__pb2.ToggleRequest.SerializeToString,
        response_deserializer=zwaveactions__pb2.ToggleReply.FromString,
        )
    self.GetLightStatus = channel.unary_unary(
        '/zwave.ZWaveAction/GetLightStatus',
        request_serializer=zwaveactions__pb2.LightStatusRequest.SerializeToString,
        response_deserializer=zwaveactions__pb2.LightStatusReply.FromString,
        )


class ZWaveActionServicer(object):

  def ToggleLight(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLightStatus(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ZWaveActionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ToggleLight': grpc.unary_unary_rpc_method_handler(
          servicer.ToggleLight,
          request_deserializer=zwaveactions__pb2.ToggleRequest.FromString,
          response_serializer=zwaveactions__pb2.ToggleReply.SerializeToString,
      ),
      'GetLightStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetLightStatus,
          request_deserializer=zwaveactions__pb2.LightStatusRequest.FromString,
          response_serializer=zwaveactions__pb2.LightStatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'zwave.ZWaveAction', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
