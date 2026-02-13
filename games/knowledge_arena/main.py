from player import Player, load_players, save_players


def main():

    players = load_players()

    name = input("Enter your name: ").strip()

    if name in players:
        player = players[name]   # retrieve existing player
        print(f"\nWelcome back! {name}")
    else:
        player = Player(name)
        players[name] = player
        print(f"\nNew profile created for {name}")

    while True:
        print("\n======================")
        print("1. Show Stats")
        print("2. Add Test Result")
        print("3. Exit")
        print("======================")

        choice = input("Choose an option: ").strip()

        if choice == "1":

            print("\n----- YOUR STATS -----")
            print(f"Score: {player.score}")
            print(f"Correct: {player.correct}")
            print(f"Attempts: {player.attempts}")
            print(f"Accuracy: {player.accuracy()}%")

        elif choice == "2":

            result = input("Was the answer correct? (y/n): ").strip().lower()

            if result == "y":
                player.update(True)
                print("Marked as correct. +10 points.")
            elif result == "n":
                player.update(False)
                print("Marked as incorrect.")
            else:
                print("Invalid input. Use 'y' or 'n'.")

        elif choice == "3":
            save_players(players)
            print("\nProgress saved. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
