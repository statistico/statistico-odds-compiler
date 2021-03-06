import pytest
import pandas as pd
from datetime import datetime
from mock import MagicMock, Mock
from compiler.preprocessing.aggregation.goals import GoalsAggregator
from compiler.grpc.proto.fixture_pb2 import Fixture
from compiler.grpc.proto import result_pb2
from compiler.grpc.fixture_client import FixtureClient
from compiler.grpc.result_client import ResultClient
from compiler.grpc.team_stats_client import TeamStatsClient
from compiler.grpc.proto import team_stats_pb2


def test_for_season_data_frame_columns(match_goals):
    value = match_goals.result_client.get_results_for_season.return_value
    value.__iter__.return_value = iter([])

    df = match_goals.for_season(5, datetime.fromisoformat('2019-04-23T18:15:38+00:00'))

    match_goals.result_client.get_results_for_season.assert_called_with(
        season_id=5,
        date_before='2019-04-23T18:15:38+00:00'
    )

    columns = [
        'fixtureID',
        'round',
        'date',
        'season',
        'homeTeam',
        'homeGoals',
        'homeXG',
        'homeShotsTotal',
        'homeShotsOnGoal',
        'awayTeam',
        'awayGoals',
        'awayXG',
        'awayShotsTotal',
        'awayShotsOnGoal',
    ]

    df_columns = df.columns

    assert (df_columns == columns).all()


def test_for_season_converts_result_object_into_data_frame_row(match_goals, result, team_stats_response):
    value = match_goals.result_client.get_results_for_season.return_value
    value.__iter__.return_value = iter([result])

    match_goals.team_stats_client.get_team_stats_for_fixture.return_value = team_stats_response

    df = match_goals.for_season(5, datetime.fromisoformat('2019-04-23T18:15:38+00:00'))

    match_goals.result_client.get_results_for_season.assert_called_with(
        season_id=5,
        date_before='2019-04-23T18:15:38+00:00'
    )

    expected = [
        66,
        '4',
        pd.Timestamp('2019-04-23 18:15:38'),
        '2018/19',
        'West Ham United',
        2,
        1.25,
        34,
        12,
        'Tottenham Hotspur',
        2,
        1,
        34,
        12,
    ]

    row = df.iloc[0, :].values.tolist()

    assert row == expected


def test_for_season_populates_multiple_rows_of_data_for_multiple_results(match_goals, result):
    value = match_goals.result_client.get_results_for_season.return_value
    value.__iter__.return_value = iter([result, result, result])

    df = match_goals.for_season(5, datetime.fromisoformat('2019-04-23T18:15:38+00:00'))

    match_goals.result_client.get_results_for_season.assert_called_with(
        season_id=5,
        date_before='2019-04-23T18:15:38+00:00'
    )

    assert df.shape == (3, 14)


def test_for_fixture_data_frame_columns(match_goals, fixture):
    match_goals.fixture_client.get_fixture_by_id.return_value = fixture

    fixture, df = match_goals.for_fixture(fixture_id=66)

    match_goals.fixture_client.get_fixture_by_id.assert_called_with(fixture_id=66)

    columns = [
        'fixtureID',
        'round',
        'date',
        'season',
        'homeTeam',
        'homeGoals',
        'homeXG',
        'homeShotsTotal',
        'homeShotsOnGoal',
        'awayTeam',
        'awayGoals',
        'awayXG',
        'awayShotsTotal',
        'awayShotsOnGoal',
    ]

    df_columns = df.columns

    assert (df_columns == columns).all()
    assert df.shape == (1, 14)


