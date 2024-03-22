try:
    user_letter = input("Enter a letter from A to Z: ")

    if len(user_letter) != 1:
        raise IndexError("You must input exactly one character.")

    if 'A' <= user_letter <= 'Z':
        print(f"You typed '{user_letter}'.")
    else:
        raise ValueError("The letter is not between A and Z.")

except IndexError as index_error:
    print(index_error)

except ValueError as value_error:
    print(value_error)
