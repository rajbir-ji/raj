<<<<<<< HEAD
#single inheritance 
class account:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
def show
        print(f"Account No: {self.acc_no}, Balance: {self.balance}")
   def__init__(self,acc_no,balance):
class saving_account(account):
    def deposit(self,amount)
=======
# write a program to deposit amount in savings account and check balance using single inheritance
# parent class :Account(account_no, balance)
# child class :SavingsAccount(deposit, check_balance)
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
>>>>>>> 9d27e64965f9df267775c3ab8eedb43175241e15
