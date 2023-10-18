def biggest_odd(numbers):
    numbers = list(map(int, numbers))  # Convert the input string to a list of integers
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))  # Filter out the odd numbers
    largest_odd = max(odd_numbers, default=0)  # Find the largest odd number

    return str(largest_odd)  # Convert the result back to a string

numbers = '23569'
result = biggest_odd(numbers)
print(f"The largest odd number is: {result}")
