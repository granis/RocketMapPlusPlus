# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/ar_plus_encounter_values.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/ar_plus_encounter_values.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.pogoprotos/data/ar_plus_encounter_values.proto\x12\x0fpogoprotos.data\"Y\n\x15\x41RPlusEncounterValues\x12\x11\n\tproximity\x18\x01 \x01(\x02\x12\x11\n\tawareness\x18\x02 \x01(\x02\x12\x1a\n\x12pokemon_frightened\x18\x03 \x01(\x08\x62\x06proto3')
)




_ARPLUSENCOUNTERVALUES = _descriptor.Descriptor(
  name='ARPlusEncounterValues',
  full_name='pogoprotos.data.ARPlusEncounterValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proximity', full_name='pogoprotos.data.ARPlusEncounterValues.proximity', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='awareness', full_name='pogoprotos.data.ARPlusEncounterValues.awareness', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_frightened', full_name='pogoprotos.data.ARPlusEncounterValues.pokemon_frightened', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=67,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['ARPlusEncounterValues'] = _ARPLUSENCOUNTERVALUES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ARPlusEncounterValues = _reflection.GeneratedProtocolMessageType('ARPlusEncounterValues', (_message.Message,), dict(
  DESCRIPTOR = _ARPLUSENCOUNTERVALUES,
  __module__ = 'pogoprotos.data.ar_plus_encounter_values_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.ARPlusEncounterValues)
  ))
_sym_db.RegisterMessage(ARPlusEncounterValues)


# @@protoc_insertion_point(module_scope)
