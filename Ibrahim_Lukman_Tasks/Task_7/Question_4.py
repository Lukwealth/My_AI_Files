# Task 4: Unique Membership Registration
print("Kindly enter three names.")
names = input("Enter 3 names '(separated by comma)': ")

# Convert them to a set to ensure uniqueness
name = ()
names_set =set(n.strip() for n in names.split(","))
print(names_set)

# Creating a dictionary
print("\nThe names and their lengths are:")
print({name: len(name) for name in names_set})