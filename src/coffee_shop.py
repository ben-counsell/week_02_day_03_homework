class CoffeeShop:
    def __init__(self, shop_name, till_balance, drinks_menu, food_menu):
        self.name = shop_name
        self.till_balance = till_balance
        self.drinks_menu = drinks_menu
        self.food_menu = food_menu
    def sell_drink_to_customer(self, drink, customer):
        if customer.wallet_balance >= drink.price and customer.age >= 16 and customer.energy_level <= 100:
            self.till_balance += drink.price
            customer.reduce_funds_in_wallet(drink.price)
            customer.increase_energy_level(drink.caffeine_level)
    def sell_food_to_customer(self, food, customer):
        if customer.wallet_balance >= food.price:
            self.till_balance += food.price
            customer.reduce_funds_in_wallet(food.price)
            customer.reduce_energy_level(food.digestion_level)