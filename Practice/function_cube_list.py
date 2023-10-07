def cube_list(my_list):
    for i in range(len(my_list)):
        my_list[i] **= 3


numbers = [25, 68, 77, 4, 9]

cube_list(numbers)
print(numbers)