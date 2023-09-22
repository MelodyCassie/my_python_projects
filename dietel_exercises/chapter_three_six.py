input("What is your problem? (Press Enter)")

user_response = input("Have you had this problem before (yes or no)? ")

if user_response.lower() == "yes":
    print("Well, you have it again.")
elif user_response.lower() == "no":
    print("Well, you have it now.")
else:
    print("Invalid input. Please enter 'yes' or 'no' for the second question.")
