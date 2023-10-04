list = []
largest_number = 0

for i in range(10):
    scores = int(input("Enter Scores: "))
    list.append(scores)

for number in list:
    if number > largest_number:
        largest_number = number
print("The Largest Number is:  ", largest_number)
