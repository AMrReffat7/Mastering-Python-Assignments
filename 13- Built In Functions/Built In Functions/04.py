def my_all(items):
    """
    Returns True if all elements in the iterable are True, otherwise False.
    """
    for item in items:
        if not item:
            return False
    return True

def my_any(items):
    """
    Returns True if any element in the iterable is True, otherwise False.
    """
    for item in items:
        if item:
            return True
    return False

def my_min(items):
    """
    Returns the smallest element in the iterable.
    """
    if not items:
        raise ValueError("min() arg is an empty sequence")
    min_val = items[0]
    for item in items[1:]:
        if item < min_val:
            min_val = item
    return min_val

def my_max(items):
    """
    Returns the largest element in the iterable.
    """
    if not items:
        raise ValueError("max() arg is an empty sequence")
    max_val = items[0]
    for item in items[1:]:
        if item > max_val:
            max_val = item
    return max_val

# Test cases
print(my_all([1, 2, 3]))         # True
print(my_all([1, 2, 3, []]))      # False

print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))     # False

print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100

print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
