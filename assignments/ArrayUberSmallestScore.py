list = []
smallest_number = 0

for count in range(10):
    scores = int(input("Enter score: "))
    list.append(scores)

for number in list:
    if number < smallest_number:
        smallest_number = number
print("smallest numberi is  " ,smallest_number)
