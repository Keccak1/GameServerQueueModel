import uuid

from .add_player_game_event import AddPlayerGameEvent
from ...game_manager.player import Player
from ...game_manager.room import Room


class AddRoomGameEvent(AddPlayerGameEvent):
    def __init__(self, manager, **kwargs):
        super().__init__(manager, kwargs)

    def trigger(self, **kwargs):
        name = self._get_name()
        regions = self._get_regions()
        room_name = self._get_room_name()
        return self._manager.add_room(Player(name, regions), room_name)

    def _get_room_name(self, **kwargs):
        return uuid.uuid4().hex[:8].upper()
