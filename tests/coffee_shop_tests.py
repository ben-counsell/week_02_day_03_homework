import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.long_black = Drink("Long Black", 3, 10)
        self.flat_white = Drink("Flat White", 4, 12)
        self.cappuccino = Drink("Cappuccino", 5, 9)
        self.ham_sandwich = Food("Ham Sandwich", 10, 7)
        self.coffee_shop = CoffeeShop("Ben's Coffee Shop", 100, {
            self.long_black : 4,
            self.flat_white : 0,
            self.cappuccino : 6,
            },
            {self.ham_sandwich : 3}
    )
        self.customer_john = Customer("John", 50, 15, 60)
        self.customer_clive = Customer("Clive", 10, 30, 98)
        self.customer_scruffy = Customer("Scruffy", -10, 45, 24)

    def test_coffee_shop_has_name(self):
        self.assertEqual("Ben's Coffee Shop", self.coffee_shop.name)
    
    def test_drink_has_name(self):
        self.assertEqual("Cappuccino", self.cappuccino.name)

    def test_if_drink_is_in_stock(self):
        self.assertGreater(self.coffee_shop.drinks_menu[self.long_black], 0)
        self.assertEqual(self.coffee_shop.drinks_menu[self.flat_white], 0)
    
    def test_drinks_sale_to_customer(self):
        self.coffee_shop.sell_drink_to_customer(self.long_black, self.customer_clive)
        self.assertEqual(7, self.customer_clive.wallet_balance)
        self.assertEqual(103, self.coffee_shop.till_balance)
        self.assertEqual(108, self.customer_clive.energy_level)
    
    def test_refused_drinks_sales(self):
        self.coffee_shop.sell_drink_to_customer(self.long_black, self.customer_john)
        self.coffee_shop.sell_drink_to_customer(self.cappuccino, self.customer_scruffy)
        self.coffee_shop.sell_drink_to_customer(self.long_black, self.customer_clive)
        self.coffee_shop.sell_drink_to_customer(self.long_black, self.customer_clive)
        self.assertEqual(103, self.coffee_shop.till_balance)

    def test_food_sale_to_customer(self):
        self.coffee_shop.sell_food_to_customer(self.ham_sandwich, self.customer_clive)
        self.assertEqual(0, self.customer_clive.wallet_balance)
        self.assertEqual(110, self.coffee_shop.till_balance)
        self.assertEqual(91, self.customer_clive.energy_level)

    def test_calculate_stock_value(self):
        self.assertEqual(42, self.coffee_shop.calculate_stock_value())
        self.coffee_shop.drinks_menu[self.flat_white] = 2
        self.assertEqual(50, self.coffee_shop.calculate_stock_value())