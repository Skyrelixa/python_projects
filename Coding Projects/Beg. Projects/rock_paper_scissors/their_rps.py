import random

def play():
    user = input('R, P, or S?: ').upper()
    computer = random.choice(['r', 'p', 's'])       # useful choice function! could have used this instead of number gen

    if user == computer:
        return 'You tied'

    if is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost.'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

play()