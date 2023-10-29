def calculate_average(array_of_numbers):
    addition = sum(array_of_numbers)
    length = len(array_of_numbers)

    if length == 0:
     return 0

    average = addition / length
    return average


result = calculate_average([1,2,3,4,5,6])

print(result)