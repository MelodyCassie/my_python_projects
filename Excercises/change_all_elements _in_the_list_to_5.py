list = [[1,2,3,4,5,6,7,8,9,10]]


for i, value in enumerate(list):
    for j, _ in enumerate(value):
        list[i][j] = 5
        print(list, end= ' ')