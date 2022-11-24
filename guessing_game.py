import random


def guessing_game():
    num = random.randint(1, 101)
    while True:
        guess = int(input('Guess between 1 and 100: '))
        if guess == num:
            print('Congrats')
            break
        if guess > num:
            print('Too high :(')
        elif guess < num:
            print('Too low :(')


guessing_game()
"""Number guessing game"""

