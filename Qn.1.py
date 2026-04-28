from turtledemo.paint import switchupdown


class BankAccount:
    def  __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.__balance = balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("deposited")
        else :
            print("invalid amount")

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("withdrawn...current balance = ",self.__balance)
        else :
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self,acc_no,balance,interest_rate):
        super().__init__(acc_no,balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest= self.get_balance()*self.interest_rate/100
        print("Interest = ",interest)
        return interest

class CurrentAccount(BankAccount):
    def __init__(self,acc_no,balance,min_balance):
        super().__init__(acc_no,balance)
        self.min_balance = min_balance

    def withdraw(self,amount):
        if self.get_balance()-amount>=self.min_balance:
            super().withdraw(amount)
        else:
            print("Insufficient Balance")


print("Savings Account")
s=SavingsAccount("1001",1000,5)
s.deposit(100)
s.withdraw(200)
s.calculate_interest()

print("Current Account")
c = CurrentAccount("1002",1000,100)
c.deposit(100)
c.withdraw(20)
c.withdraw(2000)



