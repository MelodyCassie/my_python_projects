group_of_values = [1, 2, 3, 4, 5]

specified_value = int(input("Enter the value to check: "))

if specified_value in group_of_values:
    print(f"{specified_value} is in the group of values.")
else:
    print(f"{specified_value} is not in the group of values.")
