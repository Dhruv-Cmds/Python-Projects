# Author: Dhruv
import random
import json

def game():

    print("You are playing a game...")

    score = random.randint (1 , 91)

    try:
        with open("games/Number Guess Game/score.json", "r") as f:
            Hi_score = json.load(f)

            if not isinstance(Hi_score, int):
                Hi_score = 0

    except (FileNotFoundError, json.JSONDecodeError):
        Hi_score = 0


    print(f"Your score is : {score}")

    if (score > Hi_score):

        with open("games/Number Guess Game/score.json" , "w") as f:
            # f.write(str(score))
            json.dump(score , f , indent=4)

    elif (Hi_score == 91):
        print("game is end, play again... :") 

        with open("games/Number Guess Game/score.json" , "w") as f:
            json.dump(0 , f , indent=4)

    return score

game()