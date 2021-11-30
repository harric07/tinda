'''
GAME: HANGMAN
RULES:
    - The computer will pick a random word from a list of words.
    - The player will have to guess the word.
    - The player will only have 6 guesses.
    - The player will be told how many letters are in the word.
    - The player will be told if they have guessed a letter or not.
    - The player will be told if they have guessed the word or not.
    - The player will be told if they have guessed a letter more than once.
'''


from some_english_words import words
import random
import string

def valid_word(words):
    x = random.choice(words)
    while "-" in x or " " in x:
        x = random.choice(words)
    return x.upper()

def hangman():
    w = valid_word(words)
    letters_in_w = set(w)
    a = set(string.ascii_uppercase) 
    # predetermined set of uppercase english letters
    counted_letters = set()
    lives = 7
    while len(letters_in_w) > 0 and lives > 0:
        print("You have used these letters: ", " ".join(counted_letters))
        word_list = [i if i in counted_letters else "-" for i in w]
        print("Current word: ", " ".join(word_list))
        input_letters = input("Guess a letter: ").upper()
        if input_letters in a - counted_letters:
            counted_letters.add(input_letters)
            if input_letters in letters_in_w:
                print("")
            else:
                lives -= 1
                print("/nYour letter", input_letters, "is not in the word.")
        elif input_letters in counted_letters:
            print("/nYou have already guessed this letter.")
        else:
            print("Invalid input.")
    if lives == 0:
        print("/nYou have lost.")
        print(f"Sorry, the word was '{w}'")
    else:
        print(f"/nYou guessed the word '{w}' with '{lives} lives remaining'.")


hangman()


