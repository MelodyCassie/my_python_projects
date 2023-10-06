print("WELCOME TO YOUR NOKIA PHONE")
first_menu = input(""" WELCOME TO YOUR NOKIA PHONE
                    1. Phone book
                    2. Messages
                    3. Chat
                    4. Call Register
                    5. Tones
                    6. Settings
                    7. Call Divert
                    8. Games
                    9. Calculator
                    10. Reminder
                    11. Clock
                    12. Profiles
                    13. SIM Services
                    CHOOSE FROM THE OPTIONS ABOVE :""")

if first_menu == 1:
    phone_book = input("""
                1. Search
                2, Service nos
                3. Add Name
                4. Erase
                5. Edit
                6. Assign Tone
                7. Send B' card
                8. Options
                9. Speed Dials
                10. Voice Tags
                CHOOSE FROM THE OPTIONS ABOVE: """)

    if phone_book == 1:
        print('Search')

    if phone_book == 2:
        print("Service No")

    if phone_book == 3:
        print('Add Name')

    if phone_book == 4:
        print('Erase')

    if phone_book == 5:
        print("Edit")

    if phone_book == 6:
        print("Assign Tone")

    if phone_book == 7:
        print("Send B' card")

    if phone_book == 8:
        print("""
      1. Type of view
      2. Memory status
       """)

if first_menu == 2:
    message_container = input("""  
                        1.Write Message
                        2.Inbox
                        3.outbox
                        4.Picture Messages
                        5.Templates
                        6.Smileys
                        7.Message Settings""")

    if message_container == 2:
       print("""
         inbox SET
         1.Message center number
         2.Message sent as
         3.Message validity
         """)
    if message_container == 3:
       print("""
        outbox COMMON
         1.Delivery reports
         2.Reply via same center
         3.Character report
         4.Info service
         5.Voice mailbox number
         6.Service command editor
         """)

if first_menu == 3:
    print("Chats")

if first_menu == 4:
    call_register = input("""
    CALL REGISTER 
    1.Missed calls
    2.Received calls
    3.Dialed number
    4.Erase recent calls
    5.Show call duration
    """)
    if call_register == 1:
     print("You have millions of contacts on your register ")

    if call_register == 2:
     print("You have millions of received calls, you are a celebrity you know!!! ")

    if call_register == 3:
     print("you've dialed millions of contacts")

    if call_register == 4:
     print("you have erased all your contacts successfully")

    if call_register == 5:
     print("""1.Last call duration
             2.All calls' duration
             3.Received calls' duration
             4.Dialed calls' duration
             5.Clear timer
    """)

if first_menu == 5:
    print("tones")

if first_menu == 6:
    print("Settings")

if first_menu == 7:
    print("Call divert")

if first_menu == 8:
    print("Games")

if first_menu == 9:
    print("Calculator")

if first_menu == 10:
    print("Reminder")

if first_menu == 11:
    print("Clock")

if first_menu == 12:
    print("Profiles")

if first_menu == 13:
    print("SIM services")
