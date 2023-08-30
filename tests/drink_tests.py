import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.long_black = Drink("Long Black", 3, 10)
        self.flat_white = Drink("Flat White", 4, 12)
        self.cappuccino = Drink("Cappuccino", 5, 9)
    def test_that_drink_has_price(self):
        self.assertEqual(3, self.long_black.price)
    def test_that_drink_has_caffeine_level(self):
        self.assertEqual(10, self.long_black.caffeine_level)