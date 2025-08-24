# Unique Voters Registration System


print("======= Unique Voters Registration System =======")

voter_names = set()  # empty set for unique names
total_voters = 5     # number of people we want to register

for i in range(total_voters):
    name = input(f"Voter {i+1}, kindly input your name: ")

    if name in voter_names:
        print(f"Sorry, {name} has already registered before!")
    else:
        voter_names.add(name)
        print(f"{name} successfully registered.")

print("\n======= REGISTRATION CLOSED =======")
print("Total number of unique voters:", len(voter_names))
print("Voters list:", ", ".join(voter_names))
