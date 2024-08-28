class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance")

    def withdraw(self, amount): 
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount} from the balance")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

# Create an instance of Account
acct1 = Account('Jose', 100)

# Access owner and balance attributes
print(acct1.owner)       # Output: Jose
print(acct1.balance)     # Output: 100

# Perform withdrawals
acct1.withdraw(75)       # Output: Withdrawn 75 from the balance
print(acct1.balance)     # Output: 25

acct1.withdraw(500)      # Output: Funds Unavailable!
print(acct1.balance)     # Output: 25

acct1.withdraw(50)       # Output: Funds Unavailable!
print(acct1.balance)     # Output: 25