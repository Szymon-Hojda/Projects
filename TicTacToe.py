board = [' ' for letter in range(10)]

def insert_letter(position , letter):
    board[position] = letter

def print_board(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')

def is_board_full():
    print()
def is_space_on_board(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def is_winner(board):
    if board[1] == board[2] == board[3]:
        print('Winner is: ' + '' )
print('Where you want put your sign?(1-9)')