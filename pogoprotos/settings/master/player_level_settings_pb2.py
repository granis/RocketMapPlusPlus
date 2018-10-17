# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/player_level_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/player_level_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6pogoprotos/settings/master/player_level_settings.proto\x12\x1apogoprotos.settings.master\"\xf0\x01\n\x13PlayerLevelSettings\x12\x10\n\x08rank_num\x18\x01 \x03(\x05\x12\x1b\n\x13required_experience\x18\x02 \x03(\x05\x12\x15\n\rcp_multiplier\x18\x03 \x03(\x02\x12\x1c\n\x14max_egg_player_level\x18\x04 \x01(\x05\x12\"\n\x1amax_encounter_player_level\x18\x05 \x01(\x05\x12\'\n\x1fmax_raid_encounter_player_level\x18\x06 \x01(\x05\x12(\n max_quest_encounter_player_level\x18\x07 \x01(\x05\x62\x06proto3')
)




_PLAYERLEVELSETTINGS = _descriptor.Descriptor(
  name='PlayerLevelSettings',
  full_name='pogoprotos.settings.master.PlayerLevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank_num', full_name='pogoprotos.settings.master.PlayerLevelSettings.rank_num', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_experience', full_name='pogoprotos.settings.master.PlayerLevelSettings.required_experience', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cp_multiplier', full_name='pogoprotos.settings.master.PlayerLevelSettings.cp_multiplier', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_egg_player_level', full_name='pogoprotos.settings.master.PlayerLevelSettings.max_egg_player_level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_encounter_player_level', full_name='pogoprotos.settings.master.PlayerLevelSettings.max_encounter_player_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_raid_encounter_player_level', full_name='pogoprotos.settings.master.PlayerLevelSettings.max_raid_encounter_player_level', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_quest_encounter_player_level', full_name='pogoprotos.settings.master.PlayerLevelSettings.max_quest_encounter_player_level', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=87,
  serialized_end=327,
)

DESCRIPTOR.message_types_by_name['PlayerLevelSettings'] = _PLAYERLEVELSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerLevelSettings = _reflection.GeneratedProtocolMessageType('PlayerLevelSettings', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERLEVELSETTINGS,
  __module__ = 'pogoprotos.settings.master.player_level_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PlayerLevelSettings)
  ))
_sym_db.RegisterMessage(PlayerLevelSettings)


# @@protoc_insertion_point(module_scope)
