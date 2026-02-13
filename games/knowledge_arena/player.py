import os

FILE = "players.txt"


class Player:

    def __init__(self, name, score=0, correct=0, attempts=0):
        self.name = name
        self.score = int(score)
        self.correct = int(correct)
        self.attempts = int(attempts)

    def update(self, is_correct):
        self.attempts += 1

        if is_correct:
            self.correct += 1
            self.score += 10

    def accuracy(self):
        if self.attempts == 0:
            return 0
        return round((self.correct / self.attempts) * 100, 2)


def load_players():
    players = {}

    # If file doesn't exist, return empty dictionary
    if not os.path.exists(FILE):
        return players

    with open(FILE, "r") as f:
        for line in f:
            line = line.strip()

            if line:
                name, score, correct, attempts = line.split(",")

                # Create Player object correctly
                players[name] = Player(name, score, correct, attempts)

    return players


def save_players(players):
    with open(FILE, "w") as f:
        for player in players.values():
            line = f"{player.name},{player.score},{player.correct},{player.attempts}\n"
            f.write(line)
