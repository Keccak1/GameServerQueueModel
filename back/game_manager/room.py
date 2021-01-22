from .fixed_size_set import FixedSizeSet
from .player import Player
from .game_element import GameElement


class Room(GameElement):

    def __init__(self, name, size):
        super().__init__()
        self._name = name
        self._players = FixedSizeSet(maxlen=size)

    def __repr__(self):
        return f"Name: {self._name}, players: {str(self._players)}"

    @property
    def name(self):
        return self._name

    @property
    def players_amount(self):
        return self._players.size

    @property
    def maxlen(self):
        return self._players.maxlen

    def to_dict(self):
        return {"name": self.name, "size": self._players.size, "players": [player.to_dict() for player in self._players]}

    def has_player(self, player_name):
        return self._players.find_by_lambda(
            lambda player: player.name == player_name)

    def player_names(self):
        return set([player.name for player in self._players])

    def free_places(self):
        return self._players.free_places()

    def empty(self):
        return self._players.empty()

    def full(self):
        return self._players.full()

    def can_add_player(self, player_name=None):
        ret = not self.full()
        if player_name:
            ret &= not self._players.find_by_lambda(
                lambda player: player.name == player_name)
        return ret

    def remove_player(self, name):
        return self.remove_players([name])

    def remove_players(self, names):
        return self._players.remove_lambda(lambda room: room.name in names)

    def add_player(self, player):
        ret = self.can_add_player(player.name)
        if ret:
            return self._players.add(player)
        return ret

    def add_players(self, players):
        return self._players.add_range(players)
