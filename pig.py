## Saar Turjeman
## IS211 - SPRING 2023
## Assignment #7

import random

class Player():

    def __init__(self, name):
        self._name = name
        self._total_score = 0

    def add_episode_score_to_total_score(self, episode_score):
        self._total_score += episode_score

    def get_total_score(self):
        return self._total_score

    def get_name(self):
        return self._name


class Die():

    def __init__(self):
        super().__init__()

    def roll(self):
        return random.randint(1, 6)


class Game():

    def __init__(self, numPlayers, die):
        self._die = die
        self._players = [Player(i + 1) for i in range(numPlayers)]

    def _play_episode(self, player):
        episode_score = 0
        print(f"Hi Player {player.get_name()}, your turn. Your total score is {player.get_total_score()}.")
        while True:
            print(f"your current score is {episode_score}.")
            decision = input("Choose either to roll(r) or to hold(h): ")
            if decision == "r":
                roll_value = self._die.roll()
                print(f"{roll_value} was rolled")
                if roll_value == 1:
                    return 0
                episode_score += roll_value
                cumulative_score = player.get_total_score() + episode_score
                if cumulative_score >= 100:
                    return cumulative_score

            elif decision == "h":
                player.add_episode_score_to_total_score(episode_score)
                return 0

    def play_game(self):
        winner = 0
        player_idx = 0
        print(f"Starting a new game with {len(self._players)} players")
        while winner == 0:
            p = self._players[player_idx]
            value = self._play_episode(p)
            if value >= 100:
                winner = p.get_name()

            player_idx = (player_idx + 1) % len(self._players)

        print(f"The winner is player {winner}")


if __name__ == "__main__":
    numPlayers = int(input("Enter number of players (default: 2): ") or "2")
    random.seed(0)
    die = Die()
    game = Game(numPlayers, die)
    game.play_game()
