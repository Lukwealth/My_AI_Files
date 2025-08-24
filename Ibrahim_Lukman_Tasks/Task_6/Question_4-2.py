print("\nHere are the slected voters required to input their names...")
First_voter = input("Kindly input your name: ")
Second_voter = input("Kindly input your name: ")
Third_voter = input("Kindly input your name: ")

voters = {First_voter, Second_voter, Third_voter}
for vote in [First_voter, Second_voter, Third_voter]:
    if vote in voters: 
        print(f"warning: {vote} has previously registered.") 

print("\nTotal number of unique voters: ", len(voters)) 
print("Voters list:", ", ".join(voters))