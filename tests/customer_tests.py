import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.john = Customer("John", 50, 15, 60)
        self.clive = Customer("Clive", 10, 30, 98)
        self.scruffy = Customer("Scruffy", -10, 45, 24)
    def test_that_customer_has_name(self):
        self.assertEqual("Clive", self.clive.name)
    def test_that_customer_has_energy_level(self):
        self.assertEqual(98, self.clive.energy_level)
    def test_reduce_funds_in_wallet(self):
        self.john.reduce_funds_in_wallet(10)
        self.assertEqual(40, self.john.wallet_balance)
    def test_increase_energy_level(self):
        self.john.increase_energy_level(20)
        self.assertEqual(80, self.john.energy_level)
    def test_reduce_energy_level(self):
        self.john.reduce_energy_level(20)
        self.assertEqual(40, self.john.energy_level)
