user_input = int(input("Enter five numbers: "))

integer_one = user_input // 10000
integer_two = user_input // 1000 % 10
integer_three = user_input // 100 % 10
integer_four = user_input // 10 % 10
integer_five = user_input % 10

print(integer_one,   integer_two,   integer_three,   integer_four,   integer_five)