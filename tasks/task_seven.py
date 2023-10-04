input("Enter 10 valid scores between 1-100 only ")

zero = 0
addition = 0
total_scores = 10

for count in range(10):
    scores = int(input("Enter a score: "))
    if scores >= 1 and scores <= 100:
        addition += scores
    else:
        print("invalid sum is:  ", zero)
print("sum of valid scores is : ", addition)
