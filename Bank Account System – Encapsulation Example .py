Bank Account System – Encapsulation Example 
class bank:
    def __init__(self):
        self.__pin=12345
        self.__amount=45000
    def check_balance(self,current_pin):
        if current_pin==self.__pin:
            print("total balance:",self.__amount)
        else:
            print("invalid pin")
    def deposit_amount(self,current_depositamount):
        if current_depositamount>0:
            self.__amount+=current_depositamount
            print(f"your money deposite successfully and your total balance is {self.__amount}")
        else:
            print("invalid pin")
    def withdraw(self,pin,withdraw_amount):
        if self.__pin==pin:
            if withdraw_amount<self.__amount:
                self.__amount-=withdraw_amount
                print(f"your withdraw is successful and remaining amount {self.__amount}")
        else:
            print("invalid pin")
        
abc=bank()
current_pin=int(input("enter pin:"))
abc.check_balance(current_pin)
current_depositamount=int(input("enter amount:"))

abc.deposit_amount(current_depositamount)
pin=int(input("enter pin:"))
withdraw_amount=int(input("enter amount"))
abc.withdraw(pin,withdraw_amount)
