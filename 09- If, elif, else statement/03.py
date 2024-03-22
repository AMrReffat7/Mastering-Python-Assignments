user_age = int(input("What is your age? ").strip())

# Calculate age in different units
months = user_age * 12
weeks = months * 4
days = user_age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Check if the age is within a reasonable range
if 10 <= user_age <= 100:
    print(f"Your Age In months Is {months:,} months")
    print(f"Your Age In weeks Is {weeks:,} weeks")
    print(f"Your Age In days Is {days:,} days")
    print(f"Your Age In hours Is {hours:,} hours")
    print(f"Your Age In minutes Is {minutes:,} minutes")
    print(f"Your Age In seconds Is {seconds:,} seconds")
else:
    print("Your age is out of range")
