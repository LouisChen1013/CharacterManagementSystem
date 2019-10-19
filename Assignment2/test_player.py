import unittest
import inspect
from player import Player


class TestPlayer(unittest.TestCase):
    """ Unit Test for Player Class """

    def setUp(self):
        """ Initialize fixtures """

        self.logPlayer()
        self.player = Player(2, "assassin")
        self.assertIsNotNone(self.player)

    def test_constructor_valid(self):
        """ Test 010A - Valid Construction"""

        self.assertIsInstance(self.player, Player)

    def test_constructor_invalid(self):
        """ Test 010B - Invalid Construction """

        self.assertRaisesRegex(
            ValueError, "Player Level cannot be undefined", Player, None, "assassin")
        self.assertRaisesRegex(
            ValueError, "Player Level cannot be empty", Player, "", "assassin")

        self.assertRaisesRegex(
            ValueError, "Player Job cannot be undefined", Player, 9, None)
        self.assertRaisesRegex(
            ValueError, "Player Job cannot be empty", Player, 9, "")

        self.assertNotIn(20, Player.LEVEL_RANGE)
        self.assertNotIn("Mage".lower(), Player.PLAYER_JOB)

    def test_set_level_valid(self):
        """ Test 020A - Set valid level"""

        self.player.set_level(2)
        self.assertEqual(2, self.player.get_level())

        self.player.set_level(5)
        self.assertEqual(5, self.player.get_level())

        self.player.set_level(10)
        self.assertEqual(10, self.player.get_level())

    def test_set_level_invalid(self):
        """ Test 020B - Set invalid level"""

        self.assertRaisesRegex(
            ValueError, "Player Level is out of range, please enter 0-10", self.player.set_level, 20)
        self.assertRaisesRegex(
            ValueError, "Player Level cannot be undefined", self.player.set_level, None)
        self.assertRaisesRegex(
            ValueError, "Player Level cannot be empty", self.player.set_level, "")

    def test_get_level(self):
        """ Test 020B - Get Valid Player Level """

        self.assertEqual(self.player.get_level(), 2)

        self.player.set_level(2)
        self.assertEqual(self.player.get_level(), 2)

        self.player.set_level(4)
        self.assertEqual(self.player.get_level(), 4)

    def test_set_job_valid(self):
        """ Test 030A - Set Valid Player Job """
        self.player.set_job("knight".lower())
        self.assertEqual("knight", self.player.get_job())

        self.player.set_job("assassin".lower())
        self.assertEqual("assassin", self.player.get_job())

        self.player.set_job("warrior".lower())
        self.assertEqual("warrior", self.player.get_job())

    def test_set_job_invalid(self):
        """ Test 030B - Set Invalid Player Job """
        self.assertRaisesRegex(
            ValueError, "Player Job must be either assassin, knight, or warrior", self.player.set_job, "Thief".lower())
        self.assertRaisesRegex(
            ValueError, "Player Job cannot be undefined", self.player.set_job, None)
        self.assertRaisesRegex(
            ValueError, "Player Job cannot be empty", self.player.set_job, "")

    def test_get_job(self):
        """ Test 040A - Get Valid Player Job """
        # init
        self.assertEqual(self.player.get_job(), "assassin")
        # change same
        self.player.set_job("assassin")
        self.assertEqual(self.player.get_job(), "assassin")
        # change different
        self.player.set_job("warrior")
        self.assertEqual(self.player.get_job(), "warrior")

    def test_get_details(self):
        """ Test 050A - Get Valid Player Details """
        self.assertEqual(
            "The player is level 2 assassin with 84 health and 33 damage, Position: X = 0 Y = 0", self.player.get_details())
        self.player.set_level(5)
        self.assertEqual(
            "The player is level 5 assassin with 96 health and 42 damage, Position: X = 0 Y = 0", self.player.get_details())
        self.player.set_job("warrior")
        self.assertEqual(
            "The player is level 5 warrior with 136 health and 22 damage, Position: X = 0 Y = 0", self.player.get_details())
        self.player.set_level(2)
        self.player.set_job("knight")
        self.assertEqual(
            "The player is level 2 knight with 104 health and 23 damage, Position: X = 0 Y = 0", self.player.get_details())

    def get_type(self):
        self.assertEqual("player", self.player.get_type())

    def tearDown(self):
        """" Tear down """
        self.logPlayer()

    def logPlayer(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))


if __name__ == "__main__":
    unittest.main()
