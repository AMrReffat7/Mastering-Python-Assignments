max_value = max(0, 3, 10, 2, -100, -23, 9)

# Calculate the sum of the range using the arithmetic sum formula
# n * (n + 1) / 2
# Check for values of 'n' where the rounded average equals the maximum value
for n in range(1, 1000):
    if round(n * (n + 1) / (2 * n)) == max_value:
        print(f"'n' may be => {n}")
