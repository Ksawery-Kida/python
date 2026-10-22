"""uczymy sie jak programowac w pythonie"""

#   Age verification
print("Hello, welcome to the age and height verification program.")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in cm: "))
message = "eligible" if age >= 18 and height >= 160 else "not eligible"
for number in range(3):
    print(message)
