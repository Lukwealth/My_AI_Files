#Indexing
word = "Python"
print(word[0])
print(word[-1])

#Slicing
word = "Python"
print(word[0:4])
print(word[2:])
print(word[:3])
print(word[::3])
print(word[1:2:3])

#String Concatenation 
a = "Hello"
b = "World"
print(a + " " + b)

#Repetition
word = "Hi!"
print(word * 5)

#String Searching & Checking
#Membership
text = "Python programming"
print("Pthon" in text)
print("Java" not in text)

#find() / rfind()
text = "Hello World"
print(text.find("o"))
print(text.rfind("o"))

#index() / rindex()
text = "Hello World"
print(text.index("W"))

#startswith() / endswith
filename = "data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))

#upper()
name = "Ada Balogun"
print(name.upper())

#lower
sentence = "python is amazing"
print(sentence.lower())

#title
sentence = "python is amazing"
print(sentence.title())

#strip
text = "   Abuja   "
print(text.strip())

#replace
message = "I love Java"
print(message.replace("Java", "Python"))

#swapcase()
text = "Hello ABEOKUTA"
print(text.swapcase())

#lstrip()
text = "   Nigeria"
print(text.lstrip())

#rstrip
text = "Nigeria   "
print(text.rstrip())

#split()
fruits = "mango orange banana"
print(fruits.split())

#rsplit()
text = "one,two,three,four"
print(text.rsplit(",", 4))

#splitlines()
lines = "Line 1\nLine 2\nLine 3 "
print(lines.splitlines())

#join()
words = ["I", "love", "Python"]
print(" ".join(words))

#center()
text = "Python"
print(text.center(20, "-"))

#rjust()
text = "Python"
print(text.rjust(10, "*"))

#zfill()
num = "42"
print(num.zfill(5))

#isalpha()
print("Lagos.isalpha()")
print("Lagos123".isalpha())

#isdigit()
print("12345".isdigit())
print("123a".isdigit())

#isalnum()
print("Python3".isalnum())
print("Python 3".isalnum())


