def add_key_value(my_dictionary, key, value):
    my_dictionary[key] = value


my_dict = {0: 10, 1: 20}
add_key_value(my_dict, 2, 30)
print(my_dict)

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)
