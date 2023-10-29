def divide_list():
    sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]

    middle = len(sample_input) // 2

    first_half = sample_input[:middle]
    second_half = sample_input[middle:]

    return first_half, second_half



sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
divided_list = divide_list()
print(divided_list)
