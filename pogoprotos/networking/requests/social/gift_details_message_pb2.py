# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/gift_details_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/gift_details_message.proto',
  package='pogoprotos.networking.requests.social',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@pogoprotos/networking/requests/social/gift_details_message.proto\x12%pogoprotos.networking.requests.social\";\n\x12GiftDetailsMessage\x12\x12\n\ngiftbox_id\x18\x01 \x03(\x06\x12\x11\n\tplayer_id\x18\x02 \x01(\tb\x06proto3')
)




_GIFTDETAILSMESSAGE = _descriptor.Descriptor(
  name='GiftDetailsMessage',
  full_name='pogoprotos.networking.requests.social.GiftDetailsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='giftbox_id', full_name='pogoprotos.networking.requests.social.GiftDetailsMessage.giftbox_id', index=0,
      number=1, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.networking.requests.social.GiftDetailsMessage.player_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=107,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['GiftDetailsMessage'] = _GIFTDETAILSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GiftDetailsMessage = _reflection.GeneratedProtocolMessageType('GiftDetailsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GIFTDETAILSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.gift_details_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.GiftDetailsMessage)
  ))
_sym_db.RegisterMessage(GiftDetailsMessage)


# @@protoc_insertion_point(module_scope)
