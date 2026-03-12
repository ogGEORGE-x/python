num=5

while num<=15:
    print(num)

    num+=2

# create a script starting with 50

num2=50

while num2>=0:
    print(num2)
    num2-=1

secret=7
guess=0

while guess!=secret:
    guess=int(input("Enter first number:"))
    if guess== secret:
        print("correct")
    else:
        print("You are a failure")
cars=["BMW","Mercedes-Benz","Porsche","Audi","Volkswagen"]
for i in cars:
    print(i)