balance = 100000

while True:
    try:
        welcome = input("Dear Customer, Welcome to Wealth Bank...\nKindly dial *349# to proceed: ")
        print("\nWealth, in just a blink....\n\n1. Transfer\n2. Airtime & Data\n3. Betting & Utilities\n4. Check Balance\n5. Add money\n6. Withdraw\n7. Card\n0. Exit")

        user_input = int(input(f"\nKindly choose from the above options to proceed: "))

        # ========== TRANSFER ==========
        if user_input == 1:
            print("\nYou just chose option 1 (Transfer)...\n1. Transfer to Wealth Account\n2. Transfer to other Bank Account\n00. Back")
            Transfer_input = int(input("Kindly choose from the above options to proceed: "))

            if Transfer_input == 1 or Transfer_input == 2:
                acct = input("Kindly input the account number: ")
                amount = int(input("Kindly input how much you would like to transfer: "))

                if amount > balance:
                    print("Insufficient Balance!")
                else:
                    pin = input("Kindly enter your 4-digit PIN: ")
                    balance -= amount
                    print(f"✅ Transfer of ₦{amount:,} to account {acct} was successful.\nNew Balance: ₦{balance:,}")

            elif Transfer_input == 0:
                continue
            else:
                print("Invalid transfer option.")

        # ========== AIRTIME & DATA ==========
        elif user_input == 2:
            choice = int(input("Select an option. \n1. Airtime\n2. Data\n00. Back to main menu\nNow input option: "))
            if choice in [1, 2]:
                number = input("Enter Phone Number: ")
                amount = int(input("Enter amount: "))

                if amount > balance:
                    print("Insufficient Balance!")
                else:
                    pin = input(f"You are sending ₦{amount:,} to {number}.\nEnter PIN to proceed or 0 to Cancel: ")
                    if pin == "0":
                        print("Transaction Cancelled")
                    else:
                        balance -= amount
                        print(f"{('Airtime' if choice==1 else 'Data')} purchase of ₦{amount:,} for {number} successful.\nNew Balance: ₦{balance:,}")

            elif choice == 0:
                continue

        # ========== BETTING & UTILITIES ==========
        elif user_input == 3:
            option = int(input("Select option\n1. Betting\n2. Electricity\n3. Solar\n00. Back to main menu.\nYour choice: "))
            if option in [1, 2, 3]:
                print("Payment Successful")
            elif option == 0:
                continue
            else:
                print("Invalid option")

        # ========== CHECK BALANCE ==========
        elif user_input == 4:
            pin = input("Kindly input your 4-digit pin to proceed: ")
            print(f"Your current balance is ₦{balance:,}")

        # ========== ADD MONEY ==========
        elif user_input == 5:
            amount = int(input("How much would you like to add? : "))
            balance += amount
            print(f" You have successfully added ₦{amount:,}.\nNew Balance: ₦{balance:,}")

        # ========== WITHDRAW ==========
        elif user_input == 6:
            amount = int(input("How much would you like to withdraw?: "))
            if amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print(f"Withdrawal of ₦{amount:,} successful.\nNew Balance: ₦{balance:,}")

        # ========== CARD ==========
        elif user_input == 7:
            card_option = input("\nWealth in a blink.....\n\nThe virtual and physical card can only be managed through the wealth app.\n00. Back\nKindly input: ")
            if card_option == "00":
                continue

        # ========== EXIT ==========
        elif user_input == 0:
            print("Thank you for banking with Wealth Bank.")
            break

        else:
            print("Wrong input!!! Try again...")

    except ValueError:
        print("Invalid input! Please enter a number.")
