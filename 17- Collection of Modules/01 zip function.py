my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

# Combine elements from my_list and my_tuple into strings and append them to my_data
for data in zip(my_list, my_tuple):
    my_data.append("".join(map(str, data)))

# Join the strings in my_data into a single string
final_string = "".join(my_data)

# Capitalize the first letter and make the rest lowercase
final_string = final_string.lower().capitalize()

print(final_string)  # Output: Elzero
