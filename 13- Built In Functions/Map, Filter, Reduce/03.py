from functools import reduce

nums = [2, 4, 6, 2]

# Using reduce with lambda function
result = reduce(lambda num1, num2: num1 * num2, nums)
print(result)
