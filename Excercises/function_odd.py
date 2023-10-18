def biggest_odd(numbers):
    largest_odd = '0'

    for num in numbers:
        if num > largest_odd and int(num) % 2 != 0:
            largest_odd = max([num for num in numbers if num > largest_odd and int(num) % 2 != 0], default='0')

            largest_odd = num

    return largest_odd


numbers = '23569'
result = biggest_odd(numbers)
print(f"The largest odd number is: {result}")
