card_number = ''

card_number = input('Hello, Kindly enter your card details to verify')

if len(card_number) == 13 and len(card_number) == 16:
    print('Card Number Added Successfully!')

else:
    print('Invalid Card')


first_number = int(card_number[0])

if first_number == 4:
    print('Visa Card')

elif first_number == 5:
    print('Master Card')

elif first_number == 6:
    print('Discover Card')


first_two_numbers = int(card_number[0][1])
if card_number == 37:
    print('American Express Card')

print(card_number)

print(len(card_number))


for i in range(len(card_number))-2 -1 -2:
 pass
