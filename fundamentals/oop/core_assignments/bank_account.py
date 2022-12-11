class BankAccount:
    accounts = []

    def __init__(self, balance=0, int_rate=0.01):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance = amount + self.balance
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charing a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.int_rate}")

    def yield_interest(self):
        if self.balance is self.balance > 0:
            self.balance = self.balance * self.int_rate + self.balance
        return self

    @classmethod
    def all_instances(cls):
        for i in cls.accounts:
            i.display_account_info()

first_account = BankAccount()
second_account = BankAccount()

first_account.deposit(100).deposit(100).deposit(100).yield_interest()

second_account.deposit(50).deposit(50).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest()
BankAccount.all_instances()