def check_if_palindrome(number):
    original_number = number
    reverse_number = 0
    while number != 0:
        last_digit = number % 10
        reverse_number = reverse_number * 10 + last_digit
        number //= 10
    if original_number == reverse_number:
       return True
    else:
       return False


print(check_if_palindrome(111111111111111))
