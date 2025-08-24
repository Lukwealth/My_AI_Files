#Assignment 6
Customer_full_name = input("Dear customer, what is your full name?: ")
Units_consumed = int(input("How many units do you consume?: "))
Cost_per_unit = float(input("What is the cost per unit? "))
total_bill = Units_consumed * Cost_per_unit
print(f"Dear {Customer_full_name}, here is your Electricity bill\n\n\tUnits Consumed(kWh) = {Units_consumed}\n\tCost per units = {Cost_per_unit}\n\tTotal bill = {total_bill}\n\nThank you for your Patronage....")