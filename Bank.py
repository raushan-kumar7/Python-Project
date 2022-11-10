class Bank:
    def Withdrawal(self,Balance_amount,Withdrawal_amount):
        return Balance_amount - Withdrawal_amount

class Cashier:
    def Deposite(self,Left_amount,Deposite_amount):
        return Left_amount + Deposite_amount

class Account(Bank,Cashier):
    def Show(self):
        print("Account Holder Name : ","Raushan")

Customer = Account()
Customer.Show()
print("Withdrawal Amount : ",Customer.Withdrawal(10000,6000))
print("Deposite Amount : ",Customer.Deposite(4000,8000))