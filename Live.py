from MemoryGame import play as memory_game
from GuessGame import play as guess_game
from CurrencyRouletteGame import play as currency_roulette_game


def welcome(name):
    # name = input("please enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():
    valid_game = False
    valid_difficulty = False
    play = True
    while play:
        print("""Please choose a game to play:
            1 - Memory Game - a sequence of numbers will appear for 1 second and 
               you have to guess it back
            2 - Guess Game - guess a number and see if you chose like the computer
            3 - Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")
        while not valid_game:
            if not valid_game:
                game = input()
                if game.isdigit() and 1 <= int(game) <= 3:
                    game = int(game)
                    valid_game = True
                else:
                    print("please choose a valid game 1 - 3\n")
        if valid_game:
            print("Please choose the difficulty of the game: \n1 - Easy\n2 - Medium\n3 - Hard\n")
            while not valid_difficulty:
                difficulty = input()
                if difficulty.isdigit() and 1 <= int(difficulty) <= 3:
                    difficulty = int(difficulty)
                    valid_difficulty = True
                else:
                    print("please choose a valid difficulty 1 - 3")
        if valid_game and valid_difficulty:
            if game == 1:
                memory_game(difficulty)
            elif game == 2:
                guess_game(difficulty)
            else:
                currency_roulette_game(difficulty)
            play_again = input("Want to play again? y/n\n")
            if play_again == "y":
                valid_game = False
                valid_difficulty = False
            else:
                play = False
