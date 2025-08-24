# # Task 4: Name Organizer
# print("Dear User, kindly input 5 different names")
# first_name_request = input("Kindly Input 1st name: ")
# second_name_request = input("Kindly Input 2nd name: ")
# third_name_request = input("Kindly Input 3rd name: ")
# fourth_name_request = input("Kindly Input 4th name: ")
# fifth_name_request = input("Kindly Input 5th name: ")
# all_names = (f'{first_name_request} ') + (f'{second_name_request} ') + (f'{third_name_request} ') + (f'{fourth_name_request} ') + (f'{fifth_name_request}')
# in_lowercase = all_names.lower()
# print(in_lowercase)


names = input("Kindly enter 5 names (separated by spaces): ")
lower = names.lower().split()
lower.sort()
for name in lower:
    print(name)