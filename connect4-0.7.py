# WORK IN PROGRESS
# HAS SOME BUGS:
"""
#1: Doesn't show what pieces are in each column until it fills.

#2: Only swaps pieces when using different columns. Pieces in column one for example will all be X or all O, and same for the other columns.


...and probably others that I haven't found. 
"""


# Import os and platform.
import os, platform
# Check what operating system the program is running on.
if platform.system() == "Windows":
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')
        
# Define the variable that holds the board places.
board = [
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
]
colIndxs = [5, 5, 5, 5, 5, 5, 5]
moveIsInt = 1
moveIs = "X"
isFull = [" ", " ", " ", " ", " ", " ", " "]

# Define the function to print the board.
def printBoard():
    clear()
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("  %s   %s   %s   %s   %s   %s   %s" % (isFull[0], isFull[1], isFull[2], isFull[3], isFull[4], isFull[5], isFull[6]))

stillPlaying = "y"
while stillPlaying == "y":
    if (moveIsInt%2) == 0:
        moveIs = "O"
    elif (moveIsInt%2) != 0:
        moveIs = "X"
    
    # Ask for move.
    move = ""
    printBoard()
    move = input(f"{moveIs}'s Turn  |   Column to place your piece (number 1-7): ")

    if move == "" or int(move) > 7 or int(move) < 1 or board[colIndxs[int(move)-1]][int(move)-1] != "_":
        print("Invalid Move.")
    
    else:
        board[colIndxs[int(move)-1]][int(move)-1] = moveIs
        colIndxs[int(move)-1] -= 1
        moveIsInt += 1
        printBoard()

        if colIndxs[int(move)-1] < 0:
            isFull[int(move)-1] = "F"
            printBoard()
            print("That column is full!")
        