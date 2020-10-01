# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compiler/grpc/proto/stats/team/stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from compiler.grpc.proto.requests import requests_pb2 as compiler_dot_grpc_dot_proto_dot_requests_dot_requests__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='compiler/grpc/proto/stats/team/stats.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*compiler/grpc/proto/stats/team/stats.proto\x12\x05proto\x1a+compiler/grpc/proto/requests/requests.proto\x1a\x1egoogle/protobuf/wrappers.proto\"}\n\x11TeamStatsResponse\x12#\n\thome_team\x18\x01 \x01(\x0b\x32\x10.proto.TeamStats\x12#\n\taway_team\x18\x02 \x01(\x0b\x32\x10.proto.TeamStats\x12\x1e\n\x07team_xg\x18\x03 \x01(\x0b\x32\r.proto.TeamXG\"Y\n\x08TeamStat\x12\x12\n\nfixture_id\x18\x01 \x01(\x04\x12\x0c\n\x04stat\x18\x02 \x01(\t\x12+\n\x05value\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"\xc1\t\n\tTeamStats\x12\x0f\n\x07team_id\x18\x01 \x01(\x04\x12\x31\n\x0bshots_total\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x33\n\rshots_on_goal\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x34\n\x0eshots_off_goal\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x33\n\rshots_blocked\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x36\n\x10shots_inside_box\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x37\n\x11shots_outside_box\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x32\n\x0cpasses_total\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x35\n\x0fpasses_accuracy\x18\t \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x37\n\x11passes_percentage\x18\n \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x33\n\rattacks_total\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x37\n\x11\x61ttacks_dangerous\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12+\n\x05\x66ouls\x18\r \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12-\n\x07\x63orners\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12.\n\x08offsides\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x30\n\npossession\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x32\n\x0cyellow_cards\x18\x11 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12/\n\tred_cards\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12+\n\x05saves\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x33\n\rsubstitutions\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x30\n\ngoal_kicks\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x33\n\rgoal_attempts\x18\x16 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x30\n\nfree_kicks\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12/\n\tthrow_ins\x18\x18 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"^\n\x06TeamXG\x12)\n\x04home\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12)\n\x04\x61way\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue2\x9e\x01\n\x10TeamStatsService\x12K\n\x16GetTeamStatsForFixture\x12\x15.proto.FixtureRequest\x1a\x18.proto.TeamStatsResponse\"\x00\x12=\n\x0eGetStatForTeam\x12\x16.proto.TeamStatRequest\x1a\x0f.proto.TeamStat\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[compiler_dot_grpc_dot_proto_dot_requests_dot_requests__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_TEAMSTATSRESPONSE = _descriptor.Descriptor(
  name='TeamStatsResponse',
  full_name='proto.TeamStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home_team', full_name='proto.TeamStatsResponse.home_team', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away_team', full_name='proto.TeamStatsResponse.away_team', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team_xg', full_name='proto.TeamStatsResponse.team_xg', index=2,
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
  serialized_start=130,
  serialized_end=255,
)


_TEAMSTAT = _descriptor.Descriptor(
  name='TeamStat',
  full_name='proto.TeamStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixture_id', full_name='proto.TeamStat.fixture_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stat', full_name='proto.TeamStat.stat', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.TeamStat.value', index=2,
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
  serialized_start=257,
  serialized_end=346,
)


_TEAMSTATS = _descriptor.Descriptor(
  name='TeamStats',
  full_name='proto.TeamStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_id', full_name='proto.TeamStats.team_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shots_total', full_name='proto.TeamStats.shots_total', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shots_on_goal', full_name='proto.TeamStats.shots_on_goal', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shots_off_goal', full_name='proto.TeamStats.shots_off_goal', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shots_blocked', full_name='proto.TeamStats.shots_blocked', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shots_inside_box', full_name='proto.TeamStats.shots_inside_box', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shots_outside_box', full_name='proto.TeamStats.shots_outside_box', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passes_total', full_name='proto.TeamStats.passes_total', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passes_accuracy', full_name='proto.TeamStats.passes_accuracy', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passes_percentage', full_name='proto.TeamStats.passes_percentage', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attacks_total', full_name='proto.TeamStats.attacks_total', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attacks_dangerous', full_name='proto.TeamStats.attacks_dangerous', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fouls', full_name='proto.TeamStats.fouls', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='corners', full_name='proto.TeamStats.corners', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offsides', full_name='proto.TeamStats.offsides', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='possession', full_name='proto.TeamStats.possession', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yellow_cards', full_name='proto.TeamStats.yellow_cards', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='red_cards', full_name='proto.TeamStats.red_cards', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saves', full_name='proto.TeamStats.saves', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='substitutions', full_name='proto.TeamStats.substitutions', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goal_kicks', full_name='proto.TeamStats.goal_kicks', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goal_attempts', full_name='proto.TeamStats.goal_attempts', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_kicks', full_name='proto.TeamStats.free_kicks', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='throw_ins', full_name='proto.TeamStats.throw_ins', index=23,
      number=24, type=11, cpp_type=10, label=1,
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
  serialized_start=349,
  serialized_end=1566,
)


