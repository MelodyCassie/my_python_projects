numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers[1:15:2])

del numbers[0:3]
print(numbers)

del numbers[::2]
print(numbers)

numbers[6:9] = [0,0,0,0]
print(numbers)

numbers[5:16] = []
print(numbers)

numbers[0:15] = []
print(numbers)

