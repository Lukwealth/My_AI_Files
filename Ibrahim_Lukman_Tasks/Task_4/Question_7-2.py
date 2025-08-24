# Task 7: List Manipulation
five_cities =["Abuja", "Lagos", "Osun", "Abeokuta", "Ondo"]
new_one = input("Dear user, kindly input a new city: ")

five_cities[2] = new_one

five_cities.pop()

new_city = ("Ibadan")

five_cities.insert(0, new_city)

print("Upated list:", five_cities)
