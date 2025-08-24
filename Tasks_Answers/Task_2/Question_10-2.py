#Assignment 10
School_name = input("What is the name of your school?: ")
Tuition_fee = float(input("How much is your tuition fee?: "))
D_Tuition_fee = f"{Tuition_fee:.2f}"
Hostel_fee = float(input("How much is your hostel fee?: "))
D_Hostel_fee = f"{Hostel_fee:.2f}"
Feeding_fee = float(input("How much is your feeding fee?: "))
D_Feeding_fee = f"{Feeding_fee:.2f}"
Total_fee = Tuition_fee + Hostel_fee + Feeding_fee
D_Total_fee = f"{Total_fee:.2f}"
print(f"Welcome to {School_name}\nHere is your school fees breakdown\n\n\tTuition fee = {D_Tuition_fee}\n\tHostel fee = {D_Hostel_fee}\n\tFeeding fee = {D_Feeding_fee}\n\n\tTOTAL = {D_Total_fee}")