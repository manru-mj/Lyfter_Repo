class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self,min_balance):
        super().__init__()
        self.min_balance = min_balance
        self.balance = min_balance
        print(f"A new savings account has been opened. A mimimum balance of {self.min_balance} is required to maintain the account.")
        self.print_balance

    def print_balance(self):
        print(f'Balance: {self.balance}')

    
    def withdraw(self, amount):
        if self.min_balance<(self.balance-amount):
            return super().withdraw(amount)
        else:
            print(f"Can't withdraw. A mimimum balance of {self.min_balance} is required to maintain the account.")

