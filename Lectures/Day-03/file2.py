# Encapsulation: Encapsulation is the principle of bundling data (attributes) and methods (functions) that operate on that data into a single unit, i.e., a class. It hides the internal details of how an object works and exposes a public interface for interacting with it.

# Python uses naming conventions to indicate the level of visibility (public, protected, private).

# Public attributes and methods are accessible directly, protected attributes and methods have a single underscore prefix (e.g., _protected_var), and private attributes and methods have a double underscore prefix (e.g., __private_var).

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self._balance = balance  # Protected attribute

    # Public method to get the balance
    def get_balance(self):
        return self._balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

# Creating an instance of the BankAccount class
account = BankAccount("123456789", 1000)

# Accessing the balance using the public method
print("Current balance:", account.get_balance())  # Output: Current balance: 1000

# Depositing and withdrawing money
account.deposit(500)
print("After depositing 500:", account.get_balance())  # Output: After depositing 500: 1500

account.withdraw(200)
print("After withdrawing 200:", account.get_balance())  # Output: After withdrawing 200: 1300

# Attempting to access protected attributes directly (not recommended)
print("Account number:", account._account_number)  # Output: Account number: 123456789
print("Balance:", account._balance)  # Output: Balance: 1300
