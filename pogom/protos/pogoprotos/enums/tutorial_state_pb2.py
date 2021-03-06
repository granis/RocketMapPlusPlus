# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/tutorial_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/tutorial_state.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%pogoprotos/enums/tutorial_state.proto\x12\x10pogoprotos.enums*\x8f\x04\n\rTutorialState\x12\x10\n\x0cLEGAL_SCREEN\x10\x00\x12\x14\n\x10\x41VATAR_SELECTION\x10\x01\x12\x14\n\x10\x41\x43\x43OUNT_CREATION\x10\x02\x12\x13\n\x0fPOKEMON_CAPTURE\x10\x03\x12\x12\n\x0eNAME_SELECTION\x10\x04\x12\x11\n\rPOKEMON_BERRY\x10\x05\x12\x1b\n\x17USE_ITEM_TUTORIAL_STATE\x10\x06\x12\"\n\x1e\x46IRST_TIME_EXPERIENCE_COMPLETE\x10\x07\x12\x15\n\x11POKESTOP_TUTORIAL\x10\x08\x12\x10\n\x0cGYM_TUTORIAL\x10\t\x12\x1c\n\x18\x43HALLENGE_QUEST_TUTORIAL\x10\n\x12\x1f\n\x1bPRIVACY_POLICY_CONFIRMATION\x10\x0b\x12\x14\n\x10TRADING_TUTORIAL\x10\x0c\x12\x1b\n\x17POI_SUBMISSION_TUTORIAL\x10\r\x12\x15\n\x11V1_START_TUTORIAL\x10\x0e\x12\x15\n\x11V2_START_TUTORIAL\x10\x0f\x12\x18\n\x14V2_CUSTOMIZED_AVATAR\x10\x10\x12\x15\n\x11V2_CAUGHT_STARTER\x10\x11\x12 \n\x1cV2_FINISHED_TUTORIAL_CATCHES\x10\x12\x12\x15\n\x11V2_NAME_SELECTION\x10\x13\x12\x10\n\x0cV2_EGG_GIVEN\x10\x14\x62\x06proto3')
)

_TUTORIALSTATE = _descriptor.EnumDescriptor(
  name='TutorialState',
  full_name='pogoprotos.enums.TutorialState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEGAL_SCREEN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_SELECTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_CREATION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_CAPTURE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_SELECTION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_BERRY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_TUTORIAL_STATE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST_TIME_EXPERIENCE_COMPLETE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_TUTORIAL', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_TUTORIAL', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_QUEST_TUTORIAL', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_POLICY_CONFIRMATION', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADING_TUTORIAL', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_SUBMISSION_TUTORIAL', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V1_START_TUTORIAL', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_START_TUTORIAL', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_CUSTOMIZED_AVATAR', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_CAUGHT_STARTER', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_FINISHED_TUTORIAL_CATCHES', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_NAME_SELECTION', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_EGG_GIVEN', index=20, number=20,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=60,
  serialized_end=587,
)
_sym_db.RegisterEnumDescriptor(_TUTORIALSTATE)

TutorialState = enum_type_wrapper.EnumTypeWrapper(_TUTORIALSTATE)
LEGAL_SCREEN = 0
AVATAR_SELECTION = 1
ACCOUNT_CREATION = 2
POKEMON_CAPTURE = 3
NAME_SELECTION = 4
POKEMON_BERRY = 5
USE_ITEM_TUTORIAL_STATE = 6
FIRST_TIME_EXPERIENCE_COMPLETE = 7
POKESTOP_TUTORIAL = 8
GYM_TUTORIAL = 9
CHALLENGE_QUEST_TUTORIAL = 10
PRIVACY_POLICY_CONFIRMATION = 11
TRADING_TUTORIAL = 12
POI_SUBMISSION_TUTORIAL = 13
V1_START_TUTORIAL = 14
V2_START_TUTORIAL = 15
V2_CUSTOMIZED_AVATAR = 16
V2_CAUGHT_STARTER = 17
V2_FINISHED_TUTORIAL_CATCHES = 18
V2_NAME_SELECTION = 19
V2_EGG_GIVEN = 20


DESCRIPTOR.enum_types_by_name['TutorialState'] = _TUTORIALSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
