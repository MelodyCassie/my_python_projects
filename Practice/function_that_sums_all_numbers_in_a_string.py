def check_for_number(the_strings):
    count = 0
    for each_value in the_strings:
        for number in each_value:

         if number >= '0' and number <= '9':
             count += 1

    return count


sum_of_numbers = check_for_number('pretty melody1234')
print(sum_of_numbers)
