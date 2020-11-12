# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compiler/grpc/proto/event.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from compiler.grpc.proto import requests_pb2 as compiler_dot_grpc_dot_proto_dot_requests__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='compiler/grpc/proto/event.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x63ompiler/grpc/proto/event.proto\x12\x05proto\x1a\"compiler/grpc/proto/requests.proto\x1a\x1egoogle/protobuf/wrappers.proto\"m\n\x15\x46ixtureEventsResponse\x12\x12\n\nfixture_id\x18\x01 \x01(\x04\x12\x1f\n\x05\x63\x61rds\x18\x02 \x03(\x0b\x32\x10.proto.CardEvent\x12\x1f\n\x05goals\x18\x03 \x03(\x0b\x32\x10.proto.GoalEvent\"Y\n\tCardEvent\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07team_id\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x11\n\tplayer_id\x18\x04 \x01(\x04\x12\x0e\n\x06minute\x18\x05 \x01(\r\"\x92\x01\n\tGoalEvent\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07team_id\x18\x02 \x01(\x04\x12\x11\n\tplayer_id\x18\x03 \x01(\x04\x12\x36\n\x10player_assist_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x0e\n\x06minute\x18\x05 \x01(\r\x12\r\n\x05score\x18\x06 \x01(\t2V\n\x0c\x45ventService\x12\x46\n\rFixtureEvents\x12\x15.proto.FixtureRequest\x1a\x1c.proto.FixtureEventsResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[compiler_dot_grpc_dot_proto_dot_requests__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_FIXTUREEVENTSRESPONSE = _descriptor.Descriptor(
  name='FixtureEventsResponse',
  full_name='proto.FixtureEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixture_id', full_name='proto.FixtureEventsResponse.fixture_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cards', full_name='proto.FixtureEventsResponse.cards', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='goals', full_name='proto.FixtureEventsResponse.goals', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=110,
  serialized_end=219,
)


_CARDEVENT = _descriptor.Descriptor(
  name='CardEvent',
  full_name='proto.CardEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.CardEvent.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='team_id', full_name='proto.CardEvent.team_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.CardEvent.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='proto.CardEvent.player_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minute', full_name='proto.CardEvent.minute', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=221,
  serialized_end=310,
)


_GOALEVENT = _descriptor.Descriptor(
  name='GoalEvent',
  full_name='proto.GoalEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.GoalEvent.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='team_id', full_name='proto.GoalEvent.team_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='proto.GoalEvent.player_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_assist_id', full_name='proto.GoalEvent.player_assist_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minute', full_name='proto.GoalEvent.minute', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='proto.GoalEvent.score', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=313,
  serialized_end=459,
)

_FIXTUREEVENTSRESPONSE.fields_by_name['cards'].message_type = _CARDEVENT
_FIXTUREEVENTSRESPONSE.fields_by_name['goals'].message_type = _GOALEVENT
_GOALEVENT.fields_by_name['player_assist_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
DESCRIPTOR.message_types_by_name['FixtureEventsResponse'] = _FIXTUREEVENTSRESPONSE
DESCRIPTOR.message_types_by_name['CardEvent'] = _CARDEVENT
DESCRIPTOR.message_types_by_name['GoalEvent'] = _GOALEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FixtureEventsResponse = _reflection.GeneratedProtocolMessageType('FixtureEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _FIXTUREEVENTSRESPONSE,
  '__module__' : 'compiler.grpc.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:proto.FixtureEventsResponse)
  })
_sym_db.RegisterMessage(FixtureEventsResponse)

CardEvent = _reflection.GeneratedProtocolMessageType('CardEvent', (_message.Message,), {
  'DESCRIPTOR' : _CARDEVENT,
  '__module__' : 'compiler.grpc.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:proto.CardEvent)
  })
_sym_db.RegisterMessage(CardEvent)

GoalEvent = _reflection.GeneratedProtocolMessageType('GoalEvent', (_message.Message,), {
  'DESCRIPTOR' : _GOALEVENT,
  '__module__' : 'compiler.grpc.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:proto.GoalEvent)
  })
_sym_db.RegisterMessage(GoalEvent)



_EVENTSERVICE = _descriptor.ServiceDescriptor(
  name='EventService',
  full_name='proto.EventService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=461,
  serialized_end=547,
  methods=[
  _descriptor.MethodDescriptor(
    name='FixtureEvents',
    full_name='proto.EventService.FixtureEvents',
    index=0,
    containing_service=None,
    input_type=compiler_dot_grpc_dot_proto_dot_requests__pb2._FIXTUREREQUEST,
    output_type=_FIXTUREEVENTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTSERVICE)

DESCRIPTOR.services_by_name['EventService'] = _EVENTSERVICE

# @@protoc_insertion_point(module_scope)