#Create a bank account class with attributes balance and methods for deposit and withdrawal.
class BankAccount:
    """A simple attempt to represent a bank account."""

    def __init__(self,balance):
        """Initialize the attributes of class BankAccount."""
        self.balance = balance

    def deposit(self,amount):
        """Add the given number to the balance."""
        self.balance += amount
        print(f"\nAmmount {amount} has been depositated.Now the balance is {self.balance}")

    def withdrawal(self,amount):
        """Subtract the given ammount from the balance."""
        if self.balance >= amount:
            self.balance -= amount
        print(f"\nAmmount {amount} has been withdrawn.Now the balance is {self.balance}")

my_account = BankAccount(5000)
my_account.deposit(1000)
my_account.withdrawal(500)
