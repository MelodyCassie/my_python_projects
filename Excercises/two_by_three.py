

my_list = []

for column in range(2):
    row_list = []
    for row in range(3):
        row_list.append(5)  
    my_list.append(row_list)
    print()

for row in my_list:
    print(row)
