even_number = [number for number in range(2, 11, 2)]
odd_number = [number for number in range(1, 11, 2)]

print(even_number)
print(odd_number)


for i in range(len(even_number)):
    print(f'{i}:{even_number[i]}')

for i in range(len(odd_number)):
    print(f'{i}:{odd_number[i]}')