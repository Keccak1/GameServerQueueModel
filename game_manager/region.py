from .fixed_size_queue import FixedSizeQueue
from .fixed_size_set import FixedSizeSet
from .player import Player
from .util import to_iterarable
from .room import Room
from .game_element import GameElement

from functools import reduce

class Region(GameElement):

    def __init__(self,
                 name,
                 max_players,
                 room_size,
                 queue_size,
                 minimum_players_to_room=None,
                 default_name="Room"):
                     
        super().__init__()
        self._name = name
        self._max_players = max_players
        self._room_size = room_size
        rooms_amount = int(max_players/room_size)
        self._rooms = FixedSizeSet(maxlen=rooms_amount)
        if minimum_players_to_room is None:
            minimum_players_to_room = room_size/2
        self._minimum_players_to_room = int(minimum_players_to_room)
        if max_players%room_size:
            queue_size+=max_players - rooms_amount * room_size
        self._players = FixedSizeQueue(maxlen=queue_size)
        self._default_name="Room"
        self._room_counter = 0

    @property
    def name(self):
        return self._name

    @property
    def queue(self):
        return self._players

    @property
    def rooms_amount(self):
        return self._rooms.size

    @property
    def in_queue(self):
        return self._players.size

    @property
    def room_size(self):
        return self._rooms.size()

    def to_dict(self):
        return {"name": self._name, 
        "max_players": self._max_players,
        "room_size": self._room_size,
        "queue": [player.to_dict() for player in self._players],
        "rooms": [room.to_dict() for room in self._rooms] }

    def add_player(self, player):
        ret = None
        if not self.has_player(player) and self.same_region(player):
            free_room = self._get_free_room(player.name)
            if free_room:
                ret = free_room.add_player(player)
            elif (self._players.size+1 >= self._minimum_players_to_room) and self.can_create_room():
                name = self._get_next_room_name()
                ret = self.add_room(name, player)
            elif self._players.can_push():
                ret = self._players.push(player)
        return ret

    def add_room(self, room_name, player):
        new_room = None
        if self.can_add_player(player) and self.can_create_room(room_name):
            new_room = Room(room_name, self._room_size)
            new_room.add_player(player)
            self._rooms.add(new_room)
            self._update_room(new_room)
        return new_room

    def can_add_player(self, player):
        basic = not self.has_player_name(player.name) and self.same_region(player)
        has_place = self.player_free_places() != 0 or self._players.free_places() !=0
        return basic and has_place

    def same_region(self, player):
        return self.name in player.regions

    def has_player(self, player):
        return self.player_in_queue(player.name) or self.player_in_room(player.name)

    def has_player_name(self, player_name):
        return self.player_in_queue(player_name) or self.player_in_room(player_name)

    def player_in_queue(self, player_name):
        return bool(self._players.find_by_lambda(lambda player: player.name == player_name))

    def player_in_room(self, player_name):
        for room in self._rooms:
            if room.has_player(player_name):
                return True
        return False

    def room_exists(self, room_name):
        return room_name in [room.name for room in self._rooms]

    def can_create_room(self, room_name = None):
        ret = not self._rooms.full()
        if room_name:
            ret&= not self.room_exists(room_name)
        return ret

    def room_size(self):
        return self._rooms.size()

    def room_free_places(self, room_name=None):
        ret = 0
        if not room_name or not self.room_exists(room_name):
                ret = self._rooms.free_places()
        return ret

    def to_create_room(self):
        return self._minimum_players_to_room - self._players.size 
        
    def player_free_places(self, player_name=None):
        ret = 0
        if (not player_name or not self.has_player_name(player_name)) and not self._rooms.empty():
            ret = reduce(lambda places_sum, new_places: places_sum+new_places,[room.free_places() for room in self._rooms])
        return ret
    
    def player_names(self):
        return reduce(lambda current_names, new_names: current_names.update(new_names),
                      [room.player_names() for room in self._rooms])

    def room_names(self):
        return set([room.name for room in self._rooms])

    def remove_player(self, player):
        return self.remove_player_by_name(player.name)

    def remove_player_by_name(self, player_name):
        ret = self._remove_from_rooms(player_name, True)
        if not ret:
            ret = self._remove_from_queue(player_name)
        return ret
    
    def _update_room(self, room):
        in_queue, free_places =self._players.size, room.free_places()
        new_players_amount = min(in_queue,free_places)
        for _ in range(new_players_amount):
            from_queue = self._players.pop()
            room.add_player(from_queue)
        
        if room.empty():
            self._rooms.remove(room)

    def _get_free_room(self, player_name=None):
        for room in self._rooms:
            if room.can_add_player(player_name):
                return  room

    def _get_next_room_name(self):
        next_name = self._default_name + str(self._room_counter)

        while self.room_exists(next_name):
            self._room_counter+=1
            next_name = self._default_name + str(self._room_counter)

        return next_name
        
    def _remove_from_queue(self, player_name):
        return self._players.remove_lambda(lambda player: player.name == player_name)

    def _remove_from_rooms(self, player_name, update=False):
        ret, to_update = None, None
        for room in self._rooms:
            if room.has_player(player_name):
                room.remove_player(player_name)
                ret, to_update = True, room

        if to_update:
            self._update_room(to_update)
        
        return ret