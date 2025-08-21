#Assignment 8
Distance = float(input("Dear User, how long is it from here to the destination in kilometres?: "))
Fare_per_km = float(input("How much is the fare per kilometer: "))
Total_fare = Fare_per_km * Distance
Decimal_fare = f"{Total_fare:.2f}"
print(f"Your distance = {Distance}\nNote: Fare per kilometre = {Fare_per_km}\nTherefore, your total fare = {Decimal_fare} ")