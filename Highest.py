Number1 = int(input("Enter First Number: "))
Number2 = int(input("Enter Second Number: "))
Number3 = int(input("Enter Third Number: "))

if Number1 >= Number2 and Number1 >= Number3:
    print('Number1 is Greater')
if Number2 >= Number1 and Number2 >= Number3:
    print('Number2 is Greater')
if Number3 >= Number1 and Number3 >= Number2:
    print('Number3 is Greater')