# Savings Account Extension
# Inherits from BankAccount and adds functionality to apply interest to the balance.

from banck_manager import  BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name: str, balance: float, interest_rate: float):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f'Interest of {interest:.2f} applied')


savings = SavingsAccount('Egor', 1000000.0, 0.05)
savings.apply_interest()
print(f'New balance: {savings.get_balance():.2f}')


