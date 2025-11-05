#I need to create a console based application that takes 1.Addition 2.Subtraction 3.Multiplication 4.Division as input from user and perform the operation accordingly
from input_ex import *

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter the operation number (1-4): ")
if operation == "1":
    result = add_numbers()
    print("Result:", result)
elif operation == "2":
    result = subtract_numbers()
    print("Result:", result)
elif operation == "3":
    result = multiply_numbers()
    print("Result:", result)
elif operation == "4":
    result = divide_numbers()
    print("Result:", result)
else:
    print("Invalid operation.")



