def print_odd_position_elements(lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            print(lst[i])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_odd_position_elements(my_list)
