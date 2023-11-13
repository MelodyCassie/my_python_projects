def difference_of_list(my_list_tuple):
    smallest = float('inf')
    for item in my_list_tuple:
        if item < smallest:
            smallest = item

    largest = float('-inf')
    for item_two in my_list_tuple:
        if item_two > largest:
            largest = item_two

    return largest - smallest


my_list_tuple = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
result_diff = difference_of_list(my_list_tuple)
print(result_diff)
