# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/event_badge_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import badge_type_pb2 as pogoprotos_dot_enums_dot_badge__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/event_badge_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5pogoprotos/settings/master/event_badge_settings.proto\x12\x1apogoprotos.settings.master\x1a!pogoprotos/enums/badge_type.proto\"\x80\x01\n\x12\x45ventBadgeSettings\x12\x15\n\rvalid_from_ms\x18\x01 \x01(\x03\x12\x13\n\x0bvalid_to_ms\x18\x02 \x01(\x03\x12>\n\x19mutually_exclusive_badges\x18\x03 \x03(\x0e\x32\x1b.pogoprotos.enums.BadgeTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_badge__type__pb2.DESCRIPTOR,])




_EVENTBADGESETTINGS = _descriptor.Descriptor(
  name='EventBadgeSettings',
  full_name='pogoprotos.settings.master.EventBadgeSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid_from_ms', full_name='pogoprotos.settings.master.EventBadgeSettings.valid_from_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_to_ms', full_name='pogoprotos.settings.master.EventBadgeSettings.valid_to_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutually_exclusive_badges', full_name='pogoprotos.settings.master.EventBadgeSettings.mutually_exclusive_badges', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=121,
  serialized_end=249,
)

_EVENTBADGESETTINGS.fields_by_name['mutually_exclusive_badges'].enum_type = pogoprotos_dot_enums_dot_badge__type__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name['EventBadgeSettings'] = _EVENTBADGESETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventBadgeSettings = _reflection.GeneratedProtocolMessageType('EventBadgeSettings', (_message.Message,), dict(
  DESCRIPTOR = _EVENTBADGESETTINGS,
  __module__ = 'pogoprotos.settings.master.event_badge_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.EventBadgeSettings)
  ))
_sym_db.RegisterMessage(EventBadgeSettings)


# @@protoc_insertion_point(module_scope)
