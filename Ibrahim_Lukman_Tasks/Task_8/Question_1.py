num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# num1 = 20, num2 = 30
print(f"{num1} == {num2} : {num1 == num2}")
# Output : 20 == 30 : False
# Explanation: 
# num1(20) is not equal to num2(30), therefore it is False


print(f"{num1} != {num2} : {num1 != num2}")
# Output : 20 != 30 : True
# Explanation: 
# num1(20) is not equal to num2(30), therefore it is True

print(f"{num1} > {num2} : {num1 > num2}")
# Output : 20 > 30 : False
# Explanation: 
# num1(20) is greater than num2(30), therefore it is False

print(f"{num1} < {num2} : {num1 < num2}")
# Output : 20 < 30 : True
# Explanation: 
# num1(20) is less than num2(30), therefore it is True


# 3 Usecases where the program can be applied 
# 1. Checking Eligibility
# 2. Confirming Student scores
# 3. For grading (Checking if students passed or failed)


# Code for Grading (Checking if students passed or failed)

score = int(input("Kindly enter your score: "))
pass_mark = 70
print(f"{score} >= {pass_mark} : {score >= pass_mark}")



# Code for (Confirming Students score)
student_1 = 50
student_2 = 70
student_3 = 80
student_4 = 60
student_5 = 20

Cut_Off_mark = 70

# To know if students meet the cut off mark or not
print("\n========== CUT OFF MARKS ==========")
print(f"\nStudent1 meet the cut off mark : {student_1 >= Cut_Off_mark}")
print(f"\nStudent2 meet the cut off mark : {student_2 >= Cut_Off_mark}")
print(f"\nStudent3 meet the cut off mark : {student_3 >= Cut_Off_mark}")
print(f"\nStudent4 meet the cut off mark : {student_4 >= Cut_Off_mark}")
print(f"\nStudent5 meet the cut off mark : {student_5 >= Cut_Off_mark}")

