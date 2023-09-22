deposit = float(input("Enter your amount"))

for x in range(1,31):
    roi = deposit * 0.10
    new_amount = deposit * roi
    deposit = new_amount
    print(f"Your ROI is ${roi: 2f} your investment is now ${new_amount}")
