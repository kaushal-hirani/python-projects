board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def print_board(board):
    """
    This function is used to print the current status of the board:
    """
    print("Here is the current status : ")
    print("-"*5)
    for row in board:
        print("|".join(row))
        print("-"*5)

def check_win(board, player):
    """
    This function is used to check that if player won or not.
    """
    #check rows
    for row in board:
        if row.count(player) == 3 :
            return True
    
    # check colns
    for col in range(3):
        col_sym = []
        for row in range(3):
            col_sym.append(board[row][col])
        if col_sym.count(player) == 3 :
            return True
    
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    return False
    
        
def make_move(board, player):
    """
    This function is used to taking move while playing.
    """
    print("player {}'s turn :".format(player))
    row = int(input('Enter the row[0-2] : '))
    col = int(input('Enter the col[0-2] : '))
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("Invalid move, try again!")
        return False


def play_game():
    # initialising first player
    # player = input("Select your player ('X' or 'O')")
    # if player == 'X' or player == 'O':

    player = 'X'
    while True:
        print_board(board)
        if make_move(board, player):
            if check_win(board, player):
                print("Player {} wins ! ".format(player))
                break
            if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print("It's a draw!")
                break
            if player == 'X':
                player = 'O'
            elif player == 'O':
                player = 'X'
play_game()


