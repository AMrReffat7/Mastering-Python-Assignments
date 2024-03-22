try:
    user_num = input("Enter your number: ")

    if len(user_num) > 1:
        raise IndexError("Only one character is allowed.")

    if user_num == '0':
        raise ValueError("Number must be larger than '0'.")

    if not user_num.isdigit():
        raise Exception("Only numbers are allowed.")

    print("##################")
    print(f"The number is '{user_num}'")
    print("##################")

except IndexError as index_error:
    print(index_error)

except ValueError as value_error:
    print(value_error)

except Exception as exception:
    print(exception)
