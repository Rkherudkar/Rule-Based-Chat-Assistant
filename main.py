#Rule Based AI Python ChatBot

import datetime
import time

name= input ("Swagat hai! Enter Your Name:")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <=11:
    print("Good Moring,",name)
elif 11 <= presentHour <=17:
    print("Good Afternoon",name)
elif 17 <= presentHour <=20:
    print("Good Evening",name)
else:
    print("Good night",name)

print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic Question ,Type 'bye' to exit the bot")

# ChatBot Memory Creation [dictionary of responses ]

responses={
    "hi":"Hello! How can I help you?",
    "how are you":"I am fine . Thank You",
    "who are you":"I am Smart AI ChatBot",
    "motivate me":"Believe in yourself and all that you are. Know that the moment you belive in yourself,you obstacle can be overcome",
    "how to learn python":"You can learn python from online resources like w3schools, GeeksforGeeks, and YouTube tutorials",
    "okk":"Ask me another question"
}

# Method/Fuction to get response of ChatBot

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return"Sorry, I am not able to tell that yet. I am still in learning mode,I am learn that soon.."


# Take user input

while True:
    UserInput=input("Please ask Your Question:")
    reply= getResponseOfBot(UserInput)
    print("Bot Response:",reply)

    if "bye" in UserInput.lower():
        print("Thank You for using ChatBot. Have a nice day!")
        break