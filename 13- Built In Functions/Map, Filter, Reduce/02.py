friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# Using list comprehension
names = [name for name in friends_filter if name.endswith("m")]
for name in names:
    print(name)

# Separator
print("=" * 50)

# Using filter with lambda function
names = filter(lambda item: item.endswith("m"), friends_filter)
for name in names:
    print(name)
