# ---------------(Assignment 1)---------------
# Prompt user for their name and greet them
user_name = input("What's your name? ").strip().capitalize()

print(f"Hello {user_name}, Happy To See You Here.")

print("=" * 50)

# ---------------(Assignment 2)---------------
# Prompt user for their age and provide a message based on their age
user_age = int(input("How old are you? ").strip())

if user_age < 16:
    print("Hello, You're under 16. Some articles may not be suitable for you.")
else:
    print(f"Hello, You're {user_age} years old. All articles are suitable for you.")

print("=" * 50)

# ---------------(Assignment 3)---------------
# Prompt user for their first and second names and greet them
first_name = input("What's your first name? ").strip().capitalize()
second_name = input("What's your second name? ").strip().capitalize()

print(f"Hello, {first_name} {second_name[0]}.")

print("=" * 50)

# ---------------(Assignment 4)---------------
# Prompt user for their email address and extract username, email service provider, and top-level domain
user_email = input("Email Address? ").strip().lower()

username = user_email[:user_email.index('@')].capitalize()
email_provider = user_email[user_email.index('@')+1:user_email.index('.')]
top_level_domain = user_email[user_email.index('.')+1:]

print(f"Your username Is {username}")
print(f"Email Service Provider Is {email_provider}")
print(f"Top Level Domain Is {top_level_domain}")
