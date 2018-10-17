# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/social_client_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/social_client_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0pogoprotos/settings/social_client_settings.proto\x12\x13pogoprotos.settings\"\xcd\x01\n\x14SocialClientSettings\x12\x15\n\renable_social\x18\x01 \x01(\x08\x12\x1a\n\x12max_friend_details\x18\x02 \x01(\x05\x12\x19\n\x11player_level_gate\x18\x03 \x01(\x05\x12\"\n\x1amax_friend_nickname_length\x18\x04 \x01(\x05\x12%\n\x1d\x65nable_add_friend_via_qr_code\x18\x05 \x01(\x08\x12\x1c\n\x14\x65nable_share_ex_pass\x18\x06 \x01(\x08\"R\n\x18SocialGiftCountTelemetry\x12\x1b\n\x13unopened_gift_count\x18\x01 \x01(\x05\x12\x19\n\x11unsent_gift_count\x18\x02 \x01(\x05\x62\x06proto3')
)




_SOCIALCLIENTSETTINGS = _descriptor.Descriptor(
  name='SocialClientSettings',
  full_name='pogoprotos.settings.SocialClientSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_social', full_name='pogoprotos.settings.SocialClientSettings.enable_social', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_friend_details', full_name='pogoprotos.settings.SocialClientSettings.max_friend_details', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_level_gate', full_name='pogoprotos.settings.SocialClientSettings.player_level_gate', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_friend_nickname_length', full_name='pogoprotos.settings.SocialClientSettings.max_friend_nickname_length', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_add_friend_via_qr_code', full_name='pogoprotos.settings.SocialClientSettings.enable_add_friend_via_qr_code', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_share_ex_pass', full_name='pogoprotos.settings.SocialClientSettings.enable_share_ex_pass', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=74,
  serialized_end=279,
)


_SOCIALGIFTCOUNTTELEMETRY = _descriptor.Descriptor(
  name='SocialGiftCountTelemetry',
  full_name='pogoprotos.settings.SocialGiftCountTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unopened_gift_count', full_name='pogoprotos.settings.SocialGiftCountTelemetry.unopened_gift_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unsent_gift_count', full_name='pogoprotos.settings.SocialGiftCountTelemetry.unsent_gift_count', index=1,
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
  serialized_start=281,
  serialized_end=363,
)

DESCRIPTOR.message_types_by_name['SocialClientSettings'] = _SOCIALCLIENTSETTINGS
DESCRIPTOR.message_types_by_name['SocialGiftCountTelemetry'] = _SOCIALGIFTCOUNTTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SocialClientSettings = _reflection.GeneratedProtocolMessageType('SocialClientSettings', (_message.Message,), dict(
  DESCRIPTOR = _SOCIALCLIENTSETTINGS,
  __module__ = 'pogoprotos.settings.social_client_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.SocialClientSettings)
  ))
_sym_db.RegisterMessage(SocialClientSettings)

SocialGiftCountTelemetry = _reflection.GeneratedProtocolMessageType('SocialGiftCountTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _SOCIALGIFTCOUNTTELEMETRY,
  __module__ = 'pogoprotos.settings.social_client_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.SocialGiftCountTelemetry)
  ))
_sym_db.RegisterMessage(SocialGiftCountTelemetry)


# @@protoc_insertion_point(module_scope)
