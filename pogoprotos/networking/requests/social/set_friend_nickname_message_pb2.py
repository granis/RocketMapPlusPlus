# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/set_friend_nickname_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/set_friend_nickname_message.proto',
  package='pogoprotos.networking.requests.social',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nGpogoprotos/networking/requests/social/set_friend_nickname_message.proto\x12%pogoprotos.networking.requests.social\"F\n\x18SetFriendNicknameMessage\x12\x11\n\tfriend_id\x18\x01 \x01(\t\x12\x17\n\x0f\x66riend_nickname\x18\x02 \x01(\tb\x06proto3')
)




_SETFRIENDNICKNAMEMESSAGE = _descriptor.Descriptor(
  name='SetFriendNicknameMessage',
  full_name='pogoprotos.networking.requests.social.SetFriendNicknameMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='friend_id', full_name='pogoprotos.networking.requests.social.SetFriendNicknameMessage.friend_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_nickname', full_name='pogoprotos.networking.requests.social.SetFriendNicknameMessage.friend_nickname', index=1,
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
  serialized_start=114,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['SetFriendNicknameMessage'] = _SETFRIENDNICKNAMEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetFriendNicknameMessage = _reflection.GeneratedProtocolMessageType('SetFriendNicknameMessage', (_message.Message,), dict(
  DESCRIPTOR = _SETFRIENDNICKNAMEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.set_friend_nickname_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.SetFriendNicknameMessage)
  ))
_sym_db.RegisterMessage(SetFriendNicknameMessage)


# @@protoc_insertion_point(module_scope)
