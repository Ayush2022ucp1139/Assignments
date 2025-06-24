class BankAccount:
    def __init__(self,account_holder,balance = 0):
        self.balance = int(balance)
        self.account_holder = account_holder

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Invalid withdrawal amount or insufficient funds"

    def check_balance(self):
        return self.balance
    
customer1 = BankAccount("Ayush",1000)
print(customer1.deposit(1000))
print(customer1.check_balance())
print(customer1.withdraw(500))    