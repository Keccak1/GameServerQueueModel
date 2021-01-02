import random

from .abstract_game_event import AbstractGameEvent


class RemoveRoomGameEvent(AbstractGameEvent):
    def __init__(self):
        pass

    def trigger(self, **kwargs):
        name = random.choice(self._manager.player_names())
        return self._manager.remove_player(name)

    def can_trigger(self, **kwargs):
        return len(self._manager.player_names())
