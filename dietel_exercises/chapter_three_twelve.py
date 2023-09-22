num = int(input("Enter a five-digit integer: "))

if 10000 <= num <= 99999:

    digit1 = num // 10000
    digit2 = (num // 1000) % 10
    digit3 = (num // 100) % 10
    digit4 = (num // 10) % 10
    digit5 = num % 10

    if digit1 == digit5 and digit2 == digit4:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
else:
    print("Input is not a five-digit integer.")
