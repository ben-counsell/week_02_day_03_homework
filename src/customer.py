class Customer:
    def __init__(self, customer_name, wallet_balance, age, energy_level):
        self.name = customer_name
        self.wallet_balance = wallet_balance
        self.age = age
        self.energy_level = energy_level
    def reduce_funds_in_wallet(self, input_amount):
        self.wallet_balance -= input_amount
    def increase_energy_level(self, input_amount):
        self.energy_level += input_amount
    def purchase_drink(self, drink):
        self.wallet_balance -= drink.price