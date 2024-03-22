import random


def generate_random_numbers():
    """Generate and print random numbers within specified ranges."""

    # Random number between 10 and 50 (inclusive)
    random_number = random.randint(10, 50)
    print(f"Random Number Between 10 And 50 => {random_number}")

    # Random even number between 2 and 10 (inclusive)
    random_even = random.randrange(2, 11, 2)
    print(f"Random Even Number Between 2 And 10 => {random_even}")

    # Random odd number between 1 and 9 (inclusive)
    random_odd = random.randrange(1, 10, 2)
    print(f"Random Odd Number Between 1 And 9 => {random_odd}")

    # Print available methods in the random module
    print(dir(random))


# Call the function to execute the code
generate_random_numbers()
