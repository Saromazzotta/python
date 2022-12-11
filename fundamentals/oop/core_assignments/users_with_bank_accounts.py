class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.balance = self.accounts.balance + amount
        return self

    def make_withdrawal(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging User $5")
            self.balance = self.balance - 5
        else: 
            self.balance = self.balance - amount
        return self

    def display_user_balance(self):
        print(f"Balance {self.balance}")

    # def transfer_money(self, amount, other_user):
    #     pass

    # def new_account(self, amount=0, int_rate=0.02):
    #     self.accounts.append(BankAccount(int_rate, amount))


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

first_user = User("person1", "person1@email.com")
second_user = User("person2", "person2@email.com")

first_user.make_deposit(100).make_withdrawal(50).display_user_balance()

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
