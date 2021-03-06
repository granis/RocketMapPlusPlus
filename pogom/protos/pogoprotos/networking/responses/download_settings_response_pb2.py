# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/download_settings_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import global_settings_pb2 as pogoprotos_dot_settings_dot_global__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/download_settings_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@pogoprotos/networking/responses/download_settings_response.proto\x12\x1fpogoprotos.networking.responses\x1a)pogoprotos/settings/global_settings.proto\"n\n\x18\x44ownloadSettingsResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x35\n\x08settings\x18\x03 \x01(\x0b\x32#.pogoprotos.settings.GlobalSettingsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_global__settings__pb2.DESCRIPTOR,])




_DOWNLOADSETTINGSRESPONSE = _descriptor.Descriptor(
  name='DownloadSettingsResponse',
  full_name='pogoprotos.networking.responses.DownloadSettingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='pogoprotos.networking.responses.DownloadSettingsResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='pogoprotos.networking.responses.DownloadSettingsResponse.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='pogoprotos.networking.responses.DownloadSettingsResponse.settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=144,
  serialized_end=254,
)

_DOWNLOADSETTINGSRESPONSE.fields_by_name['settings'].message_type = pogoprotos_dot_settings_dot_global__settings__pb2._GLOBALSETTINGS
DESCRIPTOR.message_types_by_name['DownloadSettingsResponse'] = _DOWNLOADSETTINGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadSettingsResponse = _reflection.GeneratedProtocolMessageType('DownloadSettingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADSETTINGSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.download_settings_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.DownloadSettingsResponse)
  ))
_sym_db.RegisterMessage(DownloadSettingsResponse)


# @@protoc_insertion_point(module_scope)
