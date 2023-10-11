number_one = 0
number_two = 1

result = number_one + number_two

print(number_one, number_two, number_two, end=" ")

for number in range(1, 51):
    number_one, number_two = number_two, result
    result = number_one * number_two
    if result < 50:
        print(result, end='' )