# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/trade_pokemon_quest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/trade_pokemon_quest.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0pogoprotos/data/quests/trade_pokemon_quest.proto\x12\x16pogoprotos.data.quests\"&\n\x11TradePokemonQuest\x12\x11\n\tfriend_id\x18\x01 \x03(\tb\x06proto3')
)




_TRADEPOKEMONQUEST = _descriptor.Descriptor(
  name='TradePokemonQuest',
  full_name='pogoprotos.data.quests.TradePokemonQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='friend_id', full_name='pogoprotos.data.quests.TradePokemonQuest.friend_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=76,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['TradePokemonQuest'] = _TRADEPOKEMONQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TradePokemonQuest = _reflection.GeneratedProtocolMessageType('TradePokemonQuest', (_message.Message,), dict(
  DESCRIPTOR = _TRADEPOKEMONQUEST,
  __module__ = 'pogoprotos.data.quests.trade_pokemon_quest_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.TradePokemonQuest)
  ))
_sym_db.RegisterMessage(TradePokemonQuest)


# @@protoc_insertion_point(module_scope)
