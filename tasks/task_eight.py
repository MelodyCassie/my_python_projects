addition  = 0
stop = 0
for count in range(10):
    score = int(input("Enter a number: "))
    if score == stop:
        break
    else:
        addition += score
print(addition)