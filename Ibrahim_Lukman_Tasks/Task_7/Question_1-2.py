# Task1: Student Bio Data Storage
student_bio_data = {}

student_name = input("Dear user, kindly input your name: ")
student_age = int(input("Dear user, kindly input your age: "))
student_gender = input("Dear user, kindly input your gender: ")
student_courses = input("Dear user, kindly input your courses(separated with comma): ")

student_courses = student_courses.split(',')

print("\nStudent Bio Data")
print(f"Name:\t\t{student_name}")
print(f"Age:\t\t{student_age}")
print(f"Gender:\t\t{student_gender}")
print(f"Courses:\t{student_courses}")