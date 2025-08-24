balance = 100000

while True:
    welcome = input("Dear Customer, Welcome to Wealth Bank...\nKindly dial *349# to proceed: ")
    print("\nWealth, in a just a blink....\n\n1. Transfer\n2. Airtime & Data\n3. Betting & Utilities\n4. Check Balance\n5. Add money\n6. Withdraw\n7. Card")

    user_input = int(input(f"\nKindly choose from the above options to proceed: "))

    if user_input == 1:
        Transfer = (f"\nYou just chose option 1 (Transfer)...\n1. Transfer to Wealth Account\n2. Transfer to other Bank Account\n00. Back")
        print(Transfer)
        
        Transfer_input = int(input(f"\nKindly choose from the above options to proceed: "))
        
        if Transfer_input == 1:
            wealth_account = int(input("Kindly input the wealth account number: "))
            wealth_amount = int(input("Kindly input how much you would like to transfer: "))
            wealth_PIN = int(input("Kindy enter your 4-digit PIN: "))
            print("Your transfer was successful")
        
        elif Transfer_input == 2:
            other_account = int(input("Kindly input the bank account number: "))
            price = int(input("Kindly input how much you would like to transfer: "))
            Transfer_PIN = int(input("Kindy enter your 4-digit PIN: "))
            print("Your transfer was successful")
            break
        elif Transfer_input == 00:
            print(welcome)
        
        else: print(f"There was an error!!! Try again...")

    elif user_input == 2:
        Airtime_and_Data_input = int(input("Select an option. \n1. Airtime\n2. Data\n00. Back to main menu\nNow input option: "))
        if Airtime_and_Data_input == 1:
            airtime_number = input("Enter Phone Number: ")
            airtime_amount = float(input("Enter amount: "))
            airtime_PIN = int(input(f"You are sending ₦{airtime_amount} to {airtime_number}.\nPress your PIN to proceed or 0 to Cancel: "))
            
            if airtime_PIN == 0:
                print("Cancelled")
            else:
                print("Airtime purchased successfully")
        
        elif Airtime_and_Data_input == 2:
            data_number = input("Enter Phone Number: ")
            data_amount = float(input("Enter amount: "))
            data_PIN = int(input(f"You are sending ₦{data_amount} to {data_number}.\nPress your PIN to proceed or 0 to Cancel: "))
            if data_PIN == 0:
                print("Cancelled")
            else:
                print("Airtime purchased successfully")
            break
        elif Airtime_and_Data_input == 00:
            print(welcome)

    elif user_input == 3:
        Betting_and_Utilities_Option = int(input("Select option\n1. Betting\n2. Electricity\n3. Solar\n00. Back to main menu.\n Kindly choose from the options above: "))
        if Betting_and_Utilities_Option == 1:
            Betting_Provider = int(input("Select Betting Provider:\n1. iLOTBet\n2. AccessBET\n3. BetWinner\n4. PariPulse\n5. Yipeebet\n6. SportyBet\n7.Bangbet\n00. Back to main menu.\n Kindly choose from the options above: "))
            print("Successful")
        elif Betting_and_Utilities_Option == 2:
            Electricity_Provider = int(input("Select Betting Provider:\n1. Ibadan\n2. Jos\n3. Abeokuta\n4. Osun\n5. Ekiti\n6. Gombe\n7. Adamawa\n00. Back to main menu.\n Kindly choose from the options above: "))
            print("Successful")
        elif Betting_and_Utilities_Option == 3:
            Solar_Provider = int(input("Select Solar Provider:\n1. Ibadan\n2. Jos\n3. Abeokuta\n4. Osun\n5. Ekiti\n6. Gombe\n7. Adamawa\n00. Back to main menu.\n Kindly choose from the options above: "))
            print("Successful")
            break
        elif Betting_and_Utilities_Option == 00:
            print(welcome)

        else:
            print("Cancelled")

    elif user_input == 4:
        balance_option = int(input("Kindly input your 4-digit pin to proceed: "))
        print(f"Your current balance is ₦{balance}")

    elif user_input == 5:
        add_money_option = int(input("How much would you like to add? :"))
        new_balance = int(add_money_option + balance)
        update_new_balance = float(new_balance)
        reupdate_new_balance = f"{update_new_balance:,}"
        print(f"You have successfully added ₦{add_money_option}.\n\tTherefore, your current balance is ₦{reupdate_new_balance}")

    elif user_input == 6:
        withdraw_option = int(input("How much would you like to withdraw?: "))
        new_balance2 = balance - withdraw_option
        update_new_balance2 = float(new_balance2)
        reupdate_new_balance2 = f"{update_new_balance2:,}"
        print(f"You have successfully withdrawed ₦{withdraw_option}.\n\tTherefore, your current balance is ₦{reupdate_new_balance2}")
        break
    elif user_input == 7:
        card_option = int(input("\n\tWealth in a blink.....\n\nThe virtual and physical card can can only be managed through the wealth app for the moment.\nThank you for your time. \n00. Back. \n Kindliy input: "))
        if card_option == 00:
            print(welcome)

    else:
        print("Wrong input!!! Try again...")
