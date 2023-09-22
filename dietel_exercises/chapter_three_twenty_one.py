purchase_price = float(input("Enter the purchase price (in dollars or less): "))


purchase_price_cents = int(purchase_price * 100)


change_cents = 100 - purchase_price_cents

quarters = change_cents // 25
change_cents %= 25

dimes = change_cents // 10
change_cents %= 10

nickels = change_cents // 5
change_cents %= 5

pennies = change_cents

print("Your change is:")
if quarters > 0:
    print(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
if dimes > 0:
    print(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
if nickels > 0:
    print(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
if pennies > 0:
    print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")
