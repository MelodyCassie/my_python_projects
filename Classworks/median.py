numbers = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20, 20]
numbers.sort()

number = len(numbers)


middle_one = numbers[number // 2]
middle_two = numbers[number // 2]
median = (middle_one + middle_two) / 2

print("Median:", median)
