from .abstract_game_manager import AbstractGameManager

from .fixed_size_queue import FixedSizeQueue
from .fixed_size_set import FixedSizeSet
from .region import Region

class SimpleGameManager(AbstractGameManager):
    
    def __init__(self,
                 players_max,
                 regions_max):

        super().__init__(players_max, regions_max)

    def most_effective_region_for_player(self, player):
        best_region = None
        base_regions = sorted([region for region in self._regions if region.can_add_player(player)], key=lambda region: region.in_queue)
        can_add_room = list(filter(lambda region: region.can_create_room(), base_regions))
        if base_regions:
            last_to_room = list(filter(lambda region: region.to_create_room() == 1, can_add_room))
            if last_to_room: # one player to creating a new room
                best_region = last_to_room[0]
            else:
                most_free_places = max(base_regions, key=lambda region: region.player_free_places())
                if most_free_places.player_free_places(): # empty place in a room
                    best_region =  most_free_places
                else:
                    best_region = base_regions[0]
        return best_region

    def most_effective_region_for_room(self, room_name, player):
        base_regions = [region for region in self._regions if region.can_add_player(player) and region.can_create_room(room_name)] 
        sorted_base_regions = sorted(base_regions, key=lambda region: region.room_free_places())
        if base_regions:
            return base_regions[0]






