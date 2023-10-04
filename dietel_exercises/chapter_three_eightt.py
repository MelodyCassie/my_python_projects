addition = 0
product = 0
for i in range(3):
    four_integers = int(input("Enter integer: "))

    addition += four_integers
print(addition)

average = addition / 4.0
print(f"average : {average:,.2f}")


for four_integers in range(3):
    product *= four_integers
print(product)

list = []
largest_number = 0

for i in range(3):
    list.append(four_integers)

for number in list:
    if number > largest_number:
        largest_number = number
print(largest_number)