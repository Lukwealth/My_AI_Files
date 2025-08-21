# Task 2: Shopping List Manager
empty_list = []
shopping_item1 = input("Dear Esteemed Client, kindly input your 1st shopping item: ")
shopping_item2 = input("Dear Esteemed Client, kindly input your 2nd shopping item: ")
shopping_item3 = input("Dear Esteemed Client, kindly input your 3rd shopping item: ")
empty_list.append(shopping_item1)
empty_list.append(shopping_item2)
empty_list.append(shopping_item3)
adding_comma = ("," .join(empty_list))
print(str(empty_list))