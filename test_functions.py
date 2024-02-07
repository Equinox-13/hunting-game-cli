import unittest
from hunting_game import Gun, Animal, Game
from unittest.mock import patch

class TestGame(unittest.TestCase):
    def setUp(self):
        self.test_gun = Gun("Test Gun", 15)
        self.test_animal = Animal("Test Animal", 30)
        self.game = Game()

    def test_gun_initialization(self):
        self.assertEqual(self.test_gun.name, "Test Gun")
        self.assertEqual(self.test_gun.power, 15)

    def test_animal_initialization(self):
        self.assertEqual(self.test_animal.name, "Test Animal")
        self.assertEqual(self.test_animal.points, 30)

    @patch('builtins.input', side_effect=['1'])
    def test_select_gun(self, mock_input):
        selected_gun = self.game.select_gun()
        self.assertIn(selected_gun, self.game.guns)

    @patch('builtins.input', side_effect=['yes'])
    def test_shoot_animal(self, mock_input):
        initial_points = self.game.points
        self.game.shoot_animal(self.test_gun)
        self.assertTrue(self.game.points > initial_points)


if __name__ == "__main__":
    unittest.main()
