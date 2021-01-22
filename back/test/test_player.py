import unittest

from game_manager.player import Player 
from game_manager.fixed_size_set import FixedSizeSet 

class PlayerTestCase(unittest.TestCase):

    def test_base(self):
        player = Player(name="Marcin", regions=["EUROPE","ASIA"])
        self.assertEqual(player.name, "Marcin")
        self.assertTrue("ASIA" in player.regions)
        self.assertTrue("EUROPE" in player.regions)
        self.assertFalse("AUSTRALIA" in player.regions)
