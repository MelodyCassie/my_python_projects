data = [1, 2, 3, 4, 5, 6]

sorted_data = sorted(data)
n = len(sorted_data)

if n % 2 == 0:
    middle1 = sorted_data[n // 2 - 1]
    middle2 = sorted_data[n // 2]
    median = (middle1 + middle2) / 2
    print(f"Median: {median} (averaging {middle1} and {middle2})")
else:
    median = sorted_data[n // 2]
    print(f"Median: {median}")
