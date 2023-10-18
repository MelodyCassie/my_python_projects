def test_for_largest_even_number():
    for num in numbers:
        if int(num) % 2 == 0:
            return num


numbers = '23569'
result = test_for_largest_even_number(numbers)
print(result)
