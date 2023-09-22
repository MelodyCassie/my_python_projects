user_input = input("Enter a five-digit integer: ")

if len(user_input) != 5 or not user_input.isdigit():
    print("Please enter a valid five-digit integer.")
else:
    for digit in user_input:
        print(digit, end="   ")
