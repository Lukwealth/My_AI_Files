# Task 5: Student Score Tracker

names_list = []
scores_list = []

print("Dear user kindly input 3 student names...")
name_1 = input("Student name 1: ")
name_2 = input("Student name 2: ")
name_3 = input("Student name 3: ")

print("Now kindly input the score of each student")
score_1 = input(f"{name_1} score: ")
score_2 = input(f"{name_2} score: ")
score_3 = input(f"{name_3} score: ")

names_list.append(name_1)
names_list.append(name_2)
names_list.append(name_3)

scores_list.append(score_1)
scores_list.append(score_2)
scores_list.append(score_3)

print(f"\tSTUDENT SCORES \n\nNAMES\t\tSCORES\n{name_1}\t\t{score_1}\n{name_2}\t\t{score_2}\n{name_3}\t\t{score_3} ")