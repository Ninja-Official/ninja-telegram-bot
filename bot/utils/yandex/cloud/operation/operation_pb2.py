# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/operation/operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&yandex/cloud/operation/operation.proto\x12\x16yandex.cloud.operation\x1a\x19google/protobuf/any.proto\x1a\x17google/rpc/status.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb0\x02\n\tOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x04 \x01(\t\x12/\n\x0bmodified_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x64one\x18\x06 \x01(\x08\x12&\n\x08metadata\x18\x07 \x01(\x0b\x32\x14.google.protobuf.Any\x12#\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x12(\n\x08response\x18\t \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06resultBb\n\x1ayandex.cloud.api.operationZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/operation;operationb\x06proto3')



_OPERATION = DESCRIPTOR.message_types_by_name['Operation']
Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'yandex.cloud.operation.operation_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.operation.Operation)
  })
_sym_db.RegisterMessage(Operation)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032yandex.cloud.api.operationZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/operation;operation'
  _OPERATION._serialized_start=152
  _OPERATION._serialized_end=456
# @@protoc_insertion_point(module_scope)
