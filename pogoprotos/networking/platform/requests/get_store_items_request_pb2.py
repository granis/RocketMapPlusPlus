# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/get_store_items_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/get_store_items_request.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nEpogoprotos/networking/platform/requests/get_store_items_request.proto\x12\'pogoprotos.networking.platform.requests\"\x16\n\x14GetStoreItemsRequestb\x06proto3')
)




_GETSTOREITEMSREQUEST = _descriptor.Descriptor(
  name='GetStoreItemsRequest',
  full_name='pogoprotos.networking.platform.requests.GetStoreItemsRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['GetStoreItemsRequest'] = _GETSTOREITEMSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetStoreItemsRequest = _reflection.GeneratedProtocolMessageType('GetStoreItemsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSTOREITEMSREQUEST,
  __module__ = 'pogoprotos.networking.platform.requests.get_store_items_request_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.GetStoreItemsRequest)
  ))
_sym_db.RegisterMessage(GetStoreItemsRequest)


# @@protoc_insertion_point(module_scope)
