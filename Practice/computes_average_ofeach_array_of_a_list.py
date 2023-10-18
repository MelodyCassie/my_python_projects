scores = [
    [25, 50, 75],
    [40, 50, 60],
    [75, 65, 80]
]

averages = []

for row in scores:
    total_score = sum(row)
    num_scores = len(row)
    average = total_score / num_scores
    averages.append(average)

for i, avg in enumerate(averages):
    print(f"Average for array {i + 1}: {avg}")
