import random


def generate_number(difficulty):
    secret_number = random.randrange(1, difficulty)
    return secret_number


def get_guess_from_user(number_range):
    is_valid = False
    while not is_valid:
        user_guess = input(f"Enter your guess: 1 - {number_range}\n")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if 1 <= user_guess <= number_range:
                return user_guess


def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False


def play(difficulty):
    difficulty *= 5
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    result = compare_results(secret_number, user_guess)
    if result:
        print("You Won!!!")
    else:
        print(f"The secret number was {secret_number}\nMaybe next time...")
