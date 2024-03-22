num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())
operation = input('Select the operation: ["+", "-", "*", "/", "%"] ').strip()

# Perform the selected operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:  # Check for division by zero
        print("Error: Division by zero")
        result = None
    else:
        result = num1 / num2
elif operation == '%':
    if num2 == 0:  # Check for modulus by zero
        print("Error: Modulus by zero")
        result = None
    else:
        result = num1 % num2
else:
    print("Invalid operation")
    result = None

# Print the result if it's valid
if result is not None:
    print(f"{num1} {operation} {num2} = {result}")
