# Welcome message
print("Welcome to the Basic Calculator!")

# Step 1: Ask the user for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Step 2: Ask the user for the operation
print("Choose an operation: + for addition, - for subtraction, * for multiplication, / for division")
operation = input("Enter the operation you want to perform: ")

# Step 3: Perform the chosen operation
if operation == "+":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == "-":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == "*":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == "/":
    if number2 != 0:  # Check for division by zero
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation. Please enter +, -, *, or /.")

# End message
print("Thank you for using the calculator!")
