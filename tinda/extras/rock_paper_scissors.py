import random

'''
ROCK, PAPER, SCISSORS
RULES:
    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock
'''



def play():
    user = input("What's your choice?\nPress 'R' for 'Rock', 'P' for 'Paper', or 'S' for 'Scissors': ").lower()
    computer = random.choice(['r', 'p', 's'])
    dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    if user == computer:
        return f"It's a tie! Computer had '{dict[computer]}' too."
    elif win(user, computer):
        return f"You win!, computer had '{dict[computer]}'."
    else:
        return f"You lose!, computer had '{dict[computer]}'."


def win(player, opponent):
    # return True if player wins
    # r > s, p > r, s > p
    if player == 'r' and opponent == 's':
        return True
    elif player == 'p' and opponent == 'r':
        return True
    elif player == 's' and opponent == 'p':
        return True
    else:
        return False



print(play())
