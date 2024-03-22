def addition(*numbers):
    """
    Perform addition with some special conditions:
    - If the number is 10, skip it.
    - If the number is 5, subtract it from the sum.
    - Otherwise, add the number to the sum.
    """
    sum_result = 0  # Initialize the sum

    for number in numbers:  # Iterate over the provided numbers
        if number == 10:
            continue  # Skip if the number is 10

        elif number == 5:
            sum_result -= 5  # Subtract 5 if the number is 5

        else:
            sum_result += number  # Add the number to the sum otherwise

    print(sum_result)  # Print the final sum

# Test the function with provided inputs
addition(10, 20, 30, 10, 15)  # Expected output: 65

addition(10, 20, 30, 10, 15, 5, 100)  # Expected output: 160
