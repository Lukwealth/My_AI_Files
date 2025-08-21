# Task 4 (Tuple Unpacking)
First_name = input("Dear user, Kindly input your first name: ")
Age = input("Dear user, Kindly input your age: ")
Favorite_color = input("Dear user, Kindly input your favorite color: ")
Home_town = input("Dear user, Kindly input your home town: ")
Tuple_profile = (First_name, Age, Favorite_color, Home_town)
First_name, Age, Favorite_color, Home_town = Tuple_profile
print(f"First_Name: {First_name}\nAge: {Age}\nFavorite Color: {Favorite_color}\nHome town: {Home_town}")