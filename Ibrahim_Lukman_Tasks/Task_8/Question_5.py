# Task 5: Store Inventory Update
# Creating a dictionary that includes items with their available quantities
store = {
    "Airpod": 10,
    "Charger": 30,
    "Power bank":40
}

# Printing the items availaible in stock so the user can choose
print("Items available for purchase. (Airpod, Charger, Power Bank)")

# Asking the user to input the item and item quantity
user_item = input("Dear user, Kindly input the item you want to buy: ")
item_quantity = int(input(f"How many {user_item} do you want to purchase :"))

# printing the dictionary before purchase
print(f"Before purchase: {store}")

# Using assignment operator -= to the item quantity in the dictionary
store[user_item] -= item_quantity

# Printing the dictionary after purchase
print(f"After purchase: {store} ")