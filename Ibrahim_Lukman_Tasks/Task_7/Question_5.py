# Task 5: Contact Quick Lookup

names = ()
phone_numbers = ()

print("Here are available contacts")
names = ("Lukman", "Olamide", "Bayo")
print(f"The names are: {names}")

phone_numbers = ("08114833385", "07085125588", "08100054890")
print(f"The phone numbers are: {phone_numbers} ")


# Using zip() and dict() to combine tuples
print("Names of customers and their phone numbers:")
contact = dict(zip(names, phone_numbers))
print(contact)

# Using .get() for safe retrieval
print(contact.get(input("\nEnter a name: "), "an error message"))
