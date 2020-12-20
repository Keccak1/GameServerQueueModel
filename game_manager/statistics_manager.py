from .game_element import GameElement
from .player import Player
from collections import namedtuple
from datetime import datetime
import time


class PlayerStatistics(GameElement):
    def __init__(self, player):
        self._player = player
        self._start = datetime.now()
        self._stop = None

    @property
    def name(self):
        return self._player.name

    @property
    def stop(self):
        return self._stop

    def done(self):
        self._stop = datetime.now()

    def to_dict(self):
        return {"name": self.name,
                "start": self._start,
                "stop:": self._stop,
                "seconds": (self._stop - self._start).total_seconds()}


class StatisticsManager(GameElement):
    def __init__(self):
        self._player_statistics = []

    def player_start(self, player):
        self._player_statistics.append(PlayerStatistics(player))

    def player_stop(self, player_name):
        player = self.find_player(player_name)
        if player:
            player.done()
            return player

    def to_dict(self):
        return {"players": [player_stat.to_dict() for player_stat in self._player_statistics if player_stat.stop]}

    def find_player(self, player_name):
        try:
            result = list(filter(lambda player_stat: player_name ==
                                 player_stat.name and not player_stat.stop, self._player_statistics))
            if result:
                return result[0]
        except ValueError:
            pass
