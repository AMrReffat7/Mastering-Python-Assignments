# Define a list of numbers
my_numbers = [15, 81, 5, 17, 20, 21, 13]

# Sort the list of numbers in descending order
my_numbers.sort(reverse=True)

# Initialize a counter for numbers divisible by 5
a = 1

# Iterate through each number in the sorted list
for num in my_numbers:
    # Check if the number is divisible by 5
    if num % 5 == 0:
        # Print the count and the number if it's divisible by 5
        print(f"{a} => {num}")
        # Increment the counter
        a += 1

# Print a message indicating that all numbers have been processed
print("All Numbers are Printed")
