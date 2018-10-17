# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/fitness_rewards_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/fitness_rewards_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4pogoprotos/data/logs/fitness_rewards_log_entry.proto\x12\x14pogoprotos.data.logs\x1a\x1fpogoprotos/inventory/loot.proto\"\xc8\x01\n\x16\x46itnessRewardsLogEntry\x12\x43\n\x06result\x18\x01 \x01(\x0e\x32\x33.pogoprotos.data.logs.FitnessRewardsLogEntry.Result\x12+\n\x07rewards\x18\x02 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12\x1a\n\x12\x64istance_walked_km\x18\x03 \x01(\x01\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,])



_FITNESSREWARDSLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.FitnessRewardsLogEntry.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=280,
  serialized_end=312,
)
_sym_db.RegisterEnumDescriptor(_FITNESSREWARDSLOGENTRY_RESULT)


_FITNESSREWARDSLOGENTRY = _descriptor.Descriptor(
  name='FitnessRewardsLogEntry',
  full_name='pogoprotos.data.logs.FitnessRewardsLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.FitnessRewardsLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='pogoprotos.data.logs.FitnessRewardsLogEntry.rewards', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance_walked_km', full_name='pogoprotos.data.logs.FitnessRewardsLogEntry.distance_walked_km', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FITNESSREWARDSLOGENTRY_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=312,
)

_FITNESSREWARDSLOGENTRY.fields_by_name['result'].enum_type = _FITNESSREWARDSLOGENTRY_RESULT
_FITNESSREWARDSLOGENTRY.fields_by_name['rewards'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_FITNESSREWARDSLOGENTRY_RESULT.containing_type = _FITNESSREWARDSLOGENTRY
DESCRIPTOR.message_types_by_name['FitnessRewardsLogEntry'] = _FITNESSREWARDSLOGENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FitnessRewardsLogEntry = _reflection.GeneratedProtocolMessageType('FitnessRewardsLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _FITNESSREWARDSLOGENTRY,
  __module__ = 'pogoprotos.data.logs.fitness_rewards_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.FitnessRewardsLogEntry)
  ))
_sym_db.RegisterMessage(FitnessRewardsLogEntry)


# @@protoc_insertion_point(module_scope)
