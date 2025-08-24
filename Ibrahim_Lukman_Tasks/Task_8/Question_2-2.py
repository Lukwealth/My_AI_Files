# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# CODE EXPLANATION
'''The code wants to check the eligibility of candidates, such a way that they have to be less than 18 years and must also score more than 70 in their test
It asks users to input their name, age and the test score and then print out their eligibility status '''

# ADAPTING THE CODE TO CASE
name = input("Kindly enter your name: ")
citizenship = int(input("Are you a Nigerian citizen?\n1. Yes\n2. No\n(Kindly input 1 or 2): "))
Enrollment = int(input("Are you a registered, full-time undergraduate student in a recognized Nigerian university?\n1. Yes\n2. No\n(Kindly input 1 or 2): "))
Other_Scholarships = int(input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whther National or International?\n1. Yes\n2. No\n(Kindly input 1 or 2): "))
Academic_Qualifications = int(input("Do you have up to five distinctions (A's and B's) in relevant subjects including English Language and Mathematics in your WAEC?\n1. Yes\n2. No\n(Kindly input 1 or 2): "))

eligibilty = (citizenship == 1) and (Enrollment == 1) and (Other_Scholarships == 2) and (Academic_Qualifications == 1)
print(f"Dear {name}\nEligiblity for the Federal Government Schorlarship: {eligibilty} ")