# Write a script that checks if someone is eligible to vote
age=int(input("Enter age:"))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not viable to vote.Underage...")

# Write a script that checks if a number is odd or even
number=int(input("Enter number:"))

if number%2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")

# Write a script that checks "python123" is valid
# else wrong password
password = (input("Enter password:"))

if "python123" in password:
    print("Correct")
else:
    print("Incorrect")
# write a script that checks the largest number of three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num1>num2 and num1>num3:
    print(f"{num1} is the largest number.")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest number.")
elif num3>num1 and num3>num2:
    print(f"{num3} is the greatest number.")
else:
    print("They are all equal.")



