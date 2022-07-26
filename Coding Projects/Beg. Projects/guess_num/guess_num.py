import random

# a function in which the computer generates a number, and you have to guess
def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while (guess!=random_num):
        guess = int(input(f"Guess a num between 1 and {x}: "))
        if guess < random_num:
            print('Sorry, guess again, too low.')
        elif guess > random_num:
            print('Sorry, guess again, too high.')
    
    print(f'Congrats! You have guessed the number {random_num}!')

# a function in which you choose a number, and the computer has to guess
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low!=high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number {guess}!")

computer_guess(1000)

