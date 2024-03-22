friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif", "ola"]

# Sort the friends list in-place
friends.sort()

ignored_names_count = 0

# Iterate through each friend and print the capitalized names
for friend in friends:
    if friend[0].isupper():
        print(friend)
    else:
        ignored_names_count += 1

print(f"Ignored names count: {ignored_names_count}")
