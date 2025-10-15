
class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def display(self):
        print("Account No:", self.account_no)
        print("Balance:", self.balance)
class SavingsAccount(Account):
    def __init__(self, account_no, balance):
        super().__init__(account_no, balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def check_balance(self):
        print("Current Balance:", self.balance)
s1 = SavingsAccount("36748718425", 1000)
s1.display()
s1.deposit(500)
