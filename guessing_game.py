import random


def user_guess():
    while True:
        try:
            num = int(input('Guess between 1 and 100: '))
        except ValueError:
            print('Number ouf of range')
            continue
        if int(num) not in range(1, 101):
            print('Number ouf of range')
            continue
        else:
            print(f'Your number is {num}')
            return int(num)


def guessing_game():
    num = random.randint(1, 100)
    while True:
        guess = user_guess()
        if guess == num:
            print('Congrats')
            break
        if guess > num:
            print('Too high :(')
        elif guess < num:
            print('Too low :(')


guessing_game()
"""Number guessing game"""

