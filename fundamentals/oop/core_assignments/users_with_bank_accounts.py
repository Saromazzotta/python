class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Balance {self.account.balance}")

    # def transfer_money(self, amount, other_user):
    #     pass

    # def new_account(self, amount=0, int_rate=0.02):
    #     self.accounts.append(BankAccount(int_rate, amount))


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
first_user = User("person1", "person1@email.com")
second_user = User("person2", "person2@email.com")

first_user.make_deposit(100).make_withdrawal(50).display_user_balance()

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
