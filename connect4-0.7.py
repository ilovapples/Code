# WORK IN PROGRESS
board = [
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
]
colIndx = 5
moveIsInt = 1
moveIs = "X"
isFull = [" ", " ", " ", " ", " ", " ", " "]

# Define the function to print the board.
def printBoard():
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("  %s  %s  %s  %s  %s  %s  %s" % (isFull[0], isFull[1], isFull[2], isFull[3], isFull[4], isFull[5], isFull[6]))
printBoard()

stillPlaying = "y"
while stillPlaying = "y":
    if (moveIsInt%2) == 0:
        moveIs = "O"
    elif (moveIsInt%2) != 0:
        moveIs = "X"
    
    # Ask for move.
    move = ""
    while move == "" or int(move) > 7 or int(move) < 1 or board[col:
        move = input("Column to place your piece (numver 1-7): ")
        
