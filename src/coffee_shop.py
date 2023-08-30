class CoffeeShop:
    def __init__(self, shop_name, till_balance, drinks_menu):
        self.name = shop_name
        self.till_balance = till_balance
        self.drinks_menu = drinks_menu
    def sell_drink_to_customer(self, drink, customer):
        if customer.wallet_balance >= drink.price and customer.age >= 16 and customer.energy_level <= 105:
            self.till_balance += drink.price
            customer.reduce_funds_in_wallet(drink.price)
            customer.increase_energy_level(drink.caffeine_level)