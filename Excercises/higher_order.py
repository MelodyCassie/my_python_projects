def bigger_odd(numbers):
    return int(max(filter(lambda n: int(n) % 2 == 1, numbers)))

print(bigger_odd('23496'))