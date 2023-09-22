ordinal_numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
gifts = [
    "a partridge in a pear tree",
    "two turtle doves",
    "three French hens",
    "four calling birds",
    "five golden rings",
    "six geese a-laying",
    "seven swans a-swimming",
    "eight maids a-milking",
    "nine ladies dancing",
    "ten lords a-leaping",
    "eleven pipers piping",
    "twelve drummers drumming"
]

for day in range(12):
    print(f"On the {ordinal_numbers[day]} day of Christmas,")
    print("My true love gave to me:")
    for i in range(day, -1, -1):
        if i == 0 and day != 0:
            print("And", end=" ")
        print(gifts[i])
    print()
