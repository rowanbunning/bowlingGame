import unittest

import bowling as bowl

class TestBowlingCalculator(unittest.TestCase):

    def setUp(self):
        self.game = bowl.BowlingGame()

    def test_roll_all_gutters(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_roll_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_roll_one_strike(self):
        self.roll_many(2, 10)
        self.assertEqual(self.game.score(), 20)

    def test_role_one_spare(self):
         self.game.roll(5)
         self.game.roll(5)
         self.game.roll(3)
         self.assertEqual(self.game.score(), 13)

    def test_role_strike(self):
         self.game.roll(10)
         self.game.roll(5)
         self.game.roll(3)
         self.assertEqual(self.game.score(), 18)

    def all_strikes(self):
        roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

    def roll_many(self, rolls, pins):
        for roll in range(rolls):
            self.game.roll(pins)