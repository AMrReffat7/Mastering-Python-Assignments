v = 1

while v < 1000:
    my_range = list(range(v))
    # Instead of converting the range to a list, you can directly calculate the sum
    if (v * (v - 1) // 2 + v) + pow(v, v, v) == 820:
        print(f"v = {v}")
        break
    v += 1
