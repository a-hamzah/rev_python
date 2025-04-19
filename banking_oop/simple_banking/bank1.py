from datetime import date


class Transaction:
    def __init__(self, transaction_amount, transaction_type):
        self.transaction_amount = transaction_amount
        self.transaction_type = transaction_type
        self.transaction_date = date.today()

    def __str__(self):
        return f'{self.transaction_date} - {self.transaction_type} - ${self.transaction_amount}'


class BankAccount:
    """
    Parent class with attributes and methods for
    child classes.
    """
    account_number = 1000

    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        self.is_dormant = False
        self.account_number = BankAccount.account_number
        BankAccount.account_number += 1
        self.transactions = []

    def deposit(self, amount):
        if not self.is_dormant and amount > 0:
            self.balance += amount
            print(f'${amount} deposited. New Balance: ${self.balance}')
            self.transactions.append(Transaction(amount, "Credit"))
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
            self.transactions.append(Transaction(amount, "Debit"))
        else:
            print("Account is dormant or amount is invalid")

    def print_transaction_history(self):
        print("***TRANSACTION HISTORY***")
        if self.transactions is not None:
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions found.")


class SavingsAccount(BankAccount):
    """
    Subclass that inherits from parent class and adds extra
    functionality for a savings account
    """

    def __init__(self, title, balance, minium_balance):
        super().__init__(title, balance)
        self.minimum_balance = minium_balance
        self.type = "Savings"

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Type: {self.type}\nAccount Title: {self.title}\nBalance: ${self.balance}"

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

account3 = SavingsAccount("Michelle", 150, 50)
account3.deposit(100)
account3.deposit(150)
account3.deposit(50)
account3.withdraw(230)
account3.withdraw(30)
account3.print_transaction_history()
# print(account3)

# account4 = SavingsAccount("Karma", "Savings", 300, 200)
# print(account4)
# account4.make_dormant()
# account4.withdraw(50)
# account4.make_dormant()
