import random
hidden_number=random.randint(1,100)
score=100

for i in range (5):
    guess=int(input("Guess a number between 1 to 100:"))
    if guess==hidden_number:
        print("You Won!")
        print("score:",score)
        break
    elif guess>hidden_number:
        print("Hint:Your guess is High")
        score-=20
    else:
        print("Your guess is Low")
        score-=20
else:
    print("All Chances are gone!")
    print("you Lost!")
    print("Hidden number:",hidden_number)
