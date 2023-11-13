def two_list_to_dictionary(my_list_one, my_list_two):
    new_dict = {}
    for item_one, item_two in zip(my_list_one, my_list_two):
        new_dict[item_one] = item_two
    return new_dict


my_list_one = ['a', 'b', 'c', 'd', 'e']
my_list_two = [1, 2, 3, 4, 5]

result_new_dict = two_list_to_dictionary(my_list_one, my_list_two)
print(result_new_dict)
