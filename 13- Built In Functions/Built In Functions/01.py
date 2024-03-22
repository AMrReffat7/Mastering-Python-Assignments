values = (0, 1, 2)

# Check if any value in `values` is True
if any(values):
    my_var = 0

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# Check if all elements of my_list are True
if all(my_list):
    print("Good")
else:
    print("Bad")
