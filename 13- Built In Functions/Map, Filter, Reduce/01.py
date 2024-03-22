friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# Using list comprehension
modified_texts = [name[1:-1] for name in friends_map]
for name in modified_texts:
    print(name)

# Separator
print("=" * 50)

# Using map with lambda function
modified_texts = map(lambda item: item[1:-1], friends_map)
for name in modified_texts:
    print(name)
