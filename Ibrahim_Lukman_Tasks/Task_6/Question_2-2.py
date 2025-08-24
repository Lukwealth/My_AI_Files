# Task_2 (Unique Name Collector)

print("Welcome to Lukwealth World") 
attendees = set()
attendees.add(input("Enter your name: "))
attendees.add(input("Enter your name: "))
attendees.add(input("Enter your name: "))
attendees.add(input("Enter your name: ")) 
attendees.add(input("Enter your name: ")) 

print("\nattendees:", attendees)

names = sorted(attendees) 
print(f"List of Lukwealth World Attendees.\n{names}")