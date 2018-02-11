# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: merch_service.proto

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
  name='merch_service.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x13merch_service.proto\",\n\x10ShirtDescription\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x13\n\x11GetShirts_Request\"7\n\x12GetShirts_Response\x12!\n\x06shirts\x18\x01 \x03(\x0b\x32\x11.ShirtDescription\"&\n\x18GetRelatedShirts_Request\x12\n\n\x02id\x18\x01 \x01(\r\">\n\x19GetRelatedShirts_Response\x12!\n\x06shirts\x18\x01 \x03(\x0b\x32\x11.ShirtDescription2\x8f\x01\n\x0cMerchService\x12\x34\n\tGetShirts\x12\x12.GetShirts_Request\x1a\x13.GetShirts_Response\x12I\n\x10GetRelatedShirts\x12\x19.GetRelatedShirts_Request\x1a\x1a.GetRelatedShirts_Responseb\x06proto3')
)




_SHIRTDESCRIPTION = _descriptor.Descriptor(
  name='ShirtDescription',
  full_name='ShirtDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ShirtDescription.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ShirtDescription.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=23,
  serialized_end=67,
)


_GETSHIRTS_REQUEST = _descriptor.Descriptor(
  name='GetShirts_Request',
  full_name='GetShirts_Request',
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
  serialized_start=69,
  serialized_end=88,
)


_GETSHIRTS_RESPONSE = _descriptor.Descriptor(
  name='GetShirts_Response',
  full_name='GetShirts_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shirts', full_name='GetShirts_Response.shirts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=90,
  serialized_end=145,
)


_GETRELATEDSHIRTS_REQUEST = _descriptor.Descriptor(
  name='GetRelatedShirts_Request',
  full_name='GetRelatedShirts_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetRelatedShirts_Request.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=147,
  serialized_end=185,
)


_GETRELATEDSHIRTS_RESPONSE = _descriptor.Descriptor(
  name='GetRelatedShirts_Response',
  full_name='GetRelatedShirts_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shirts', full_name='GetRelatedShirts_Response.shirts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=187,
  serialized_end=249,
)

_GETSHIRTS_RESPONSE.fields_by_name['shirts'].message_type = _SHIRTDESCRIPTION
_GETRELATEDSHIRTS_RESPONSE.fields_by_name['shirts'].message_type = _SHIRTDESCRIPTION
DESCRIPTOR.message_types_by_name['ShirtDescription'] = _SHIRTDESCRIPTION
DESCRIPTOR.message_types_by_name['GetShirts_Request'] = _GETSHIRTS_REQUEST
DESCRIPTOR.message_types_by_name['GetShirts_Response'] = _GETSHIRTS_RESPONSE
DESCRIPTOR.message_types_by_name['GetRelatedShirts_Request'] = _GETRELATEDSHIRTS_REQUEST
DESCRIPTOR.message_types_by_name['GetRelatedShirts_Response'] = _GETRELATEDSHIRTS_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShirtDescription = _reflection.GeneratedProtocolMessageType('ShirtDescription', (_message.Message,), dict(
  DESCRIPTOR = _SHIRTDESCRIPTION,
  __module__ = 'merch_service_pb2'
  # @@protoc_insertion_point(class_scope:ShirtDescription)
  ))
_sym_db.RegisterMessage(ShirtDescription)

GetShirts_Request = _reflection.GeneratedProtocolMessageType('GetShirts_Request', (_message.Message,), dict(
  DESCRIPTOR = _GETSHIRTS_REQUEST,
  __module__ = 'merch_service_pb2'
  # @@protoc_insertion_point(class_scope:GetShirts_Request)
  ))
_sym_db.RegisterMessage(GetShirts_Request)

GetShirts_Response = _reflection.GeneratedProtocolMessageType('GetShirts_Response', (_message.Message,), dict(
  DESCRIPTOR = _GETSHIRTS_RESPONSE,
  __module__ = 'merch_service_pb2'
  # @@protoc_insertion_point(class_scope:GetShirts_Response)
  ))
_sym_db.RegisterMessage(GetShirts_Response)

GetRelatedShirts_Request = _reflection.GeneratedProtocolMessageType('GetRelatedShirts_Request', (_message.Message,), dict(
  DESCRIPTOR = _GETRELATEDSHIRTS_REQUEST,
  __module__ = 'merch_service_pb2'
  # @@protoc_insertion_point(class_scope:GetRelatedShirts_Request)
  ))
_sym_db.RegisterMessage(GetRelatedShirts_Request)

GetRelatedShirts_Response = _reflection.GeneratedProtocolMessageType('GetRelatedShirts_Response', (_message.Message,), dict(
  DESCRIPTOR = _GETRELATEDSHIRTS_RESPONSE,
  __module__ = 'merch_service_pb2'
  # @@protoc_insertion_point(class_scope:GetRelatedShirts_Response)
  ))
_sym_db.RegisterMessage(GetRelatedShirts_Response)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class MerchServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetShirts = channel.unary_unary(
          '/MerchService/GetShirts',
          request_serializer=GetShirts_Request.SerializeToString,
          response_deserializer=GetShirts_Response.FromString,
          )
      self.GetRelatedShirts = channel.unary_unary(
          '/MerchService/GetRelatedShirts',
          request_serializer=GetRelatedShirts_Request.SerializeToString,
          response_deserializer=GetRelatedShirts_Response.FromString,
          )


  class MerchServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def GetShirts(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetRelatedShirts(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_MerchServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetShirts': grpc.unary_unary_rpc_method_handler(
            servicer.GetShirts,
            request_deserializer=GetShirts_Request.FromString,
            response_serializer=GetShirts_Response.SerializeToString,
        ),
        'GetRelatedShirts': grpc.unary_unary_rpc_method_handler(
            servicer.GetRelatedShirts,
            request_deserializer=GetRelatedShirts_Request.FromString,
            response_serializer=GetRelatedShirts_Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'MerchService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaMerchServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetShirts(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetRelatedShirts(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaMerchServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetShirts(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    GetShirts.future = None
    def GetRelatedShirts(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    GetRelatedShirts.future = None


  def beta_create_MerchService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('MerchService', 'GetRelatedShirts'): GetRelatedShirts_Request.FromString,
      ('MerchService', 'GetShirts'): GetShirts_Request.FromString,
    }
    response_serializers = {
      ('MerchService', 'GetRelatedShirts'): GetRelatedShirts_Response.SerializeToString,
      ('MerchService', 'GetShirts'): GetShirts_Response.SerializeToString,
    }
    method_implementations = {
      ('MerchService', 'GetRelatedShirts'): face_utilities.unary_unary_inline(servicer.GetRelatedShirts),
      ('MerchService', 'GetShirts'): face_utilities.unary_unary_inline(servicer.GetShirts),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_MerchService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('MerchService', 'GetRelatedShirts'): GetRelatedShirts_Request.SerializeToString,
      ('MerchService', 'GetShirts'): GetShirts_Request.SerializeToString,
    }
    response_deserializers = {
      ('MerchService', 'GetRelatedShirts'): GetRelatedShirts_Response.FromString,
      ('MerchService', 'GetShirts'): GetShirts_Response.FromString,
    }
    cardinalities = {
      'GetRelatedShirts': cardinality.Cardinality.UNARY_UNARY,
      'GetShirts': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'MerchService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
