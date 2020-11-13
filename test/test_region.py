import unittest

from game_manager.region import Region 
from game_manager.room import Room 
from game_manager.player import Player 

class RegionTestCase(unittest.TestCase):
    def setUp(self):
        self._region = Region(name="EUROPE",
        max_players=100,
        room_size = 10,
        queue_size=20)


    def test_regions(self):
        self.assertTrue(self._region.can_create_room())
        self.assertFalse(self._region.has_player_name("dummy"))
        self.assertFalse(self._region.player_in_queue("dummy"))
        self.assertFalse(self._region.player_in_room("dummy"))
        self.assertFalse(self._region.player_in_room("Room"))
        self.assertTrue(self._region.can_create_room("Room"))
        self.assertFalse(self._region.add_room("Room", Player(name="dummy", regions=["ASIA"])))
        self.assertTrue(self._region.add_room("Room", Player(name="dummy", regions=["EUROPE"])))
        self.assertEqual(self._region.rooms_amount, 1)
        self.assertEqual(self._region.in_queue, 0)
        self.assertTrue(self._region.add_player(Player(name="Tomek", regions=["EUROPE"])))
        self.assertFalse(self._region.add_player(Player(name="Zosia", regions=["ASIA"])))
        self.assertEqual(self._region.player_free_places(), 8)
        self.assertEqual(self._region.room_free_places(), 9)
        for i in range(8):
            self._region.add_player(Player(name=str(i), regions=["EUROPE"]))
        self.assertEqual(self._region.player_free_places(), 0)
        self._region.add_player(Player(name="QueuePlayer", regions=["EUROPE"]))
        self.assertTrue(self._region.player_in_queue("QueuePlayer"))
        self.assertTrue(self._region.add_room("Room2", Player(name="Marcin", regions=["EUROPE"])))
        self.assertFalse(self._region.player_in_queue("QueuePlayer"))
        self.assertEqual(self._region.room_free_places(), 8)
        self.assertEqual(self._region.player_free_places(), 8)
        for i in range(self._region.player_free_places() +self._region._minimum_players_to_room):  
            self._region.add_player(Player(name=str(i)+str(i), regions=["EUROPE"]))
        self.assertEqual(self._region.in_queue, 0)