sentinel = 0
user_input = 0

while user_input != sentinel:
    user_input = int(input("Enter a number: ",("type 0 to exit")))
    if user_input != sentinel:
        result = user_input * user_input
        print(result)
