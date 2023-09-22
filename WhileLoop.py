while True:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")


    repeat = input("Do you want to repeat? (yes/no): ").lower()


    if repeat != "yes":
        break  # Exit the loop if the answer is not "yes"
