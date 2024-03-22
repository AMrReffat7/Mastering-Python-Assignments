user_age = int(input("What is your age? ").strip())

# Check if the user's age is suitable for the program
message = "Unfortunately, your age is not suitable for the program" if user_age >= 30 or user_age < 18 else "This program is suitable for you"
print(message)
