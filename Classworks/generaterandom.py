import random

number = int(input("Guess a number: "))
generate = random.randint(1, 10)


while number != generate:
      print("wrong")
      number = int(input("Guess a number: "))


if number == generate:
    print("you won")

