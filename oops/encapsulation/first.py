class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

    # Setter for balance with validation
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

# Usage example
if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    account.deposit(50)
    account.withdraw(30)
    print("Current balance:", account.get_balance())

    # Trying to access private attribute directly (not recommended)
    # print(account.__balance)  # AttributeError

    # Using setter to update balance
    account.set_balance(200)
    print("Updated balance:", account.get_balance())