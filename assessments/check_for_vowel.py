word = input('Enter a word: ')

vowels = ["a", "e", "i", "o", "u"]

found_vowel = False

for vowel in vowels:
    if vowel in word:
        found_vowel = True
        break

if found_vowel:
    print("The word entered has a vowel in it.")
else:
    print("The word entered does not have a vowel.")
