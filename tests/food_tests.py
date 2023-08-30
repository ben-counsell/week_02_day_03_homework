import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.ham_sandwich = Food("Ham Sandwich", 10, 7)
    def test_that_food_has_price(self):
        self.assertEqual(10, self.ham_sandwich.price)