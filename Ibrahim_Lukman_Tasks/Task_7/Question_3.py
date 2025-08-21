# Task 3: Days and Activities Pairing
print("Days of the Week") 
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "saturday")
print(days_of_the_week)

print("Dear user Kindly fix one activity each for the following listed days of the week.")
activity_1 = input("Enter an activity for Monday: ")
activity_2 = input("Enter an activity for Tuesday: ")
activity_3 = input("Enter an activity for Wednesday: ")
activities = (activity_1, activity_2, activity_3)

print("\nThe activities for the week are:")
activities_for_the_week = {
    "Sunday": "none",
    "Monday": activity_1,
    "Tuesday": activity_2,
    "Wednesday": activity_2,
    "Thursday": "none",
    "Friday": "none",
    "Saturday": "none"
}
for key, value in activities_for_the_week.items():
    print(f"{key}: {value}")

# Printing the dictionary
print("\nActivities for the Week.")
days_activities = dict(zip(days_of_the_week, activities))
print(days_activities)