def test_for_fixture_returns_data_frame_of_collated_fixture_data(match_goals, fixture):
    match_goals.fixture_client.get_fixture_by_id.return_value = fixture

    fixture, df = match_goals.for_fixture(fixture_id=66)

    match_goals.fixture_client.get_fixture_by_id.assert_called_with(fixture_id=66)

    row = df.iloc[0, :]

    assert row['fixtureID'] == 66
    assert row['round'] == '4'
    assert row['date'] == pd.Timestamp('2019-04-23T18:15:38')
    assert row['season'] == '2018/19'
    assert row['homeTeam'] == 'West Ham United'
    assert row['awayTeam'] == 'Tottenham Hotspur'


def test_for_fixture_raises_exception_if_unable_to_retrieve_fixture(match_goals):
    match_goals.fixture_client.get_fixture_by_id.side_effect = Exception()

    with pytest.raises(Exception):
        match_goals.for_fixture(fixture_id=66)


def test_for_fixture_returns_fixture_and_data_frame(match_goals, fixture):
    match_goals.fixture_client.get_fixture_by_id.return_value = fixture

    fixture, df = match_goals.for_fixture(fixture_id=66)

    match_goals.fixture_client.get_fixture_by_id.assert_called_with(fixture_id=66)

    assert fixture.id == 66
    assert fixture.season.name == '2018/19'
    assert fixture.round.name == '4'
    assert fixture.season.id == 39910
    assert fixture.season.is_current.value == True
    assert fixture.date_time.utc == 1556043338
    assert fixture.home_team.name == 'West Ham United'
    assert fixture.away_team.name == 'Tottenham Hotspur'


@pytest.fixture()
def match_goals():
    fixture_client = MagicMock(spec=FixtureClient)
    result_client = MagicMock(spec=ResultClient)
    team_stats_client = Mock(spec=TeamStatsClient)

    aggregator = GoalsAggregator(
        fixture_client=fixture_client,
        result_client=result_client,
        team_stats_client=team_stats_client
    )

    return aggregator


@pytest.fixture()
def result():
    result = result_pb2.Result()
    result.id = 66

    result.season.name = '2018/19'

    result.round.name = '4'

    result.season.id = 39910
    result.season.is_current.value = True

    result.date_time.utc = 1556043338

    result.home_team.id = 7901
    result.home_team.name = 'West Ham United'
    result.away_team.id = 496
    result.away_team.name = 'Tottenham Hotspur'
    result.stats.home_formation.value = '4-4-2'
    result.stats.away_formation.value = '5-3-1-1'
    result.stats.home_score.value = 2
    result.stats.away_score.value = 2

    return result


@pytest.fixture()
def home_past_result():
    result = result_pb2.Result()
    result.date_time.utc = 1555761600
    result.home_team.id = 7901
    result.home_team.name = 'West Ham United'
    result.away_team.id = 496
    result.away_team.name = 'Tottenham Hotspur'
    result.stats.home_score.value = 5
    result.stats.away_score.value = 2
    return result


@pytest.fixture()
def away_past_result():
    result = result_pb2.Result()
    result.date_time.utc = 1555549200
    result.home_team.id = 496
    result.home_team.name = 'Manchester City'
    result.way_team.id = 7901
    result.away_team.name = 'Liverpool'
    result.stats.home_score.value = 1
    result.stats.away_score.value = 3
    return result


@pytest.fixture
def team_stats_response():
    response = team_stats_pb2.TeamStatsResponse()

    response.home_team.shots_total.value = 34
    response.home_team.shots_on_goal.value = 12

    response.away_team.shots_total.value = 34
    response.away_team.shots_on_goal.value = 12

    response.team_xg.home.value = 1.25
    response.team_xg.away.value = 1

    return response


@pytest.fixture()
def fixture():
    fixture = Fixture()
    fixture.id = 66

    fixture.season.name = '2018/19'

    fixture.round.name = '4'

    fixture.season.id = 39910
    fixture.season.is_current.value = True

    fixture.date_time.utc = 1556043338

    fixture.home_team.id = 7901
    fixture.home_team.name = 'West Ham United'
    fixture.away_team.id = 496
    fixture.away_team.name = 'Tottenham Hotspur'

    return fixture
