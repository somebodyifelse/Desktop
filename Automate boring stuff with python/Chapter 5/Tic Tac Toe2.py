Board = {'1': ' ','2': ' ','3': ' ',
         '4': ' ','5': ' ','6': ' ',
         '7': ' ','8': ' ','9': ' '}
def printBoard(board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
turn = 'X'
for i in range(9):
        printBoard(Board)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        Board [move] = turn
        if turn == 'X':
                turn = '0'
        else:
                turn = 'X'

printBoard(board)
