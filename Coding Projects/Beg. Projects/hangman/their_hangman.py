# downsides:
from words import words
import random
import string

# function to verify the word is valid in Python
def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)            # keeping track of what letters can be guessed from all words
    alphabet = set(string.ascii_uppercase)
    used_letters = set()                # what the user has guessed

    lives = 7
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have used these letters: ', ' '.join(used_letters))
        print(f"You have {lives} lives remaining.")

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1

        elif user_letter in used_letters:
            print("Character already used. Please try again.")

        else:
            print("Invalid character")

    # gets here when len(word_letters) = 0 OR lives == 0
    if lives == 0:
        print("Sorry! You died.")
    else:
        print("You guessed the word!")

hangman()