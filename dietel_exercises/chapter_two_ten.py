first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))

addition = first_number + second_number + third_number
average = first_number + second_number + third_number / 3.0
product = first_number * second_number * third_number

print(addition)
print(average)
print(product)

if first_number >= second_number and first_number >= third_number:

    print('First Number Is Larger')

elif second_number >= first_number and second_number >= third_number:
    print('Second Number Is Larger')

elif third_number >= first_number and third_number >= second_number:
    print('Third Number Is Larger')
