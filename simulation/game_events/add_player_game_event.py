import uuid
import random

from .abstract_game_event import AbstractGameEvent
from ...game_manager.player import Player


class AddPlayerGameEvent(AbstractGameEvent):
    def __init__(self, manager, **kwargs):
        super().__init__(manager, kwargs)

    def trigger(self, **kwargs):
        regions = self._get_regions()
        name = self._get_name()
        return self._manager.add_player(Player(name, regions))

    def _get_regions(self):
        regions = self._manager.region_names()
        regions_size = random.randint(1, len(region))
        return random.sample(regions, regions_size)

    def _get_name(self):
        return uuid.uuid4().hex[:8].upper()

    def can_trigger(self, **kwargs):
        return len(self._manager.region_names)
