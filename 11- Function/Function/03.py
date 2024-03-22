def member_skills(name="", *skills):
    if not name:
        name = "Unknown"

    if not skills:
        print(f"Hello {name}, you have no skills to show.")
    else:
        print(f"Hello {name}, your skills are:")
        for skill in skills:
            print(f"- {skill}")

# Taking user input
user_name = input("What's your name? ").strip().capitalize()
user_skills = input("Enter your skills, separated by space: ").split()

# Calling the function with user input
member_skills(user_name, *user_skills)

# Calling the function without arguments
member_skills()
