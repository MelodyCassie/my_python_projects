def print_even_position_elements(lst):
    for i in range(1, len(lst), 2):
        print(lst[i])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_position_elements(my_list)
