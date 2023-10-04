def compute_running_total(numbers):
    running_total = []
    total = 0

    for number in numbers:
        total += number
        running_total.append(total)

    return running_total

numbers = [1, 2, 3, 4, 5]
result = compute_running_total(numbers)
print("Running Total:", result)
