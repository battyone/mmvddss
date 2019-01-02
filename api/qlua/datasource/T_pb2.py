# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: T.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='T.proto',
  package='qlua.rpc.datasource.T',
  syntax='proto3',
  serialized_options=_b('\n\023qlua.rpc.datasourceH\001'),
  serialized_pb=_b('\n\x07T.proto\x12\x15qlua.rpc.datasource.T\"8\n\x07Request\x12\x17\n\x0f\x64\x61tasource_uuid\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61ndle_index\x18\x02 \x01(\x05\"\x87\x01\n\x06Result\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\x12\x10\n\x08week_day\x18\x04 \x01(\x05\x12\x0c\n\x04hour\x18\x05 \x01(\x05\x12\x0b\n\x03min\x18\x06 \x01(\x05\x12\x0b\n\x03sec\x18\x07 \x01(\x05\x12\n\n\x02ms\x18\x08 \x01(\x05\x12\r\n\x05\x63ount\x18\t \x01(\x05\x42\x17\n\x13qlua.rpc.datasourceH\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='qlua.rpc.datasource.T.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datasource_uuid', full_name='qlua.rpc.datasource.T.Request.datasource_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candle_index', full_name='qlua.rpc.datasource.T.Request.candle_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=34,
  serialized_end=90,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.datasource.T.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='qlua.rpc.datasource.T.Result.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='qlua.rpc.datasource.T.Result.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='qlua.rpc.datasource.T.Result.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='week_day', full_name='qlua.rpc.datasource.T.Result.week_day', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='qlua.rpc.datasource.T.Result.hour', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='qlua.rpc.datasource.T.Result.min', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sec', full_name='qlua.rpc.datasource.T.Result.sec', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ms', full_name='qlua.rpc.datasource.T.Result.ms', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='qlua.rpc.datasource.T.Result.count', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=93,
  serialized_end=228,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'T_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.datasource.T.Request)
  ))
_sym_db.RegisterMessage(Request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'T_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.datasource.T.Result)
  ))
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)