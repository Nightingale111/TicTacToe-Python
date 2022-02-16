#Tic-Tac-Toe

#variables

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
Winner = None
gameRunning = True

# Print a gameboard

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#Take player input

def playerInput(board):
    inp = int(input("Enter a number 1 through 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Spot is not available! Please pick a different number.")

#Checking for a win or a tie

def checkRows(board):
    global Winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner = board[6]
        return True

def checkColumns(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner = board[2]
        return True

def checkDiagonals(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        Winner = board[2]
        return True

#Checking for a win (master function)

def checkWin(board):
    global gameRunning
    if checkColumns(board):
        printBoard(board)
        print(f"The winner is {Winner}!")
        gameRunning = False
    elif checkRows(board):
        printBoard(board)
        print(f"The winner is {Winner}!")
        gameRunning = False
    elif checkDiagonals(board):
        printBoard(board)
        print(f"The winner is {Winner}!")
        gameRunning = False

#Checking for a Tie

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

#Switching Players

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#While the game is running:

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
