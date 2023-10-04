number = int(input("Enter five digit number:  "))
for number in range(1,6):
    number /= 10
    number %= 10
    number %= 10
    number %= 10
print(number, end=' ')

