def calculate(n1, n2, operation):
    # Convert inputs to integers
    n1 = int(n1)
    n2 = int(n2)

    # Check the operation and perform corresponding calculation
    if operation in ['+', 'add', 'a']:
        result = n1 + n2
    elif operation in ['-', 'subtract', 's']:
        result = n1 - n2
    elif operation in ['*', 'multiply', 'm']:
        result = n1 * n2
    elif operation == "":
        # If no operation is provided, default to addition
        result = n1 + n2
    else:
        # If the operation is not recognized, print an error message
        print("This operation is not available!")
        return

    # Print the result
    print(f"Result: {result}")


# Input from the user: 2 numbers separated by space, and the desired operation
numbers = input("Enter 2 numbers separated by space: ").split()
operation = input("Choose the operation [+,-,*]: ").lower()

# Check if exactly 2 numbers were provided
if len(numbers) == 2:
    # Call the calculate function with the provided inputs
    calculate(*numbers, operation)
else:
    # If the input is invalid (not exactly 2 numbers), print an error message
    print("Invalid input. Please enter two numbers.")
