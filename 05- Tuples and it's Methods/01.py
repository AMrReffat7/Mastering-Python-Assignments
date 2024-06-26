# ---------------(Assignment 1)---------------
# Define a tuple with a single element and print its value and type
name = "Ali",  # Note the comma to create a tuple with a single element

print(name)
print(type(name))

print("=" * 50)

# ---------------(Assignment 2)---------------
# Convert a tuple to a list, modify it, and convert it back to a tuple
my_friends = ("Osama", "Ahmed", "Sayed")

friends_list = list(my_friends)
friends_list[0] = "Elzero"
friends_tuple = tuple(friends_list)

print(friends_tuple)
print(type(friends_tuple))
print(f"{len(friends_tuple)} Elements")

print("=" * 50)

# ---------------(Assignment 3)---------------
# Concatenate two tuples and print the resulting tuple and its length
nums = (1, 2, 3)
letters = ("A", "B", "C")

my_tuple = nums + letters

print(f"My Tuple = {my_tuple}")
print(f"{len(my_tuple)} Elements")

print("=" * 50)

# ---------------(Assignment 4)---------------
# Unpack a tuple into variables and print specific elements
my_tuple = (1, 2, 3, 4)

A, B, _, C = my_tuple  # Using underscore to denote unused variable

print(A)
print(B)
print(C)
