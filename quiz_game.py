# Welcoming 
print("Welcome to my computer quiz !!")

# Asking whether or not you wanna paly the game 
playing = input("Do you want to play the game? ")

if playing != "y":
    quit()

print("ok! let's play")

# Taking the input in the form of answer of the question being asked
answer = input("Q1. What does CPU stand for? ")
answer = answer.lower()

if answer == "central processing unit":
    print("Correct!")

else:
    print("Incorrect")


# Taking the input in the form of answer of the question being asked
answer = input("Q2. What does ROM stand for? ")
answer = answer.lower()

if answer == "read only memory":
    print("Correct!")

else:
    print("Incorrect")


# Taking the input in the form of answer of the question being asked
answer = input("Q3. What does PSU stand for? ")
answer = answer.lower()

if answer == "power supply unit":
    print("Correct!")

else:
    print("Incorrect")

