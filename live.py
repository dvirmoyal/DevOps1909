def welcome():
    name = input("What is your name? ")
    return (f"Hello {name} and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.")


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    chosen_game = input("Enter the number of the game you want to play (1-3): ")
    difficulty = input("Please choose game difficulty from 1 to 5: ")