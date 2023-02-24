import os
import platform
clearValue = ""
if platform.system == "Windows":
    clearValue = 'cls'
else:
    clearValue = 'clear'


def clear():
    os.system(clearValue)


board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def printBoard():
    clear()
    print("_____________")
    print("|_%s_|_%s_|_%s_|" % (board[0], board[1], board[2]))
    print("|_%s_|_%s_|_%s_|" % (board[3], board[4], board[5]))
    print("|_%s_|_%s_|_%s_|" % (board[6], board[7], board[8]))


printBoard()
stillPlaying = "y"
turn = 1
xoroTurn = "X"
wasxoroTurn = ""


def gameEnd():
    stillPlaying = input("Play Again? (y/n): ")
    if stillPlaying == "y":
        board[0] = "_"
        board[1] = "_"
        board[2] = "_"
        board[3] = "_"
        board[4] = "_"
        board[5] = "_"
        board[6] = "_"
        board[7] = "_"
        board[8] = "_"
        printBoard()
    elif stillPlaying == "n":
        quit()


while stillPlaying == "y":
    move = input("Move: ")
    if move == "1":
        board[0] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[0] == board[1] == board[2]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[0] == board[3] == board[6]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[0] == board[4] == board[8]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
    
    elif move == "2":
        board[1] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[1] == board[0] == board[2]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[1] == board[4] == board[7]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
    
    elif move == "3":
        board[2] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[2] == board[1] == board[0]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[2] == board[5] == board[8]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[2] == board[4] == board[6]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()

    elif move == "4":
        board[3] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[3] == board[6] == board[0]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[3] == board[4] == board[5]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()

    elif move == "5":
        board[4] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[4] == board[7] == board[1]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[4] == board[5] == board[3]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[4] == board[6] == board[2]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[4] == board[8] == board[0]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
    
    elif move == "6":
        board[5] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[5] == board[3] == board[4]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[5] == board[2] == board[8]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
    
    elif move == "7":
        board[6] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[6] == board[0] == board[3]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[6] == board[7] == board[8]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[6] == board[2] == board[4]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
    
    elif move == "8":
        board[7] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[7] == board[8] == board[6]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[7] == board[1] == board[4]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
    
    elif move == "9":
        board[8] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn % 2) == 0:
            xoroTurn = "O"
        elif (turn % 2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[8] == board[6] == board[7]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[8] == board[2] == board[5]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
        elif board[8] == board[0] == board[4]:
            print("%s got 3 in a row!" % wasxoroTurn)
            gameEnd()
    
    
            
    elif move == "r":
        board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        printBoard()
    elif move == "":
        print("Invalid Move.")
    elif move == "help":
        print("Commands are:\n\n\"r\" to reset board\nAny number 1 to 9 to choose where to put your piece.\n\"?\" or \"help\" to bring up the help menu.")
    elif move == "?":
        print("Commands are:\n\n\"r\" to reset board\nAny number 1 to 9 to choose where to put you piece.\n\"?\" or \"help\" to bring up the help menu.")

    else:
        print("Invalid move.")