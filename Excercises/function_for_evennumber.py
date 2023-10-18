def even(n):
    if n % 2 == 0:
        return n

numbers = [1,2,3,4,5,7,8,9,10]

result = list(filter(lambda n: n % 2 == 0, numbers))