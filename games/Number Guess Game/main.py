# Author: Dhruv
import random

def game():

    print("You are playing a game...")

    score = random.randint (1 , 91)

    with open ("Hi_score.txt") as f:     
      Hi_score = f.read()

      if (Hi_score != ""):        
        Hi_score = int(Hi_score)

      else:
        Hi_score = 0 

    print(f"Your score is : {score}")

    if (score > Hi_score):

        with open("Hi_score.txt" , "w") as f:
            f.write(str(score))

    elif (Hi_score == 91):
        print("game is end, play again... :") 

        with open("Hi_score.txt" , "w") as f:
            f.write(str(0))

    return score

game()