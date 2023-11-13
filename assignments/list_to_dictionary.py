def list_to_dictionary(my_list, key, value):
    my_dict = {}
    for item in my_list:
        my_dict[item[key]] = item[value]
    return my_dict


my_list = [{'key': 'a', 'value': 'apple'},
           {'key': 'b', 'value': 'banana'},
           {'key': 'c', 'value': 'coconut'}]

result_dict = list_to_dictionary(my_list, 'key', 'value')
print(result_dict)
