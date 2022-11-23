import random
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
def printBoard():
    print("_____________")
    print("|_%s_|_%s_|_%s_|" % (board[0], board[1], board[2]))
    print("|_%s_|_%s_|_%s_|" % (board[3], board[4], board[5]))
    print("|_%s_|_%s_|_%s_|" % (board[6], board[7], board[8]))
printBoard()
stillPlaying = "y"
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
    elif int(move) > 9:
        print("Invalid Move.")
    elif int(move) < 1:
        print("Invalid Move.")
    elif board[int(move)-1] != "_":
        print("Invalid Move.")
    else:
        board[int(move)-1] = "X"
        printBoard()
        if board[int(move)-1] is board[0]:
            if board[0] == "X":
                if board[0] == board[1] == board[2]:
                    print("X got 3 in a row!")
                    gameEnd()
                if board[0] == board[3] == board[6]:
                    print("X got 3 in a row!")
                    gameEnd()
                if board[0] == board[4] == board[8]:
                    print("X got 3 in a row!")
                    gameEnd()
        if board[int(move)-1] is board[1]:
            if board[1] == "X":    
                if board[1] == board[4] == board[7]:
                    print("X got 3 in a row!")
                    gameEnd()
                if board[0] == board[1] == board[2]:
                    print("X got 3 in a row!")
                    gameEnd()
        if board[int(move)-1] is board[2]:
            if board[2] == "X":
                if board[2] == board[4] == board[6]:
                    print("X got 3 in a row!")
                    gameEnd()
                if board[0] == board[1] == board[2]:
                    print("X got 3 in a row!")
                    gameEnd()
                    
        aiMove = 0            
        while board[aiMove] != "_":
            aiMove = random.randint(0, 8)
        board[aiMove] = "O"
        printBoard()
        if board[int(move)-1] is board[0]:
            if board[0] == "O":
                if board[0] == board[1] == board[2]:
                    print("O got 3 in a row!")
                    gameEnd()
                if board[0] == board[3] == board[6]:
                    print("O got 3 in a row!")
                    gameEnd()
                if board[0] == board[4] == board[8]:
                    print("O got 3 in a row!")
                    gameEnd()
        if board[int(move)-1] is board[1]:
            if board[1] == "O":    
                if board[1] == board[4] == board[7]:
                    print("O got 3 in a row!")
                    gameEnd()
                if board[0] == board[1] == board[2]:
                    print("O got 3 in a row!")
                    gameEnd()
        if board[int(move)-1] is board[2]:
            if board[2] == "O":
                if board[2] == board[4] == board[6]:
                    print("O got 3 in a row!")
                    gameEnd()
                if board[0] == board[1] == board[2]:
                    print("O got 3 in a row!")
                    gameEnd()