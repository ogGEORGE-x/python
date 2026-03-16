from abc import ABC,abstractmethod
class MpesaAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f"{amount} deposited. Balance:{self.__balance}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"{amount} withdrawn. Balance:{self.__balance}")
            return True
        return False
    def get_balance(self):
        return self.__balance
    
# abstraction
class MpesaService(ABC):
    @abstractmethod
    def access_service(self,account,ammount):
        pass
class SendMoney(MpesaService):
    def access_service(self,account,amount):
        if account.withdraw(amount):
            print(f"Sent {amount} to another user")
        else:
            print("Transaction failed.Insufficient funds.")
account=MpesaAccount("Daniel",1000)
send_money=SendMoney()

send_money.access_service(account,100)

    