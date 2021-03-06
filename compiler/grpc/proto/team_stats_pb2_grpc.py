# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from compiler.grpc.proto import requests_pb2 as compiler_dot_grpc_dot_proto_dot_requests__pb2
from compiler.grpc.proto import team_stats_pb2 as compiler_dot_grpc_dot_proto_dot_team__stats__pb2


class TeamStatsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTeamStatsForFixture = channel.unary_unary(
                '/proto.TeamStatsService/GetTeamStatsForFixture',
                request_serializer=compiler_dot_grpc_dot_proto_dot_requests__pb2.FixtureRequest.SerializeToString,
                response_deserializer=compiler_dot_grpc_dot_proto_dot_team__stats__pb2.TeamStatsResponse.FromString,
                )
        self.GetStatForTeam = channel.unary_stream(
                '/proto.TeamStatsService/GetStatForTeam',
                request_serializer=compiler_dot_grpc_dot_proto_dot_requests__pb2.TeamStatRequest.SerializeToString,
                response_deserializer=compiler_dot_grpc_dot_proto_dot_team__stats__pb2.TeamStat.FromString,
                )


class TeamStatsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTeamStatsForFixture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatForTeam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TeamStatsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTeamStatsForFixture': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTeamStatsForFixture,
                    request_deserializer=compiler_dot_grpc_dot_proto_dot_requests__pb2.FixtureRequest.FromString,
                    response_serializer=compiler_dot_grpc_dot_proto_dot_team__stats__pb2.TeamStatsResponse.SerializeToString,
            ),
            'GetStatForTeam': grpc.unary_stream_rpc_method_handler(
                    servicer.GetStatForTeam,
                    request_deserializer=compiler_dot_grpc_dot_proto_dot_requests__pb2.TeamStatRequest.FromString,
                    response_serializer=compiler_dot_grpc_dot_proto_dot_team__stats__pb2.TeamStat.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.TeamStatsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TeamStatsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTeamStatsForFixture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TeamStatsService/GetTeamStatsForFixture',
            compiler_dot_grpc_dot_proto_dot_requests__pb2.FixtureRequest.SerializeToString,
            compiler_dot_grpc_dot_proto_dot_team__stats__pb2.TeamStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatForTeam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.TeamStatsService/GetStatForTeam',
            compiler_dot_grpc_dot_proto_dot_requests__pb2.TeamStatRequest.SerializeToString,
            compiler_dot_grpc_dot_proto_dot_team__stats__pb2.TeamStat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
