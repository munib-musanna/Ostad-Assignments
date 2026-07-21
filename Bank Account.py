'''7. (Challenge) Extend the BankAccount class so it 
also counts how many transactions 
(deposits + withdrawals) have happened.'''

class BankAccount:
    def __init__(self, owner, balance = 0, transactions = 0):
        self.owner = owner
        self.balance = balance
        self.transactions = transactions
    def show_info(self):
        print(f"Account Holder: {self.owner}. \n Balance: {self.balance} \n Transactions: {self.transactions}")
    def deposit(self, amount):
         self.balance += amount
         self.transactions += 1
         return self.show_info()
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions += 1
        else:
            print("Insufficient Balance.")
        return self.show_info()
    
acc = BankAccount("Munib", 10000)
acc.deposit(500)
acc.withdraw(2000)
acc.withdraw(25000)
acc.deposit(650)
acc.show_info()
