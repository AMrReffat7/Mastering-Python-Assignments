# ---------------(Assignment 1)---------------
# Printing boolean values of different data types
print(bool(True))
print(bool("amr"))
print(bool(100))
print(bool(["amr", "ahmed"]))
print(bool(False))
print(bool(0))
print(bool())
print(bool(None))

print("=" * 40)

# ---------------(Assignment 2)---------------
# Checking if scores in html, css, and javascript are all above 50
html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)

print("=" * 50)

# ---------------(Assignment 3)---------------
# Checking if num is greater than num_one or num_two, and both num > num_one and num > num_two
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

print("=" * 50)

# ---------------(Assignment 4)---------------
# Performing mathematical operations and type conversion
num_one = 10
num_two = 20
result = num_one + num_two

print("Result:", result)

exponent = result ** 3
print("Exponent:", exponent)

modulus = exponent % 26000
print("Modulus:", modulus)

division = modulus / 5
print("Division:", division)

# Convert division result to string
final = str(division)
print("Type of final:", type(final))
