from datetime import datetime
from compiler.data.repository.redis import RedisRepository
from compiler.data.aggregator.match_goals import MatchGoals
from compiler.framework import config


class DataHandler:
    def __init__(
        self,
        configuration: config,
        repository: RedisRepository,
        aggregator: MatchGoals
    ):
        self._configuration = configuration
        self._repository = repository
        self._aggregator = aggregator

    def store_match_goals_data_for_supported_competitions(self, date_before: datetime):
        """
        Loop through supported competitions and
            a) parse data into dataframe
            b) store dataframe to persistence layer
        """
        competitions = self._configuration.SUPPORTED_COMPETITIONS

        for i, competition in competitions.items():
            competition_id = competition['id']
            seasons = competition['seasons']

            for season in seasons:
                df = self._aggregator.for_season(
                    season_id=season['id'],
                    date_before=date_before
                )

                filename = "competition:" \
                           + str(competition_id) \
                           + ':season:' \
                           + str(season['id'])

                self._repository.save_data_frame(key=filename, df=df)