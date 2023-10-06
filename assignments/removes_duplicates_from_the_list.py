numbers = [15, 20, 25, 20, 10, 5]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)
