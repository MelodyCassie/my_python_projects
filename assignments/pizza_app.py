print("""
                <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                
                                                  WELCOME TO MELLY'S PIZZA APP!!
                                                  
                <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>  

""")

while True:
    response = input('Can i take your order? \n (Yes or No) ')

    if response.lower() == 'yes':
        size_of_pizza = input('What size of pizza do you want to buy? \n (Large, Medium or Small) \n')

        if size_of_pizza.lower() == 'large':
            number_of_guest_for_large_pizza = input(int('What number of guest are you expecting? '))

            if number_of_guest_for_large_pizza > 0:
                super_hungry_people_for_large_pizza = input(int('How many people are super hungry from the ' + number_of_guest_for_large_pizza + ' guests you are expecting? '))

                if super_hungry_people_for_large_pizza > 0 and super_hungry_people_for_large_pizza <= number_of_guest_for_large_pizza:
                    slices_per_super_hungry = input(int('How many slices will each super hungry guest eat? '))





    elif response.lower() == "no":
        print('Alright!\n Have a nice day.')
