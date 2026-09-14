"""uczymy sie jak programowac w pythonie"""
import questionary
#(First_name = "ksawery"
#Last_name = "kida"
#Full_name = f"{len(First_name)} + {3+2} = {len(First_name) + 3 + 2}"
#print(Full_name)

#   """methods testing"""

#USE = "        program test"
#print(USE.upper().strip())
#print(USE.strip().title())
#print(USE.find("te"))
#print(USE.replace("test", "test2").strip().upper())
#print("pro" in USE)
#print("prox" not in USE)

#"""Numbers testing"""

    # """Module"""

#import math
#print(2**3)
#print(3 + 2)
#print(15 // 4)


"""choice = questionary.select(
    "Choose your operation: ",
    choices= ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division"]).ask()
if choice == "1. Addition":
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    print("Solution: ", x + y)
if choice == "2. Subtraction":
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    print("Solution: ", x - y)
if choice == "3. Multiplication":
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    print("Solution: ", x * y)
if choice == "4. Division":
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    print("Solution: ", x / y)"""





#x=input("Enter first number: ")
#int_x=int(x) 
#y=input("Enter second number: ")
#inty=int(y)

#   Age verification
print("Hello, welcome to the age and height verification program.")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in cm: "))
message = "eligible" if age >= 18 and height >=160 else "not eligible"
for number in range(3):
    print(message)