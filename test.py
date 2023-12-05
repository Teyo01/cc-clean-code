import unittest
from YamsGame import *


class TestYamsGame(unittest.TestCase):
    def test_brelan(self):
        game = YamsGame([[1, 1, 1, 2, 3]])
        self.assertEqual(game.calculate_score(), 28)

    def test_carre(self):
        game = YamsGame([[4, 4, 4, 4, 2]])
        self.assertEqual(game.calculate_score(), 35)

    def test_full(self):
        game = YamsGame([[3, 3, 3, 2, 2]])
        self.assertEqual(game.calculate_score(), 30)

    def test_grande_suite(self):
        game = YamsGame([[2, 3, 4, 5, 6]])
        self.assertEqual(game.calculate_score(), 40)

    def test_yams(self):
        game = YamsGame([[6, 6, 6, 6, 6]])
        self.assertEqual(game.calculate_score(), 50)

    def test_chance(self):
        game = YamsGame([[1, 1, 2, 2, 3]])
        self.assertEqual(game.calculate_score(), 9)

    def test_multiple_rolls(self):
        game = YamsGame([[1, 1, 1, 2, 3], [4, 4, 4, 4, 2], [3, 3, 3, 2, 2]])
        self.assertEqual(game.calculate_score(), 93)


if __name__ == '__main__':
    unittest.main()
