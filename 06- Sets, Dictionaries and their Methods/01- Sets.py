# ---------------(Assignment 1)---------------
# Set operations: union, update
nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Union of two sets using | operator and union() method
print(nums | letters)
print(nums.union(letters))

# Update nums set with the elements of letters set
nums.update(letters)
print(nums)

print("=" * 50)

# ---------------(Assignment 2)---------------
# Set manipulation: clear, add, discard
my_set = {1, 2, 3}

print("Initial set:", my_set)

# Clear the set
my_set.clear()
print("Cleared set:", my_set)

# Add elements to the set
my_set.add("A")
my_set.add("B")

# Discard an element (if present)
my_set.discard("C")
print("Modified set:", my_set)

print("=" * 50)

# ---------------(Assignment 3)---------------
# Set operations: issubset
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Check if set_one is a subset of set_two
print("Is set_one a subset of set_two?", set_one.issubset(set_two))
