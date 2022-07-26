secret_word = "giraffe"
guess = input("Guess which animal I'm thinking of!: ").lower()

if guess == secret_word:
    print("Congrats! You win!")
else:
    guess_count = 0
    guess_limit = 4

while guess != secret_word and guess_count <= guess_limit:
    guess = input("Nope! Try again: ").lower()
    guess_count += 1

    if guess_count == guess_limit and guess != secret_word:
        print("You lose the game...try again next time.")
        guess_count = guess_limit+1
    elif guess == secret_word:
        print("Congrats! You win!")
        guess_count = guess_limit+1
