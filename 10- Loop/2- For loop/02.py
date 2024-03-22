for num in range(1, 21):
    if num < 10 and num not in [6, 8, 12]:
        print(f"0{num}")
    elif num in [6, 8, 12]:
        continue
    else:
        print(num)

print("All numbers have been printed.")
