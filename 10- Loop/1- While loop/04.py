my_friends = []
remaining_slots = 4

while remaining_slots > 0:
    name = input("What's your friend's name? ").strip()

    # Check if the name is valid
    if name and name[0].isupper() and name[1:].islower():
        my_friends.append(name)
        print(f"Your friend: {name} added")
        remaining_slots -= 1
    else:
        print('Invalid name. Please enter a valid name (first letter capital, rest lowercase).')

print("List of friends:")
print(my_friends)
