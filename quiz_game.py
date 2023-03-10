# Welcoming 
print("Welcome to my computer quiz !!")

# Asking whether or not you wanna paly the game 
playing = input("Do you want to play the game? ").lower()
score = 0

if playing != "yes":
    quit()

print("ok! let's play")

# Taking the input in the form of answer of the question being asked
answer = input("Q1. What does CPU stand for? ").lower()

if answer == "central processing unit":
    score += 1
    print("Correct!")

else:
    print("Incorrect")


# Taking the input in the form of answer of the question being asked
answer = input("Q2. What does ROM stand for? ").lower()


if answer == "read only memory":
    score+= 1
    print("Correct!")

else:
    print("Incorrect")


# Taking the input in the form of answer of the question being asked
answer = input("Q3. What does PSU stand for? ").lower()


if answer == "power supply unit":
    score+= 1
    print("Correct!")

else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/3) * 100) + "%.")


