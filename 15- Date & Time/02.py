import datetime

# Get current date and time
current_datetime = datetime.datetime.now()

# ---------------(DATE)---------------

# YYYY-MM-DD
print(current_datetime.strftime("%Y-%m-%d"))

# Abbreviated month, day, year
print(current_datetime.strftime("%b %d, %Y"))

# Day, abbreviated month, year
print(current_datetime.strftime("%d-%b-%Y"))

# Day, abbreviated month, two-digit year
print(current_datetime.strftime("%d/%b/%y"))

# Abbreviated weekday, day, full month name, year
print(current_datetime.strftime("%a, %d %B %Y"))

# Locale's appropriate date representation
print(current_datetime.strftime("%x"))


# ---------------(TIME)---------------

# Hour:Minute:Second AM/PM (without leading zero)
print(current_datetime.strftime("%-I:%M:%S %p"))

# Locale's appropriate time representation (24-hour clock)
print(current_datetime.strftime("%X"))


# ---------------(DATE & TIME)---------------

# Locale's appropriate date and time representation
print(current_datetime.strftime("%c"))
