# ---------------(Assignment 1)---------------

name = "Amr Reffat"
age = 18
country = "Egypt"

# Using f-strings for better readability and interpolation
print(f'Hello {name}, How are you doing? """ Your age is "{age}" + Your country is:{country}')

print("="*50)

# ---------------(Assignment 2)---------------

# Same as Assignment 1

# ---------------(Assignment 3)---------------

name = "amro"

# Using f-strings for better readability and interpolation
print(f'Second Letter Is "{name[1]}"')
print(f'Third Letter Is "{name[2]}"')
print(f'Last  Letter Is "{name[-1]}"')

print("="*50)

# ---------------(Assignment 4)---------------

# Same as Assignment 3

# ---------------(Assignment 5)---------------

name = "#@#@Amro#@#@"

# Using strip to remove specified characters from both ends of the string
print(name.strip("#@"))

print("="*50)

# ---------------(Assignment 6)---------------

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

# Using zfill to pad numbers with zeros to ensure they are of the specified width
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

print("="*50)

# ---------------(Assignment 7)---------------

name_one = "Amr"
name_two = "Amr_Reffat"

# Using rjust to right-justify strings with specified width and fill character
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

print("="*50)

# ---------------(Assignment 8)---------------

name_one = "MoUstaFa"
name_two = "osaMA"

# Using swapcase to swap cases of characters in the string
print(name_one.swapcase())
print(name_two.swapcase())

print("="*40)

# ---------------(Assignment 9)---------------

msg = "I Love Python And, I Love Elzero Web School"

# Using count to count occurrences of a substring in a string
print(msg.count('Love'))

print("="*50)

# ---------------(Assignment 10)---------------

name = "Amr"

# Using index to find the index of the first occurrence of a substring in a string
print(name.index('i'))

print("="*50)

# ---------------(Assignment 11)---------------

msg = "I Love Python And, I Love Elzero Web School"

# Using replace to replace occurrences of a substring with another substring in a string
print(msg.replace('Love', '<3', 1))

print("="*50)

# ---------------(Assignment 12)---------------

msg = "I <3 Python And Although <3 Elzero Web School"

# Using replace to replace occurrences of a substring with another substring in a string
print(msg.replace('<3', 'Love'))

print("="*50)

# ---------------(Assignment 13)---------------

# Same as Assignment 1
