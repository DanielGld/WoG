import random
import time
from os import system, name


def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        sequence.append(random.randrange(1, 101))
    return sequence


def get_list_from_user(num_of_guesses):
    sequence = []
    print("Please enter the sequence after each entry press enter:\n")
    for i in range(num_of_guesses):
        tmp = input()
        if tmp.isdigit():
            sequence.append(int(tmp))
        else:
            i -= 1
            print("invalid entry please try again")
    return sequence


def is_list_equal(game_sequence, user_sequence):
    if game_sequence == user_sequence:
        return True
    else:
        return False


def clear():
    print("\n" * 100)
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux
    else:
        _ = system('clear')


def play(difficulty):
    difficulty *= 3
    sequence = generate_sequence(difficulty)
    print(sequence)
    time.sleep(0.7)
    clear()
    user_sequence = get_list_from_user(difficulty)
    result = is_list_equal(sequence, user_sequence)
    if result:
        print("You Won!!!")
    else:
        print(f"The sequence was {sequence}\nMaybe next time...")
