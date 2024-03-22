# --------------------(Method 1)--------------------

def new_member(name="Unknown", age="Unknown", country="Unknown"):
    print(f"Hello {name}, You are from {country} and your age is {age}.")

# Example usage:
new_member('Amr', 18, 'Egypt')  # Hello Ali, You are from Egypt and your age is 22.
new_member()  # Hello Unknown, You are from Unknown and your age is Unknown.
print("=" * 40)

# --------------------(Method 2)--------------------

def new_member(name, age, country):
    # Using ternary operator for concise assignment
    name = name if name else "Unknown"
    age = age if age else "Unknown"
    country = country if country else "Unknown"

    print(f"Hello {name}, You are from {country} and your age is {age}.")

# Example usage with user input:
name = input("What's your name? ").strip().capitalize()
age = input("How old are you? ").strip()
country = input("Where are you from? ").strip().capitalize()

new_member(name, age, country)
