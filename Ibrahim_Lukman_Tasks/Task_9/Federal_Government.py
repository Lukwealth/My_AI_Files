# Admission Process

UTME_Grade = set(range(200, 401))
Cut_off_Score = set(range(200, 321))

while True:
    name = input("Kindly input your name: ")

    try:
        School_Choice = int(input("Did you choose UNILAG as your first choice? \n1. Yes \n2. No \nSelect your choice:  "))
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).")
        continue

    if School_Choice == 2:
        print("Sorry, You are not eligible")
        break
    elif School_Choice == 1:
        print("You can proceed")
        break
    else:
        print("Wrong input, try again")

try:
    UTME_Score = int(input("Kindly input your UTME score: "))
    if UTME_Score in UTME_Grade:
        print("Great, You can proceed")
    else:
        print("No, you are not eligible")
except ValueError:
    print("Invalid input! UTME score must be a number.")

try:
    O_level = int(input("Do you have up to 5 credit passes at one sitting O'level subjects, including English Language and Mathematics? \n1. Yes \n2. No\nKindly choose your option: "))
    if O_level == 1:
        print("You can proceed")
    elif O_level == 2:
        print("You are not eligible")
    else:
        print("Wrong Input, Try again")
except ValueError:
    print("Invalid input! Please enter 1 or 2.")

try:
    Cut_off_marks = int(input("After the post UTME, what was your score?: "))
    if Cut_off_marks in Cut_off_Score:
        print("You have been successfully offered admission.. WELCOME ONBOARD.")
    else:
        print("No, you are not eligible")
except ValueError:
    print("Invalid input! Post UTME score must be a number.")
