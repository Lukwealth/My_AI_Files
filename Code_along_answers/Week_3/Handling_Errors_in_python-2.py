# 1. SYNTAX ERROR

# Common Subtype of Syntax Errors
# a. Indentation Error - Incorrect spacing

for i in range(3):
print(i) # Wrong indentation

# This will show error 

# b. Missing Colon/Parenthesis Error

if 5 > 3  # Missing colon
    print("Hello")



# c. Invalid Syntax - General grammar mistakes

print "Hello"



# 2. RUNTIME ERROR

# Common subtypes of Runtime Errors
# a. Zero Division Error - Dividing by zero

x = 10 / 0   # This will throw error

# b. Name Error - Using a variable brfore defining it.

print(age)   # age not defined

# c. Type Error - Wrong data type in an operation

result = "10" + 5   # str + int not allowed

# d. Value Error - Invalid value for a function

number = int("abc")   # cannot convert string to int

# e. Index Error - Accessing list index out of range

fruits = ["apple", "banana"]
print(fruits[3])    # Index out of range

# f. Key Error - Accessing a dictionary with a missing key

data = {"name": "Ada"}
print(data["age"])  # Key not found

# 3. File Not Found Error - File does not exist

f = open("missing.txt") # File not found

# Handling Runtime Errors
# a. try - block of code to test for errors
# b. except - block of code that runs if an error occurs.
# c. finally - block of code that always runs (whether error occurs or not).


try:
    x = 10 / 2
    print("Result:", x)


# This is a specific exception

try:
    number = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")



# This is a case of multiple exception

try:
    number = int("abc") # ValueError
    result = 10 / 0     # ZeroDivisionError

except ValueError:
    print("Invalid conversion to integer.")



# No understanding yet

try:
    f = open("sample.txt", "r")
    content = f.read()

except FileNotFoundError:
    print("File not found,\.")

finally:
    print("Closing file if it was opened.")




# More example on Application of try-except-finally

balance = 5000  # Starting balance

print("Welcone to the ATM")
amount = input("Enter amount to withdraw: ")

try:
    amount = float(amount)  # Convert input to number

    if amount > balance:
        raise ValueError("Insufficient funds.")
    
    balance -= amount
    print("Withdrawal successful. New balance: ₦", balance)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unextected error:", e)

finally:
    print("Transaction session closed.")




# SEMANTIC ERRORS
# cOMMON SUBTYPES OF SEMANTIC ERRORS

# Wrong condition in Logic

age = 18
if age > 18:    # Should be >=
    print("Eligible to vote")
else:
    print("Not eligible")

# output: Not eligible (Wrong result)



# Wrong Formula/Computation

length = 10
width = 5
area = length + width   # should be multiplication
print("Area:", area)

# output: 15 (expected 50)


# Wrong variable usage

marks  = [70, 80, 90]
total = marks[0] * marks[1] * marks[2]  # wrong, should be sum
print("Total:", total)