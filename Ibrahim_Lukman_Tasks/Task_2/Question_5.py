#Assignment 5
Market_name = input("Dear customer, what is the name of your market?: ")
Number_of_traders = input("How many traders are in this market?: ")
Daily_revenue = float(input("How much revenue do you make in this market daily in naira?: "))
Revenue_formatted = f"{Daily_revenue:,}"
print(f"{Market_name} is a market that contains {Number_of_traders} traders and this market generates #{Revenue_formatted} daily")