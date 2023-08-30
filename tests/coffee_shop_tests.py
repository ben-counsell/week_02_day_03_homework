import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop("Ben's Coffee Shop", 100, [
            Drink("Long Black", 3, 10), 
            Drink("Flat White", 4, 12), 
            Drink("Cappuccino", 5, 9)
            ]
        )
        self.customer_john = Customer("John", 50, 15, 100)
        self.customer_clive = Customer("Clive", 10, 30, 98)
        self.customer_scruffy = Customer("Scruffy", -10, 45, 24)

    def test_coffee_shop_has_name(self):
        self.assertEqual("Ben's Coffee Shop", self.coffee_shop.name)
    
    def test_drink_has_name(self):
        self.assertEqual("Cappuccino", self.coffee_shop.drinks_menu[2].name)
    
    def test_sale_to_customer(self):
        self.coffee_shop.sell_drink_to_customer(self.coffee_shop.drinks_menu[1], self.customer_clive)
        self.assertEqual(6, self.customer_clive.wallet_balance)
        self.assertEqual(104, self.coffee_shop.till_balance)
        self.assertEqual(110, self.customer_clive.energy_level)
    
    def test_refused_sales(self):
        self.coffee_shop.sell_drink_to_customer(self.coffee_shop.drinks_menu[0], self.customer_john)
        self.coffee_shop.sell_drink_to_customer(self.coffee_shop.drinks_menu[2], self.customer_scruffy)
        self.coffee_shop.sell_drink_to_customer(self.coffee_shop.drinks_menu[0], self.customer_clive)
        self.coffee_shop.sell_drink_to_customer(self.coffee_shop.drinks_menu[0], self.customer_clive)
        self.assertEqual(103, self.coffee_shop.till_balance)
    