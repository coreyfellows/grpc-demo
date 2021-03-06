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
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ShirtDescription.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
      options=None, file=DESCRIPTOR),
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
      options=None, file=DESCRIPTOR),
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
      options=None, file=DESCRIPTOR),
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



_MERCHSERVICE = _descriptor.ServiceDescriptor(
  name='MerchService',
  full_name='MerchService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=252,
  serialized_end=395,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetShirts',
    full_name='MerchService.GetShirts',
    index=0,
    containing_service=None,
    input_type=_GETSHIRTS_REQUEST,
    output_type=_GETSHIRTS_RESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRelatedShirts',
    full_name='MerchService.GetRelatedShirts',
    index=1,
    containing_service=None,
    input_type=_GETRELATEDSHIRTS_REQUEST,
    output_type=_GETRELATEDSHIRTS_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MERCHSERVICE)

DESCRIPTOR.services_by_name['MerchService'] = _MERCHSERVICE

# @@protoc_insertion_point(module_scope)
