# Encapsulation and Access Control: OOP provides mechanisms to control the access to the internal state of objects. You can specify which attributes and methods are public, private, or protected, limiting direct access to certain parts of an object.

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number  # Protected attribute
        self._balance = initial_balance  # Protected attribute

    # Public method to get the account number
    def get_account_number(self):
        return self._account_number

    # Public method to get the balance
    def get_balance(self):
        return self._balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds")

# Creating an instance of the BankAccount class
account = BankAccount("123456789", 1000)

# Accessing the account number and balance using public methods
print("Account Number:", account.get_account_number())  # Output: Account Number: 123456789
print("Initial Balance:", account.get_balance())  # Output: Initial Balance: 1000

# Attempting to access protected attributes directly (not recommended)
print("Account Number (direct access):", account._account_number)  # Output: Account Number (direct access): 123456789
print("Balance (direct access):", account._balance)  # Output: Balance (direct access): 1000

# Depositing and withdrawing money using public methods
account.deposit(500)  # Output: Deposited $500. New balance: $1500
account.withdraw(200)  # Output: Withdrew $200. New balance: $1300
