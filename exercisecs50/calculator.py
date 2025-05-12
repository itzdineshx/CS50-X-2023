#import cs50's library -> for get_int function
from cs50 import get_int

while True:
    # Get input from the user
    num1 = float(input("Enter Num1: "))

    # Get the operation input from the user
    op = input("Enter Operator (+, -, *, /, or 'exit' to quit): ")

    # Check if the user wants to exit
    if op.lower() == 'exit':
        print("Calculator exiting. Goodbye!")
        break

    num2 = float(input("Enter Num2: "))

    # Perform operations
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue  # Restart the loop to allow for a valid input
        result = num1 / num2
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
        continue  # Restart the loop to allow for a valid input

    print(f"Result: {result}")
