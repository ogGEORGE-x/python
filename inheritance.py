class Car:
    def __init__(self,Brand):
        self.Brand=Brand

    def printbrand(self):
        print(self.Brand)
Brand=input("Enter car brand:")

class type(Car):
    def type(self,type):
        print(self)

Y= type(input("Enter brand type:"))
Y.printbrand()