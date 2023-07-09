# this is a tic-tac-toe python game for 2 players.

def display_board(board):
    # 3 x 3 tic-tac-toe board ranging from index 0 to index 8.
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])



def player_marker():    # this method will define the player's marker (X or O).

    '''
    OUTPUT = (PLAYER1 MARKER, PLAYER2 MARKER)
    '''

    MARKER = ''

    while (MARKER != 'X' and MARKER != 'O'):
        MARKER = input("Player 1, Please choose 'X' or 'O': ")    # prompt the user to enter X or O.

    if MARKER == 'X':

        return ('X', 'O')


    else:

        return ('O', 'X')


def place_marker(board, marker, position):   # provided the board, choose the index you'd like to place your marker at
    board[position] = marker


def who_goes_first(): # helps determine the order of which player goes first.
    import random
    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        return "Player1's turn."
    else:
        return "Player2's turn."
    return


def win_check(board, mark):
    return (board[0] == mark and board[1] == mark and board[2] == mark) or \
    (board[0] == board[3] == board[6] == mark) or \
    (board[2] == board[5] == board[8] == mark) or (board[6] == board[7] == board[8] == mark) or \
    (board[6] == board[4] == board[2] == mark) or (board[8] == board[4] == board[0] == mark) or \
    (board[3] == board[4] == board[5] == mark) or (board[0] == board[1] == board[2] == mark)


test_board = ['n','n','n','n','n','n','n','n','n','n']      # n represents empty spaces


display_board(test_board) # original board
print()
print(player_marker())
print()
print(who_goes_first())


print()
place_marker(test_board, "X", 0)
place_marker(test_board, "O", 4)
place_marker(test_board, "X", 1)
place_marker(test_board, "O", 2)
place_marker(test_board, "X", 3)
display_board(test_board)
print()
print(win_check(test_board, "O"))   # prints false because O has not won yet.
print()
place_marker(test_board, "O", 6)
display_board(test_board)
print()
print(win_check(test_board, "O"))   # prints true because O has won the game.




