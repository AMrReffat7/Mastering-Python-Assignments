my_friends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_people: list) -> None:
    """
    Says hello to each member of the list.

    Parameters:
        some_people (list): A list containing names of people to greet.

    Returns:
        None
    """
    for someone in some_people:
        print(f"Hello {someone}")


say_hello(my_friends)
