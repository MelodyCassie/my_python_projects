number_of_passes = 0
number_of_failure = 0

user_input = int (input('ENTER EITHER 1 OR 2: '))

while True:
 print('continue entering a number: ')
 number_of_passes += user_input

#except:
#user_input != 1 and user_input != 2:
print('continue to enter a number: ')
user_input += user_input

print(f"{number_of_passes}, {number_of_failure}")
