class TicTacToe:
    def __init__(self):
        # using a list to represent 9 space board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None # keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # print which numbers correspond to each spot
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        # WITH LIST COMPREHENSION
        return [i for i,spot in enumerate(self.board) if spot == ' ']

        # WITHOUT LIST COMPREHENSION
        # moves = []
        # # enumerate creates a list of tuples with index, value
        # for (i,spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    
    def empty_squares(self): # returns Boolean
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())
        # OR return self.board.couunt(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] == letter
            if self.winner(square,letter):
                self.current_winner == letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere...check all possibilities
        pass
    
def play(game, x_player, o_player, pgame=True):
    # returns winner of game, or None for a tie
    if pgame:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while game still has empty squares

    while game.empty_squares():
        # getting a move
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # defining a function to make a move
        if game.make_move(square, letter):
            if pgame:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just an empty line

            if game.current_winner:
                if pgame:
                    print(letter + " wins!")
                return letter
            
            # switching players
            letter = 'O' if letter == 'X' else 'X'
        
        if pgame:
            print("It's a tie.")