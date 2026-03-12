class MPesaAccount:
    def __init__(self,name,phone,balance):
        self.name=name
        self.phone=phone
        self.balance=balance
    def deposit(self,amount):
        self.balance +=amount
        print("Deposited",amount)
        print(f"Your balance is {self.balance}")
    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance -=amount
            print(f"Withdrawn {amount}")
            print(f"New balance is {self.balance}")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print(f"Balance is {self.balance}")

user1=MPesaAccount("Osama",254701234567,5000)
user1.check_balance()
user1.deposit(6456)
user1.check_balance()
user1.withdraw(20000)

user2=MPesaAccount("Suki",254709112387,2500)
user2.check_balance()
user2.deposit(64560)
user2.check_balance()
user2.withdraw(20000)

user3=MPesaAccount("Adolf",254732985469,397328)
user3.check_balance()
user3.deposit(43084)
user3.check_balance()
user3.withdraw(200000)

user4=MPesaAccount("Hanzo",254763963263,759473)
user4.check_balance()
user4.deposit(5473)
user4.check_balance()
user4.withdraw(20000000)


