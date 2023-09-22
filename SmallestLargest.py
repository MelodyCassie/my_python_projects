
largest = float('-inf')
smallest = float('inf')

while True:
    try:

        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input.lower() == 'done':
            break


        number = float(user_input)


        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")

print(f"The largest number entered is: {largest}")
print(f"The smallest number entered is: {smallest}")
