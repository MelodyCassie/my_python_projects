binary_str = input("Enter a binary number: ")

decimal_value = 0


for i in range(len(binary_str) - 1, -1, -1):

    if binary_str[i] == '1':
        decimal_value += 2 ** (len(binary_str) - 1 - i)

print("Decimal equivalent:", decimal_value)
