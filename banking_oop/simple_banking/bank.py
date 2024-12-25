class BankAccount:
    """
    Parent class with attributes and methods for
    child classes.
    """

    def __init__(self, title, type, balance):
        self.title = title
        self.type = type
        self.balance = balance

    def __str__(self):
        return f"Account Title: {self.title}\nAccount Type: {self.type}\nBalance: {self.balance}"


account1 = BankAccount("Rambo", "Current", 200)
print(account1)
