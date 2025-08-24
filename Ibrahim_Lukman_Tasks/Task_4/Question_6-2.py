# Task 6: Word Analyzer
word = input("Dear user, kindly input a word: ")
print(len(word))

upper_case = word.isupper()
print(upper_case)
lower_case = word.islower()
print(lower_case)
title = word.istitle()
print(title)

reversed_word = (word[::-1])
print(reversed_word)