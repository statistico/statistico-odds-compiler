from compiler.grpc.proto.compiler import compiler_pb2_grpc, compiler_pb2
from compiler.grpc.fixture_client import FixtureClient
from compiler.data.handling.data_handler import DataHandler
from compiler.model.match_goals import train_glm_model, get_over_under_odds


class OddsCompilerServiceServicer(compiler_pb2_grpc.OddsCompilerServiceServicer):
    def __init__(self, fixture_client: FixtureClient, handler: DataHandler):
        self.__fixture_client = fixture_client
        self.__handler = handler

    def GetOverUnderGoalsForFixture(self, request, context):
        fixture = self.__fixture_client.get_fixture_by_id(fixture_id=request.fixture_id)

        fix_data = self.__handler.get_match_goals_data_for_fixture(fixture_id=fixture.id)

        train_data = self.__handler.get_stored_match_goals_data_for_competition(
            competition_id=fixture.competition.id
        )

        model = train_glm_model(features=train_data)

        odds = get_over_under_odds(model=model, fixture=fix_data.to_dict('records')[0])

        response = compiler_pb2.OverUnderGoalsResponse(
            fixture_id=fixture.id,
            under=odds.get_under_decimal_odds(),
            over=odds.get_over_decimal_odds()
        )

        return response