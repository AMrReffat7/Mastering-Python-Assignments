User_num = int(input('Enter your number: '))

# Check if the input number is greater than 0
if User_num > 0:
    num = User_num

    # Print numbers in descending order
    while num > 1:
        num -= 1
        print(num)

    # Print the count of numbers printed successfully
    print(f"{User_num - 1} numbers printed successfully.")

else:
    # Print a message if the input number is not greater than 0
    print(f"Number {User_num} isn't larger than 0")
