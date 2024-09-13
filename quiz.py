print("Welcome to my game")

playing = input("do you want to play my game? ")

if playing != "yes":
    quit()
print("okay! Lets play")
score = 0
answer =input("what is captial of india? ")
if answer.lower() =="delhi":
    print("correct!")
    score += 1
else:
    print("incorrect!")
answer = input("what is first letter in alphabet? ")
if answer.lower() =="A":
    print("correct!")
    score += 1
else:
    print("incorrect!")
answer = input("what is captial of china? ")
if answer.lower() =="beijing":
    print("correct!")
    score += 1
else:
    print("incorrect!")
answer = input("what is captial of japan? ")
if answer.lower() =="tokyo":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you got "+ str(score) +" questions corect")


