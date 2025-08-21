#Question_6
Given_string = "Let's move on with python"
print("python" in Given_string)
print("python" not in Given_string)

#Question_7
name = "Growth"
print("".join(reversed(name)))

#Question_8
Food = "     Amala     "
print(Food.strip())

#Question_9
school_name = input("Dear User, What is the name of your School?:  ")
vowel_a = school_name.lower().count("a")
vowel_e = school_name.lower().count("e")
vowel_i = school_name.lower().count("i")
vowel_o = school_name.lower().count("o")
vowel_u = school_name.lower().count("u")
number_of_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
print(number_of_vowels)

#Question_10
String = "1234"
string_to_int = int(String)
Multiplication = string_to_int * 2
print(Multiplication)