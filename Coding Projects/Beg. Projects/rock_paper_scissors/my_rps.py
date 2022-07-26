import random

def play():
    
    # generating the competitors' choices
    user = input("R for rock, P for paper, S for scissors: ").upper()
    computer = random.randint(1,3)

    # if-else to create the computer string for rock, paper, or scissors
    if computer == 1:
        cstr = 'R'
    elif computer == 2:            
        cstr = 'P'
    elif computer == 3:
        cstr = 'S'
    else:
        cstr = 'INVALID'

    # if-else to determine whether computer input is valid. Acts as a failsafe.
    if cstr == 'INVALID':
        print("Computer error. Please rerun the program.")
        return False
    else:
        print(f"{user} versus {cstr}!")

    # if-else to determine which competitor wins
    if user == cstr:
        print("It's a tie!")
    elif (user == 'S' and cstr == 'R') or (user == 'R' and cstr == 'P') or (user == 'P' and cstr == 'S'):
        print("The computer won.")
    else:
        print("You win! Congratulations!")

    user_again = input("\nWould you like to play again? (Y or N): ").upper()

    if user_again == 'Y':
        play()
    elif user_again == 'N':
        return 0
    else:
        print("Invalid input. Restart the program.")


# calling the function
play()

# thanks once recursive ends
print("Thanks for playing!")