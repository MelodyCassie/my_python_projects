my_dict = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}

sorted_dict_ascending = (sorted(my_dict.items()))
print("Ascending order:", sorted_dict_ascending)


for key, value in sorted_dict_ascending:
    print(f"{key}: {value}", end="  ")







my_dict = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}
sorted_dict_descending = sorted(my_dict.items(), reverse=True)
print("Descending order:", sorted_dict_descending)

