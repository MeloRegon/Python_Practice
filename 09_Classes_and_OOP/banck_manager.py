# Basic Bank Account Class
# Defines a BankAccount class with methods for deposit, withdrawal, and balance check.

class BankAccount:
    def __init__(self, name:str, balance: float):
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount:.2f}')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Withdraw {amount:.2f}')
        else:
            print(f'Insufficient funds or invalid amount.')

    def get_balance(self) -> float:
        return self.balance



if __name__ =='__main__':
    account = BankAccount('Egor', 1000000.0)
    account.deposit(1000)
    account.withdraw(500)
    print(f'Current balance: {account.get_balance()}')

