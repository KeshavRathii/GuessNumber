import random

target = random.randint(1,100)
print("Let's play a game : Guess the number between 1 to 100 ")

while True:
    userChoice = input("Guess the target or Quit : ")
    if userChoice.casefold() == "quit":
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess.... ")
    elif(userChoice > target):
        print("Your number was too big. Take a smaller guess.... ")


print("------GAME OVER------")
