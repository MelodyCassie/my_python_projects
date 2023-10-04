number = int(input("Enter number: "))

original_number = number
reversed_number = 0
ten = 10

while number > 0:
    last_digit = number % 10
    reversed_number = reversed_number * 10 + last_digit
    number //= 10

if original_number == reversed_number:
    print("This is a palindrome: ", original_number)

else:
    print("not a palindrome! ", original_number)
