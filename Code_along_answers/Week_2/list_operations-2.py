# LIST OPERATIONS IN PYTHON
# 1. Concatenation (+)
list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(result)

# 2. Repetition (*)
nums = [1, 2]
repeated = nums * 3
print(repeated)

# 3. Indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

# 4. Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])

# 5. Membership (in/not in)
colors = ["red", "green", "blue"]
print("green" in colors)
print("yellow" not in colors)

# 6. Length (len())
items = ["pen", "book", "laptop"]
print(len(items))

# 7. Min and Max (min()/max())
nums = [5, 2, 9, 1]
print(min(nums))
print(max(nums))

# 8. Sum (sum())
numbers = [1, 2, 3, 4]
print(sum(numbers))

# 9. List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# 10. Copying a List
a = [1, 2, 3]
b = a.copy()
print(b)
b = list(a)
print(b)