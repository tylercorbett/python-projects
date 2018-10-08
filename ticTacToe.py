#Tic-Tac-Toe by Tyler Corbett (thetylercorbett@gmail.com) Oct. 2018

# GLOBAL VARIABLES
currentTurn = 'X'

board = {
    'topLeft':' ', 'topMid':' ', 'topRight':' ',
    'midLeft':' ', 'midMid':' ', 'midRight':' ',
    'botLeft':' ', 'botMid':' ', 'botRight':' '
}

gameIsWon = False
###

# FUNCTIONS

def printBoard():
    print('\n')
    print(board['topLeft'] + '|' + board['topMid'] + '|' + board['topRight'] + '\n' +
          board['midLeft'] + '|' + board['midMid'] + '|' + board['midRight'] + '\n' +
          board['botLeft'] + '|' + board['botMid'] + '|' + board['botRight'] + '\n')
    
def changeTurn():
    global currentTurn
    if (currentTurn == 'X'):
        currentTurn = 'O'
        print('Current turn: ' + currentTurn)
    else:
        currentTurn = 'X'
        print('Current turn: ' + currentTurn)

def getInput():
    nextMove = input('What space would you like to play? ')
    if (nextMove not in board):
        print('Enter valid input')
        getInput()
    elif (board[nextMove] == 'X' or board[nextMove] == 'O'):
        print('That space is already taken!')
        getInput()
    else:
        board[nextMove] = currentTurn

###

def checkForWinner():
    global gameIsWon
    # Horizontal combos
    if (board['topLeft'] + board['topMid'] + board['topRight'] == 'XXX'):
        printBoard()
        print('X wins!')
        gameIsWon = True
    elif (board['topLeft'] + board['topMid'] + board['topRight'] == 'OOO'):
        printBoard()
        print('O wins!')
        gameIsWon = True
    elif (board['midLeft'] + board['midMid'] + board['midRight'] == 'XXX'):
        printBoard()
        print('X wins!')
        gameIsWon = True
    elif (board['midLeft'] + board['midMid'] + board['midRight'] == 'OOO'):
        printBoard()
        print('O wins!')
        gameIsWon = True
    elif (board['botLeft'] + board['botMid'] + board['botRight'] == 'XXX'):
        printBoard()
        print('X wins!')
        gameIsWon = True
    elif (board['botLeft'] + board['botMid'] + board['botRight'] == 'OOO'):
        printBoard()
        print('O wins!')
        gameIsWon = True
    ###
    # Vertical combos
    elif (board['topLeft'] + board['midLeft'] + board['botLeft'] == 'XXX'):
        printBoard()
        print('X wins!')
        gameIsWon = True
    elif (board['topLeft'] + board['midLeft'] + board['botLeft'] == 'OOO'):
        printBoard()
        print('O wins!')
        gameIsWon = True
    elif (board['topMid'] + board['midMid'] + board['botMid'] == 'XXX'):
        printBoard()
        print('X wins!')
        gameIsWon = True
    elif (board['topMid'] + board['midMid'] + board['botMid'] == 'OOO'):
        printBoard()
        print('O wins!')
        gameIsWon = True
    elif (board['topRight'] + board['midRight'] + board['botRight'] == 'XXX'):
        printBoard()
        print('X wins!')
        gameIsWon = True
    elif (board['topRight'] + board['midRight'] + board['botRight'] == 'OOO'):
        printBoard()
        print('O wins!')
        gameIsWon = True
    ###
    # Both diagonals
    elif (board['topLeft'] + board['midMid'] + board['botRight'] == 'XXX'):
        printBoard()
        print('X wins!')
        gameIsWon = True
    elif (board['topLeft'] + board['midMid'] + board['botRight'] == 'OOO'):
        printBoard()
        print('O wins!')
        gameIsWon = True
    elif (board['topRight'] + board['midMid'] + board['botLeft'] == 'XXX'):
        printBoard()
        print('X wins!')
        gameIsWon = True
    elif (board['topRight'] + board['midMid'] + board['botLeft'] == 'OOO'):
        printBoard()
        print('O wins!')
        gameIsWon = True
    ###

# Run the game
while (gameIsWon == False):
    changeTurn()
    printBoard()
    getInput()
    checkForWinner()
###


# Create function to check if input has been used already or is invalid