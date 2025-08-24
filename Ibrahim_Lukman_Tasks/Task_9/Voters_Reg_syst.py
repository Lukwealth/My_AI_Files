# Create a Unique Voters Registration System
print("======= List of people selected to vote =======")
name1 = input("Kindly input your name: ")
name2 = input("Kindly input your name: ")
name3 = input("Kindly input your name: ")
name4 = input("Kindly input your name: ")
name5 = input("Kindly input your name: ")

voter_names = {name1, name2, name3, name4, name5}

for x in [name1, name2, name3, name4, name5]:
    if x in voter_names: 
        print(f"Sorry, {x} has registered before!!!")

print("\nTotal number of unique voters: ", len(voter_names)) 
print("Voters list:", ", ".join(voter_names))

