#Task 4: Student Record
# Creating an empty dictionary
student = {}

# Asking user to input their name and age
student["name"] = input("Kindly input your name: ")
student["age"] = int(input("Kindly input your age: "))

# Adding a list of scores
student["list_of_scores"] = [60, 70, 80]

# Using comparison operator to check if the student has passed
average_score = sum(student["list_of_scores"]) / len(student["list_of_scores"])
student["passed"] = average_score >= 50

# Using a logical operator to check if the student is a teenager
student["teenager"] = student["age"] >= 13 and student["age"] <= 19

# Printing out the complete record
print(f"Student Record:\nName: {student['name']}\nAge: {student['age']}\nScores: {student['list_of_scores']}\nPassed: {student['passed']}\nTeenager: {student['teenager']}")
