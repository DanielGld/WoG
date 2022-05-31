import random

from currency_converter import CurrencyConverter


def get_money_interval(difficulty, ils):
    return round(max(ils - (5 - difficulty), 0), 2), round(ils + (5 - difficulty), 2)


def get_guess_from_user(usd):
    is_valid = False
    while not is_valid:
        user_guess = input(f"Enter your guess: {usd}$ in ils is:\n")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            return user_guess


def play(difficulty):
    difficulty *= 1.2
    c = CurrencyConverter()
    usd = random.randrange(100)
    ils = round(c.convert(usd, "USD", "ILS"), 2)
    low, high = get_money_interval(difficulty, ils)
    user_guess = get_guess_from_user(usd)
    if low <= user_guess <= high:
        print(f"You Won!!! {usd}$ is {ils} in ils")
    else:
        print(f"You lose... maybe next time {usd}$ is {ils} in ils")
