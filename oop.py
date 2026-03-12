class Car:
    # constructor
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    # method
    def drive(self):
        print(self.brand,f"is my dream Car and {self.color} in color.")

# create object
car1=Car("BMW","Matte black")
car1.drive()
car2=Car("Mercedes-Benz","Dark blue")
car2.drive()
car3=Car("Porsche","Metallic white")
car3.drive()
car4=Car("Nissan","Midnight purple")
car4.drive()
car5=Car("Audi","Dark red")
car5.drive()

# Create a class called fruits.
# It should have three attributes:type,color,price
# A method called display(), then instance of that class(object)


class Fruits:
    def __init__(self,type,color,price):
        self.type=type
        self.color=color
        self.price=price

    def display(self):
        print(self.type,f"are {self.color} in color and each set cost {self.price}")

fruit1=Fruits("Apples","red","Ksh 60/=")
fruit1.display()
fruit2=Fruits("Bananas","yellow","Ksh 70/=")
fruit2.display()
fruit3=Fruits("Grapes","red","Ksh 100/=")
fruit3.display()
fruit4=Fruits("Pineapples","yellow","Ksh 125/=")
fruit4.display()
fruit5=Fruits("Pears","Green","Ksh 105/=")
fruit5.display()
fruit6=Fruits("Orange","orange","Ksh 75/=")
fruit6.display()

