# ---------------(Assignment 1)---------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Accessing and removing elements using list indexing and pop method
print(friends[0])               # 1st method
print(friends.pop(0))           # 2nd method
print(friends[-1])              # 1st method
print(friends.pop(-1))          # 2nd method

print("=" * 50)

# ---------------(Assignment 2)---------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Slicing the list to print alternate elements
print(friends[::2])
print(friends[1::2])

print("=" * 50)

# ---------------(Assignment 3)---------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Slicing the list to print specific ranges of elements
print(friends[1:4])
print(friends[-2:])

print("=" * 50)

# ---------------(Assignment 4)---------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Replacing elements in the list
friends[3:5] = ['Elzero', 'Elzero']

print(friends)

print("=" * 50)

# ---------------(Assignment 5)---------------
friends = ["Osama", "Ahmed", "Sayed"]

# Inserting and appending elements to the list
friends.insert(0, "Ali")
print(friends)

friends.append("Gamal")
print(friends)

print("=" * 50)

# ---------------(Assignment 6)---------------
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Removing specific elements from the list
friends.remove("Nasser")
friends.remove("Osama")
print(friends)

friends.remove("Salem")
print(friends)

print("=" * 50)

# ---------------(Assignment 7)---------------
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Extending the list with elements from other lists
friends.extend(employees)
friends.extend(school)

print(friends)

print("=" * 50)

# ---------------(Assignment 8)---------------
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Sorting the list alphabetically
friends.sort()
print(friends)

friends.sort(reverse=True)
print(friends)

print("=" * 50)

# ---------------(Assignment 9)---------------
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Getting the length of the list
print(len(friends))

print("=" * 50)

# ---------------(Assignment 10)---------------
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Accessing nested lists
print(technologies[-1][0])
print(technologies[-1][-1])

print("=" * 50)

# ---------------(Assignment 11)---------------
my_list = [1, 2, 3, 3, 4, 5, 1]

# Removing specific elements and sorting the list
my_list.remove(1)
my_list.remove(3)
my_list.sort()
unique_list = my_list

print(unique_list)
print(type(unique_list))
print(unique_list[:4])
