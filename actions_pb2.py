# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: actions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='actions.proto',
  package='action',
  syntax='proto3',
  serialized_pb=_b('\n\ractions.proto\x12\x06\x61\x63tion\"\x13\n\x11MonitoringRequest\"$\n\x0fMonitoringReply\x12\x11\n\tisHealthy\x18\x01 \x01(\x08\x32W\n\x08PiAction\x12K\n\x13IsMonitoringHealthy\x12\x19.action.MonitoringRequest\x1a\x17.action.MonitoringReply\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MONITORINGREQUEST = _descriptor.Descriptor(
  name='MonitoringRequest',
  full_name='action.MonitoringRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=44,
)


_MONITORINGREPLY = _descriptor.Descriptor(
  name='MonitoringReply',
  full_name='action.MonitoringReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isHealthy', full_name='action.MonitoringReply.isHealthy', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['MonitoringRequest'] = _MONITORINGREQUEST
DESCRIPTOR.message_types_by_name['MonitoringReply'] = _MONITORINGREPLY

MonitoringRequest = _reflection.GeneratedProtocolMessageType('MonitoringRequest', (_message.Message,), dict(
  DESCRIPTOR = _MONITORINGREQUEST,
  __module__ = 'actions_pb2'
  # @@protoc_insertion_point(class_scope:action.MonitoringRequest)
  ))
_sym_db.RegisterMessage(MonitoringRequest)

MonitoringReply = _reflection.GeneratedProtocolMessageType('MonitoringReply', (_message.Message,), dict(
  DESCRIPTOR = _MONITORINGREPLY,
  __module__ = 'actions_pb2'
  # @@protoc_insertion_point(class_scope:action.MonitoringReply)
  ))
_sym_db.RegisterMessage(MonitoringReply)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class PiActionStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.IsMonitoringHealthy = channel.unary_unary(
          '/action.PiAction/IsMonitoringHealthy',
          request_serializer=MonitoringRequest.SerializeToString,
          response_deserializer=MonitoringReply.FromString,
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
            request_deserializer=MonitoringRequest.FromString,
            response_serializer=MonitoringReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'action.PiAction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaPiActionServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def IsMonitoringHealthy(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaPiActionStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def IsMonitoringHealthy(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    IsMonitoringHealthy.future = None


  def beta_create_PiAction_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('action.PiAction', 'IsMonitoringHealthy'): MonitoringRequest.FromString,
    }
    response_serializers = {
      ('action.PiAction', 'IsMonitoringHealthy'): MonitoringReply.SerializeToString,
    }
    method_implementations = {
      ('action.PiAction', 'IsMonitoringHealthy'): face_utilities.unary_unary_inline(servicer.IsMonitoringHealthy),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_PiAction_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('action.PiAction', 'IsMonitoringHealthy'): MonitoringRequest.SerializeToString,
    }
    response_deserializers = {
      ('action.PiAction', 'IsMonitoringHealthy'): MonitoringReply.FromString,
    }
    cardinalities = {
      'IsMonitoringHealthy': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'action.PiAction', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
