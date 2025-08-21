#Assignment 12
Greeting = print("Dear Customer, Welcome to Wealth Bank.")
Dial = input("Kindly dial *123# to proceed: ")
print(f"You can now proceed:\n1. Check Balance \n2. Buy Airtime \n3. Buy Data")
User_input = input(f"Kindly choose option 1, 2, or 3 to proceed: ")
if User_input == "1":
    print(f'You just selected option 1 (Check Balance)')
    print(f"\nYour balance is $5,000")
elif User_input == "2":
    print(f"You just selected option 2 (Buy Airtime)")
    Airtime = int(input("How much Airtime would you like to purchase?: "))
    print(f"You have successfully purchased ₦{Airtime}\nThank you.....")
elif User_input == "3":
    print(f"You just selected option 3 (Buy Data)")
    Data = int(input("How much Data would you like to purchase?: "))
    print(f"You have successfully purchased {Data}GB\nThank you.....")
print("\nThank you for banking with us...")