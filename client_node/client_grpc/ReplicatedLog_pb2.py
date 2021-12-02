# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_grpc/ReplicatedLog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client_grpc/ReplicatedLog.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x63lient_grpc/ReplicatedLog.proto\"\x1e\n\x04POST\x12\t\n\x01w\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\x1b\n\x0cPOSTResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x12\n\x03GET\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x1b\n\x0bGETResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\t\"\x0e\n\x0c\x41skHeartBeat\"\x1e\n\tHeartBeat\x12\x11\n\theartbeat\x18\x01 \x01(\x05\"1\n\nHeartBeats\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x03(\t\x12\x12\n\nheartbeats\x18\x02 \x03(\x05\x32\x39\n\x12PostRequestService\x12#\n\x0bPostRequest\x12\x05.POST\x1a\r.POSTResponse25\n\x11GetRequestService\x12 \n\nGetRequest\x12\x04.GET\x1a\x0c.GETResponse2D\n\x13\x41skHeartBeatService\x12-\n\x10HeartBeatRequest\x12\r.AskHeartBeat\x1a\n.HeartBeat2F\n\x14\x41skHeartBeatsService\x12.\n\x10HeartBeatRequest\x12\r.AskHeartBeat\x1a\x0b.HeartBeatsb\x06proto3'
)




_POST = _descriptor.Descriptor(
  name='POST',
  full_name='POST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='w', full_name='POST.w', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='POST.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=35,
  serialized_end=65,
)


_POSTRESPONSE = _descriptor.Descriptor(
  name='POSTResponse',
  full_name='POSTResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='POSTResponse.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=94,
)


_GET = _descriptor.Descriptor(
  name='GET',
  full_name='GET',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='GET.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=96,
  serialized_end=114,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GETResponse',
  full_name='GETResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='GETResponse.data', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=116,
  serialized_end=143,
)


_ASKHEARTBEAT = _descriptor.Descriptor(
  name='AskHeartBeat',
  full_name='AskHeartBeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=145,
  serialized_end=159,
)


_HEARTBEAT = _descriptor.Descriptor(
  name='HeartBeat',
  full_name='HeartBeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heartbeat', full_name='HeartBeat.heartbeat', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=161,
  serialized_end=191,
)


_HEARTBEATS = _descriptor.Descriptor(
  name='HeartBeats',
  full_name='HeartBeats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='HeartBeats.address', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heartbeats', full_name='HeartBeats.heartbeats', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=193,
  serialized_end=242,
)

DESCRIPTOR.message_types_by_name['POST'] = _POST
DESCRIPTOR.message_types_by_name['POSTResponse'] = _POSTRESPONSE
DESCRIPTOR.message_types_by_name['GET'] = _GET
DESCRIPTOR.message_types_by_name['GETResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['AskHeartBeat'] = _ASKHEARTBEAT
DESCRIPTOR.message_types_by_name['HeartBeat'] = _HEARTBEAT
DESCRIPTOR.message_types_by_name['HeartBeats'] = _HEARTBEATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

POST = _reflection.GeneratedProtocolMessageType('POST', (_message.Message,), {
  'DESCRIPTOR' : _POST,
  '__module__' : 'client_grpc.ReplicatedLog_pb2'
  # @@protoc_insertion_point(class_scope:POST)
  })
_sym_db.RegisterMessage(POST)

POSTResponse = _reflection.GeneratedProtocolMessageType('POSTResponse', (_message.Message,), {
  'DESCRIPTOR' : _POSTRESPONSE,
  '__module__' : 'client_grpc.ReplicatedLog_pb2'
  # @@protoc_insertion_point(class_scope:POSTResponse)
  })
_sym_db.RegisterMessage(POSTResponse)

GET = _reflection.GeneratedProtocolMessageType('GET', (_message.Message,), {
  'DESCRIPTOR' : _GET,
  '__module__' : 'client_grpc.ReplicatedLog_pb2'
  # @@protoc_insertion_point(class_scope:GET)
  })
_sym_db.RegisterMessage(GET)

GETResponse = _reflection.GeneratedProtocolMessageType('GETResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'client_grpc.ReplicatedLog_pb2'
  # @@protoc_insertion_point(class_scope:GETResponse)
  })
_sym_db.RegisterMessage(GETResponse)

AskHeartBeat = _reflection.GeneratedProtocolMessageType('AskHeartBeat', (_message.Message,), {
  'DESCRIPTOR' : _ASKHEARTBEAT,
  '__module__' : 'client_grpc.ReplicatedLog_pb2'
  # @@protoc_insertion_point(class_scope:AskHeartBeat)
  })
_sym_db.RegisterMessage(AskHeartBeat)

HeartBeat = _reflection.GeneratedProtocolMessageType('HeartBeat', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEAT,
  '__module__' : 'client_grpc.ReplicatedLog_pb2'
  # @@protoc_insertion_point(class_scope:HeartBeat)
  })
_sym_db.RegisterMessage(HeartBeat)

HeartBeats = _reflection.GeneratedProtocolMessageType('HeartBeats', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATS,
  '__module__' : 'client_grpc.ReplicatedLog_pb2'
  # @@protoc_insertion_point(class_scope:HeartBeats)
  })
_sym_db.RegisterMessage(HeartBeats)



_POSTREQUESTSERVICE = _descriptor.ServiceDescriptor(
  name='PostRequestService',
  full_name='PostRequestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=244,
  serialized_end=301,
  methods=[
  _descriptor.MethodDescriptor(
    name='PostRequest',
    full_name='PostRequestService.PostRequest',
    index=0,
    containing_service=None,
    input_type=_POST,
    output_type=_POSTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POSTREQUESTSERVICE)

DESCRIPTOR.services_by_name['PostRequestService'] = _POSTREQUESTSERVICE


_GETREQUESTSERVICE = _descriptor.ServiceDescriptor(
  name='GetRequestService',
  full_name='GetRequestService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=303,
  serialized_end=356,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRequest',
    full_name='GetRequestService.GetRequest',
    index=0,
    containing_service=None,
    input_type=_GET,
    output_type=_GETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETREQUESTSERVICE)

DESCRIPTOR.services_by_name['GetRequestService'] = _GETREQUESTSERVICE


_ASKHEARTBEATSERVICE = _descriptor.ServiceDescriptor(
  name='AskHeartBeatService',
  full_name='AskHeartBeatService',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=358,
  serialized_end=426,
  methods=[
  _descriptor.MethodDescriptor(
    name='HeartBeatRequest',
    full_name='AskHeartBeatService.HeartBeatRequest',
    index=0,
    containing_service=None,
    input_type=_ASKHEARTBEAT,
    output_type=_HEARTBEAT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ASKHEARTBEATSERVICE)

DESCRIPTOR.services_by_name['AskHeartBeatService'] = _ASKHEARTBEATSERVICE


_ASKHEARTBEATSSERVICE = _descriptor.ServiceDescriptor(
  name='AskHeartBeatsService',
  full_name='AskHeartBeatsService',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=428,
  serialized_end=498,
  methods=[
  _descriptor.MethodDescriptor(
    name='HeartBeatRequest',
    full_name='AskHeartBeatsService.HeartBeatRequest',
    index=0,
    containing_service=None,
    input_type=_ASKHEARTBEAT,
    output_type=_HEARTBEATS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ASKHEARTBEATSSERVICE)

DESCRIPTOR.services_by_name['AskHeartBeatsService'] = _ASKHEARTBEATSSERVICE

# @@protoc_insertion_point(module_scope)
