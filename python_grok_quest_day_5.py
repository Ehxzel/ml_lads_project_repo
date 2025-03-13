print("Welcome User!")

balance = 1000 #Initial Value of Customer Balance

while True:
    user_pin = int(input("Enter your PIN:_ "))
    default_pin = 1234

    if user_pin != default_pin:
        print("The PIN you entered is incorrect. Please try again :_ ")
        atm_on = True
        print("<--------------------<>-------------------->","\n")

    else:
        print("PIN Verification Successful......","\n")
        print("<--------------------<>-------------------->")
        break


#while True:

# atm_main_menu = {

# "check_balance":"1",
# "deposit_money":"2",
# "withdrawl_money":"3",
# "Exit":"4"

# }

display_message_0 = "Welcome to main menu."
display_message_1 = "To check balance, press 1"
display_message_2 = "To deposit money, press 2"
display_message_3 = "To withdrawl money, press 3"
display_message_4 = "To Exit Menu, press 4"

# print(display_message_0,"\n",display_message_1,"\n", display_message_2,"\n", display_message_3,"\n", display_message_4,"\n")
print("<--------------------<>-------------------->","\n")

while True:
    print(display_message_0,"\n",display_message_1,"\n", display_message_2,"\n", display_message_3,"\n", display_message_4,"\n")
    request = (input("Waiting for your Request:_ "))
    
    print("<--------------------<>-------------------->","\n")

    if request == str(1):
        print(f"Dear Customer, your current balance is {balance}")
        print("<--------------------<>-------------------->","\n")

    if request == str(2):
        x = int(input("Enter how much you want to deposit:_ "))
        balance = x + balance
        print(f"Amount deposited = {x}, Updated balance = {balance}")
        print("<--------------------<>-------------------->","\n")

    if request == str(3):
        print(f"Displaying your current Balance:_ {balance}")
        print("<--------------------<>-------------------->","\n")

        y = int(input("How much are you ready to withdrawl:_ "))
        if y > balance:
            print(f"Insufficient Funds, this is your current balance, {balance}")
            print("<--------------------<>-------------------->","\n")
            # break
            
        elif y <= balance and  y == balance:
            print("You're ready to proceed")
            print(f"Withdrawl Successful, current balance = {balance - y}")
            print("<--------------------<>-------------------->","\n")
            # break
            
    if request == str(4):
        print("You've exited the Main Menu.......")
        print("<--------------------<>-------------------->","\n")
        break
print("You've exited the Main Menu........")
print("Thank you for patronizing our Service........")

#All that's left now, is to modularize the Code.