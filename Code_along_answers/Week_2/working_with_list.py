# CREATING AN EMPTY LIST
# Method 1: Using square brackets
empty_list = []
print(empty_list)

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2)


# CREATING A LIST WITH INITIAL ELEMENTS
# List of integers
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)


# CREATING A LIST FROM ANOTHER SEQUENCE
# From a string (each character becomes an element)
chars = list("hello")
print(chars)


# CREATING A LIST USING LIST COMPREHENSION
# Squares of numbers 0-4
squares = [a**2 for a in range(5)]
print(squares)

# From a tuple
my_tuple = (10,20,30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# From a range
numbers_range = list(range(5))
print(numbers_range)

# Even numbers between 0-10
evens = [b for b in range(11) if b % 2 == 0]
print(evens)

# CREATING A NESTED LIST
# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)

# Accessing elements in a nested list
print(matrix[1])
print(matrix[0][1])


# Ordered Collection
fruits = ["mango", "orange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])

# Allows Duplicates
items = ["rice", "beans", "yam", "rice"]
print(items)

# Mutable(Can be Changed)
numbers = [1, 2, 3]
numbers[1] = 20
print(numbers)

# Can contain Different Data Types
mixed = [10, "Nigeria", 3.14, True]
print(mixed)

# Can Be Nested
nested_list = [[1, 2], ["a", "b"]]
print(nested_list)
print(nested_list[0][1])
print(nested_list[1][1])

# Dynamic Size
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
names.append('Lukman')
print(names)