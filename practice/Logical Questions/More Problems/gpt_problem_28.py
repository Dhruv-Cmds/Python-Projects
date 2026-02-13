# Stores a secret game name.
# Gives the user up to 5 attempts to guess the correct game name.
# Counts how many attempts the user makes.
# If the user guesses correctly:
# Stop the game.
# Return the number of attempts taken.
# If the guess is wrong:
# Print "Try again" and continue.
# Finally, display the total number of attempts used to guess correctly.

def guess_game (secret):
    attempts = 0

    for i in range (5):
        user_guess = input("Enter a game name :")
        attempts += 1
        if (user_guess == secret):
            return attempts
        
        else:
            print("Try again :")

print(guess_game(secret="Minecraft"))

                                #  SECOUN METHOD

def guess_game (secret):

    total_attempts = 0

    for i in range (5):
        user_guess = input("Enter a game name :")
        total_attempts += 1

        if (user_guess.lower().strip() == secret):       
            return total_attempts
        
        else:
            print("TRY AGAIN...")

secret = "Minecraft"
print(guess_game(secret))
