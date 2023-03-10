print("Welcome to my computer quiz !!")


playing = input("Do you want to play the game? ")

if playing != "yes":
    quit()

print("ok! let's play")

answer = input("Q1. What does CPU stand for? ")
answer = answer.lower()

if answer == "central processing unit":
    print("Correct!")

else:
    print("Incorrect")



answer = input("Q2. What does ROM stand for? ")
answer = answer.lower()

if answer == "read only memory":
    print("Correct!")

else:
    print("Incorrect")



answer = input("Q3. What does PSU stand for? ")
answer = answer.lower()

if answer == "power supply unit":
    print("Correct!")

else:
    print("Incorrect")

