#Question_11
Fruits = "apple,banana,orange"
print(Fruits.split(","))

#Question_12
User_Sentence = input("Dear user, Kindly tell us how you spent your weekend: ")
new_words = "\n".join(User_Sentence.split())
print("words in the sentence:\n",new_words)

#Question_13
Home_Address = "Road 5 House 19, Oluwo, Panseke, Abeokuta, Ogun State"
print(Home_Address.replace(" ","_"))

#Question_14
fruit = "Banana"
print(fruit.count("a"))

#Question_15
Slack_link = "https://app.slack.com/client/"
print(Slack_link.startswith("https://"))