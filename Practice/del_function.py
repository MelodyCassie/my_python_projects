numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del numbers[-2]
print(numbers)

numbers_two = list(range(1, 16))
del numbers_two[0:4]
print(numbers_two)

del numbers_two[0:15]
print(numbers_two)