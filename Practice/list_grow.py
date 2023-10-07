list_one = [1, 2, 3, 4]
list_two = [number for number in range(5, 11)]
list_one += list_two
print(list_one)


combined_list = list_one + list_two
print(combined_list)

even_number = [number for number in range(2, 11, 2)]
odd_number = [number for number in range(1, 11, 2)]

print(even_number)
print(odd_number)


for i in range(len(even_number)):
    print(f'{i}:{even_number[i]}')
