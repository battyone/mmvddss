# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getParamEx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='getParamEx.proto',
  package='qlua.rpc.getParamEx',
  syntax='proto3',
  serialized_options=_b('\n\010qlua.rpcH\001'),
  serialized_pb=_b('\n\x10getParamEx.proto\x12\x13qlua.rpc.getParamEx\"W\n\x07ParamEx\x12\x12\n\nparam_type\x18\x01 \x01(\t\x12\x13\n\x0bparam_value\x18\x02 \x01(\t\x12\x13\n\x0bparam_image\x18\x03 \x01(\t\x12\x0e\n\x06result\x18\x04 \x01(\t\"C\n\x07Request\x12\x12\n\nclass_code\x18\x01 \x01(\t\x12\x10\n\x08sec_code\x18\x02 \x01(\t\x12\x12\n\nparam_name\x18\x03 \x01(\t\"8\n\x06Result\x12.\n\x08param_ex\x18\x01 \x01(\x0b\x32\x1c.qlua.rpc.getParamEx.ParamExB\x0c\n\x08qlua.rpcH\x01\x62\x06proto3')
)




_PARAMEX = _descriptor.Descriptor(
  name='ParamEx',
  full_name='qlua.rpc.getParamEx.ParamEx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_type', full_name='qlua.rpc.getParamEx.ParamEx.param_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param_value', full_name='qlua.rpc.getParamEx.ParamEx.param_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param_image', full_name='qlua.rpc.getParamEx.ParamEx.param_image', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='qlua.rpc.getParamEx.ParamEx.result', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=128,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='qlua.rpc.getParamEx.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_code', full_name='qlua.rpc.getParamEx.Request.class_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sec_code', full_name='qlua.rpc.getParamEx.Request.sec_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param_name', full_name='qlua.rpc.getParamEx.Request.param_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=197,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.getParamEx.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_ex', full_name='qlua.rpc.getParamEx.Result.param_ex', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=255,
)

_RESULT.fields_by_name['param_ex'].message_type = _PARAMEX
DESCRIPTOR.message_types_by_name['ParamEx'] = _PARAMEX
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParamEx = _reflection.GeneratedProtocolMessageType('ParamEx', (_message.Message,), dict(
  DESCRIPTOR = _PARAMEX,
  __module__ = 'getParamEx_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getParamEx.ParamEx)
  ))
_sym_db.RegisterMessage(ParamEx)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'getParamEx_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getParamEx.Request)
  ))
_sym_db.RegisterMessage(Request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'getParamEx_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getParamEx.Result)
  ))
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
