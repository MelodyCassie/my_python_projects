def my_index(li: list, n):
    idx = 0
    for i in range(len(li)):
        if li[i] == n:
            idx = i
        return idx

numbers = [1, 2, 3, 3, 4, 3, 2, 5, 5]
print(numbers)
print(my_index(numbers, -3))