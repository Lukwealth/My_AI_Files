# Admission Process

UTME_Grade = set(range(200, 401))
Cut_off_Score = set(range(200, 321))

while True:
    name = input("Kindly input your name: ")


    School_Choice = int(input("Did you chose UNILAG as your first choice? \n1. Yes \n2. No \n Select your choice:  "))

    if School_Choice == 2:
        print("Sorry, You are not eligible")
        
    else:
        print("Wrong input, try again")
        break
    
if School_Choice == 1:
    print("You can proceed")

UTME_Score = int(input("Kindly input your UTME score: "))

if UTME_Score in UTME_Grade:
    print("Great, You can proceed")

else:
    print("No, you are not eligible")

O_level = int(input("Do you have up to 5 credit passes at one sitting O'level subjects, including English Language and Mathematics? \n1. Yes \n2. No\nKindly choose your option: "))

if O_level == 1:
    print("You can proceed")

if O_level == 2:
    print("You are not eligible")

else:
    print("Wrong Input, Try again")


Cut_off_marks = int(input("After the post UTME, what was your score?: "))

if Cut_off_marks in Cut_off_Score:
    print("You have been successfully offered admission.. WELCOME ONBOARD.")

else:
    print("No, you are not eligible")



