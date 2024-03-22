# ---------------(Assignment 1)---------------
# Printing the types of different numeric values
print(type(5))
print(type(5.5))
print(type(5+6j))

print("="*50)  # Separator for clarity

# ---------------(Assignment 2)---------------
# Printing the real and imaginary parts of a complex number
my_complex_number = 1+2j

print("Imaginary part:", my_complex_number.imag)
print("Real part:", my_complex_number.real)

print("="*50)  # Separator for clarity

# ---------------(Assignment 3)---------------
# Printing a floating-point number with 10 decimal places
num1 = 10

print("Formatted number:", "{:.10f}".format(num1))

print("="*50)  # Separator for clarity

# ---------------(Assignment 4)---------------
# Converting a floating-point number to an integer
num = 159.650

num2 = int(num)
print("Converted integer:", num2)
print("Type of converted integer:", type(num2))

print("="*50)  # Separator for clarity

# ---------------(Assignment 5)---------------
# Various arithmetic operations
print("100 - 115 =", 100 - 115)
print("50 * 30 =", 50 * 30)
print("21 % 4 =", 21 % 4)
print("110 / 11 =", 110 / 11)
print("97 // 20 =", 97 // 20)
