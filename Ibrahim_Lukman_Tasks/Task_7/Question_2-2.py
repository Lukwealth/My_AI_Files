# Task 2: Super Market Price List
items = {} 
prices = {}

print("The following are the available items available for purchase.")
item_1 = ("Rice")
item_2 = ("Beans")
item_3 = ("Pepper")

items = (item_1, item_2, item_3)
print(items)


print("\nPlease enter the prices of the above listed items.")
price_1 = float(input("Kindly enter the price for Rice: "))
price_2 = float(input("Kindly enter the price for Beans: "))
price_3 = float(input("Kindly enter the price for Pepper: "))


price_list = {price_1, price_2, price_3}
print(prices)


print(f"\nAvailable items available for purchase and their prices:\n{item_1}:\t\t₦{price_1: ,.2f}k\n{item_2}:\t\t₦{price_2: ,.2f}k\n{item_3}:\t\t₦{price_3: ,.2f}k")

# To update the price of an item
price_update = float(input("Please enter a new price for Rice: "))
price_list.update({price_update,})
price_3 = price_update 
print(f"The updated price for Rice is now: #{price_update: ,.2f}k")
print("\nThe updated prices for all available items are:")
print(f"{item_1}: \t\t₦{price_1: ,.2f}k\n{item_2}: \t\t₦{price_2: ,.2f}k\n{item_3}: \t₦{price_update: ,.2f}k")