import os
def clear():
    os.system('cls')
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
    if move == "r":
        board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        printBoard()
    elif move == "":
        print("Invalid Move.")
    elif move == "help":
        print("Commands are:\n\n\"r\" to reset board\nAny number 1 to 9 to choose where to put your piece.\n\"?\" or \"help\" to bring up the help menu.")
    elif move == "?":
        print("Commands are:\n\n\"r\" to reset board\nAny number 1 to 9 to choose where to put you piece.\n\"?\" or \"help\" to bring up the help menu.")
    elif int(move) > 9:
        print("Invalid Move.")
    elif int(move) < 1:
        print("Invalid Move.")
    elif board[int(move)-1] != "_":
        print("Invalid Move.")
    else:
        board[int(move)-1] = xoroTurn
        wasxoroTurn = xoroTurn
        turn += 1
        if (turn%2) == 0:
            xoroTurn = "O"
        elif (turn%2) != 0:
            xoroTurn = "X"
        printBoard()
        if board[int(move)-1] is board[0]:
            if board[0] == wasxoroTurn:
                if board[0] == board[1] == board[2]:
                    print("%s got 3 in a row!" % wasxoroTurn)
                    gameEnd()
                if board[0] == board[3] == board[6]:
                    print("%s got 3 in a row!" % wasxoroTurn)
                    gameEnd()
                if board[0] == board[4] == board[8]:
                    print("%s got 3 in a row!" % wasxoroTurn)
                    gameEnd()
        if board[int(move)-1] is board[1]:
            if board[1] == wasxoroTurn:    
                if board[1] == board[4] == board[7]:
                    print("%s got 3 in a row!" % wasxoroTurn)
                    gameEnd()
                if board[0] == board[1] == board[2]:
                    print("%s got 3 in a row!" % wasxoroTurn)
                    gameEnd()
        if board[int(move)-1] is board[2]:
            if board[2] == wasxoroTurn:
                if board[2] == board[4] == board[6]:
                    print("%s got 3 in a row!" % wasxoroTurn)
                    gameEnd()
                if board[0] == board[1] == board[2]:
                    print("%s got 3 in a row!" % wasxoroTurn)
                    gameEnd()
