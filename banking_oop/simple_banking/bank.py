class BankAccount:
    """
    Parent class with attributes and methods for
    child classes.
    """
    account_number = 1000

    def __init__(self, title, type, balance):
        self.title = title
        self.type = type
        self.balance = balance
        self.is_dormant = False
        self.account_number = BankAccount.account_number
        BankAccount.account_number += 1

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Title: {self.title}\nAccount Type: {self.type}\nBalance: ${self.balance}"

    def deposit(self, amount):
        if not self.is_dormant and amount > 0:
            self.balance += amount
            print(f'${amount} deposited. New Balance: ${self.balance}')
        else:
            print("Account is dormant or amount is invalid")

    def make_dormant(self):
        if self.is_dormant:
            print("Account is already dormant.")
        else:
            self.is_dormant = True
            print("Account has been made dormant.")

    def withdraw(self, amount):
        if amount <= self.balance and not self.is_dormant:
            self.balance -= amount
            print(f'Withdrew ${amount}. Remaining Balance: {self.balance}')
        else:
            print("Account is dormant or amount is invalid")


class SavingsAccount(BankAccount):
    """
    Subclass that inherits from parent class and adds extra
    functionality for a savings account
    """

    def __init__(self, title, type, balance, minium_balance):
        super().__init__(title, type, balance)
        self.minimum_balance = minium_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Minimum amount requirement is not met")
        else:
            super().withdraw(amount)


# account1 = BankAccount("Rambo", "Current", 200)
# # print(account1)
# account1.deposit(100)
# account1.deposit(50)
# # account1.make_dormant()
# account1.deposit(200)
# account1.withdraw(300)
# print(account1)

# account2 = BankAccount("Kulu", "Saving", 300)
# print(account2)
# account2.deposit(50)

account3 = SavingsAccount("Michelle", "Savings", 50, 100)
print(account3)
account3.deposit(100)
account3.withdraw(100)
print(account3)

account4 = SavingsAccount("Karma", "Savings", 300, 200)
print(account4)
account4.make_dormant()
account4.withdraw(50)
account4.make_dormant()
