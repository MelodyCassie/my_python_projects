scores = [
    [25, 50, 75],
    [40, 50, 60],
    [75, 65, 80]
]
averages = []

for rows in scores:
    sum_of_rows = sum(rows)
    length_of_rows = len(rows)

    average = sum_of_rows / length_of_rows
    averages.append(average)

for i, ave in enumerate(averages):
    print(f'THE AVERAGE OF ROW  {i + 1} is {[ave]}')

