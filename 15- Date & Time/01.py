import datetime

# Get the current date
current_date = datetime.datetime.now()

# Specify the specific date
specific_date = datetime.datetime(2027, 8, 1)

# Calculate the number of days between the specific date and the current date
days_difference = (current_date - specific_date).days

# Print the number of days
print(f"Number Of Days From '2021-06-25' To The Current date Is => {days_difference} days")
