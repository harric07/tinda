'''
Guess the number game:
    1. one where the computer picks a random number between 1 and the number you pick
        and the user has to guess the number
    2. one where you pick the random number and the computer has to guess the number
'''

import random


def guess_the_number(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        attempts += 1
        if guess == random_number:
            print(f"No. of attempts: {attempts},  You guessed it!")
        elif guess > random_number:
            print(f"No. of attempts: {attempts}, Sorry, Too high!")
        else:
            print(f"No. of attempts: {attempts}, Sorry, Too low!")
    print(f"Yay, congrats. You guessed the random number '{random_number}' which I picked in '{attempts}' attempts.")

guess_the_number(10)



def computer_guess(x):
    low, high = 1, x
    feedback = ""
    attempts = 0
    while feedback != 'correct':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)? ").lower()
        attempts += 1
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay, I guessed the random number '{guess}' which you picked in '{attempts}' attempts.")
            break
        else:
            print("Please enter H, L or C")
            continue

computer_guess(10)
