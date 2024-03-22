my_list = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple1 = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_tuple2 = ("L", "E", "O", 1, 2, "E", "R", "O")

# Combine elements from my_list, my_tuple1, and my_tuple2
combined_data = [item1 for item1, item2, item3 in zip(my_list, my_tuple1, my_tuple2) if not isinstance(item1, int)]

# Join the filtered elements into a single string
final_string = "".join(map(str, combined_data))

# Capitalize the first letter and make the rest lowercase
final_string = final_string.lower().capitalize()

print(final_string)  # Output: Elzero
