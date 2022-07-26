# downsides: does not out unvalid words, does not keep track of words already written
from words import words as w
import random

computer = random.choice(w)
guesses = 20
result = ["_"] * len(computer)
l = ''.join(result)
print("Your desired word has " + str(len(l)) + " letters.")

# function to start the hangman game
def hangman():
    print("\nWelcome to Hangman! You have a choice of " + str(len(w)) + " words and " + str(guesses) + " letter guesses.")
    loop()
    return 0

# function to insert letters to their proper index
def letter_insert(user):
    i = 0
    for x in computer:
        new = computer[i]
        if user == new:
            result.pop(i)
            result.insert(i, user)
            i += 1
        elif user != new:
            i += 1
    return 0
        
# loop to continue guessing
def loop():
    x = 0
    while x < guesses:
        user = input("Guess a letter: ")

        if user in computer:
            print("You got a letter right!")
            letter_insert(user)
        else:
            print("Nope.")

        newresult = ''.join(result)
        print(f"Your current word is: {newresult}")

        x += 1
        if x == guesses:
            print(f"Sorry, but this is the end of the game! The word was '{computer}'. Try again next time.")
            break
        elif newresult == computer:
            print("\nCongratulations, you win!")
            break
        else:
            continue
    return 0
    
hangman()