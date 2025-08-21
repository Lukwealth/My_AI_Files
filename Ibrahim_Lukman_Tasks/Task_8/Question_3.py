# Task3: Online Store Cart Calculation
# Creating a list of items and another list of prices
item_list = ["iphone", "Samsung", "Huawei", "Redmi", "Motorolla"]
price_list = [500, 700, 300, 200, 400]

# Starting with an empty cart total
cart_total = 0

# Using assignment operators (+=) to add the price of some items into cart_total
cart_total += price_list[0] 
cart_total += price_list[1] 
cart_total += price_list[4]

cart_total += item_list[0] 
cart_total += item_list[1] 
cart_total += price_list[4]


# printing the list of items and the total price
print(f"Items: {item_list}\nTotal Price: ₦{cart_total}")