_TEAMXG = _descriptor.Descriptor(
  name='TeamXG',
  full_name='proto.TeamXG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home', full_name='proto.TeamXG.home', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away', full_name='proto.TeamXG.away', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1568,
  serialized_end=1662,
)

_TEAMSTATSRESPONSE.fields_by_name['home_team'].message_type = _TEAMSTATS
_TEAMSTATSRESPONSE.fields_by_name['away_team'].message_type = _TEAMSTATS
_TEAMSTATSRESPONSE.fields_by_name['team_xg'].message_type = _TEAMXG
_TEAMSTAT.fields_by_name['value'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['shots_total'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['shots_on_goal'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['shots_off_goal'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['shots_blocked'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['shots_inside_box'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['shots_outside_box'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['passes_total'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['passes_accuracy'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['passes_percentage'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['attacks_total'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['attacks_dangerous'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['fouls'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['corners'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['offsides'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['possession'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['yellow_cards'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['red_cards'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['saves'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['substitutions'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['goal_kicks'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['goal_attempts'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['free_kicks'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMSTATS.fields_by_name['throw_ins'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TEAMXG.fields_by_name['home'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_TEAMXG.fields_by_name['away'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
DESCRIPTOR.message_types_by_name['TeamStatsResponse'] = _TEAMSTATSRESPONSE
DESCRIPTOR.message_types_by_name['TeamStat'] = _TEAMSTAT
DESCRIPTOR.message_types_by_name['TeamStats'] = _TEAMSTATS
DESCRIPTOR.message_types_by_name['TeamXG'] = _TEAMXG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeamStatsResponse = _reflection.GeneratedProtocolMessageType('TeamStatsResponse', (_message.Message,), dict(
  DESCRIPTOR = _TEAMSTATSRESPONSE,
  __module__ = 'compiler.grpc.proto.stats.team.stats_pb2'
  # @@protoc_insertion_point(class_scope:proto.TeamStatsResponse)
  ))
_sym_db.RegisterMessage(TeamStatsResponse)

TeamStat = _reflection.GeneratedProtocolMessageType('TeamStat', (_message.Message,), dict(
  DESCRIPTOR = _TEAMSTAT,
  __module__ = 'compiler.grpc.proto.stats.team.stats_pb2'
  # @@protoc_insertion_point(class_scope:proto.TeamStat)
  ))
_sym_db.RegisterMessage(TeamStat)

TeamStats = _reflection.GeneratedProtocolMessageType('TeamStats', (_message.Message,), dict(
  DESCRIPTOR = _TEAMSTATS,
  __module__ = 'compiler.grpc.proto.stats.team.stats_pb2'
  # @@protoc_insertion_point(class_scope:proto.TeamStats)
  ))
_sym_db.RegisterMessage(TeamStats)

TeamXG = _reflection.GeneratedProtocolMessageType('TeamXG', (_message.Message,), dict(
  DESCRIPTOR = _TEAMXG,
  __module__ = 'compiler.grpc.proto.stats.team.stats_pb2'
  # @@protoc_insertion_point(class_scope:proto.TeamXG)
  ))
_sym_db.RegisterMessage(TeamXG)



_TEAMSTATSSERVICE = _descriptor.ServiceDescriptor(
  name='TeamStatsService',
  full_name='proto.TeamStatsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1665,
  serialized_end=1823,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTeamStatsForFixture',
    full_name='proto.TeamStatsService.GetTeamStatsForFixture',
    index=0,
    containing_service=None,
    input_type=compiler_dot_grpc_dot_proto_dot_requests_dot_requests__pb2._FIXTUREREQUEST,
    output_type=_TEAMSTATSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatForTeam',
    full_name='proto.TeamStatsService.GetStatForTeam',
    index=1,
    containing_service=None,
    input_type=compiler_dot_grpc_dot_proto_dot_requests_dot_requests__pb2._TEAMSTATREQUEST,
    output_type=_TEAMSTAT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEAMSTATSSERVICE)

DESCRIPTOR.services_by_name['TeamStatsService'] = _TEAMSTATSSERVICE

# @@protoc_insertion_point(module_scope)
