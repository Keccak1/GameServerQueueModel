import unittest

from game_manager.room import Room 
from game_manager.player import Player 

class RoomTestCase(unittest.TestCase):
    def setUp(self):
        self.room = Room(name="test_room", size=4)

    def test_base(self):
        self.assertTrue(self.room.empty())
        self.assertTrue(self.room.can_add_player())
        self.assertFalse(self.room.full())
        self.assertEqual(self.room.players_amount, 0)
        self.assertTrue(self.room.can_add_player("Tomek"))
        self.assertTrue(self.room.add_player(Player(name="Tomek", regions=["EU"])))
        self.assertFalse(self.room.can_add_player("Tomek"))
        self.assertFalse(self.room.add_player(Player(name="Tomek", regions=["EU"])))
        self.assertTrue(self.room.remove_player("Tomek"))
        self.assertTrue(self.room.add_player(Player(name="Tomek", regions=["EU"])))
        self.assertTrue(self.room.add_player(Player(name="Kasia", regions=["EU"])))
        self.assertTrue(self.room.add_player(Player(name="Zosia", regions=["EU"])))
        self.assertTrue(self.room.add_player(Player(name="Basia", regions=["EU"])))
        self.assertFalse(self.room.add_player(Player(name="Wojtek", regions=["EU"])))
        self.assertFalse(self.room.empty())
        self.assertFalse(self.room.can_add_player())
        self.assertTrue(self.room.full())
