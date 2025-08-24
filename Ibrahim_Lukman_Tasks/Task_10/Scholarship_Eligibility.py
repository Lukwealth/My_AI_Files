# SCHOLARSHIP ELIGIBILITY

name = input("Kindly enter your name: ")

try:
    citizenship = int(input("Are you a Nigerian citizen?\n1. Yes\n2. No\n(Kindly input 1 or 2): "))
    if citizenship == 1:
        print('Good, you can proceed')
    elif citizenship == 2:
        print("Sorry, you are not eligible for the scholarship..")
        exit()  # stop program since not eligible
    else:
        print("Invalid input... Try again!!!")
        exit()
except ValueError:
    print("Invalid input! Please enter 1 or 2.")
    exit()

try:
    Enrollment = int(input("\nAre you a registered, full-time undergraduate student in a recognized Nigerian university?\n1. Yes\n2. No\n(Kindly input 1 or 2): "))
    if Enrollment == 1:
        print('Good, you can proceed')
    elif Enrollment == 2:
        print("Sorry, you are not eligible for the scholarship..")
        exit()
    else:
        print("Invalid input... Try again!!!")
        exit()
except ValueError:
    print("Invalid input! Please enter 1 or 2.")
    exit()

try:
    Other_Scholarships = int(input("\nAre you currently receiving any other scholarship from the Oil and Gas industry (National or International)?\n1. Yes\n2. No\n(Kindly input 1 or 2): "))
    if Other_Scholarships == 1:
        print('Sorry, you are not eligible for the scholarship..')
        exit()
    elif Other_Scholarships == 2:
        print("Good, you can proceed")
    else:
        print("Invalid input... Try again!!!")
        exit()
except ValueError:
    print("Invalid input! Please enter 1 or 2.")
    exit()

try:
    Academic_Qualifications = int(input("\nDo you have up to five distinctions (A's and B's) in relevant subjects including English and Mathematics in WAEC?\n1. Yes\n2. No\n(Kindly input 1 or 2): "))
    if Academic_Qualifications == 1:
        print(f"\nDear {name}, CONGRATULATIONS!!! You have been offered the opportunity to take this scholarship because you are eligible.")
    elif Academic_Qualifications == 2:
        print("Sorry, you are not eligible for the scholarship..")
    else:
        print("Invalid input... Try again!!!")
except ValueError:
    print("Invalid input! Please enter 1 or 2.")
