# Import customGrid module.
# Requires customGrid.py file. 
# WILL NOT WORK WITHOUT 'customGrid.py' FILE
import customGrid as cg

# Define printBoard() function to print the board.
board = cg.generate(4, 4)
def printBoard():
    print("_" * (1+4*4))
    boardPrint = ""
    for i in range(4):
        boardPrint += "|"
        for j in range(4):
            boardPrint += "_%s_|" % (board[i][j])
        boardPrint += "\n"
    print(boardPrint)
    
    
printBoard()

# Define playing variables.
# Define turn and X or O variables.
turn = 1
XORO = "X"
wasXORO = XORO

# Defines the game loop variable.
stillPlaying = "y"

# Starts the game loop.
while stillPlaying == "y":
    
    # Prompts the user for input of X and Y coords of move.
    moveX = input("X of Move: ").lower()
    moveY = input("Y of Move: ").lower()
    
    # Check for special cases, such as ?, help, reset, nothing, etc.
    # Check if input is nothing.
    if moveX == "" or moveY == "":
        printBoard()
        print("Invalid.")
    # Check if input is ? or help and open help menu if so.
    elif moveX == "?" or moveX == "help" or moveY == "?" or moveY == "help":
        print("\nHELP\n\"?\" or \"help\" to open help menu.\nInput 4x4 grid coordinates (X and Y) to input your move.\n\"r\" or \"reset\" to reset the board.\n")
    # Check if input is r or reset and reset board if so.
    elif moveX == "r" or moveX == "reset" or moveY == "r" or moveY == "reset":
        board = cg.generate(4, 4)
        turn = 1
        XORO = "X"
        printBoard()
    else:
        # Set moveY to be the correct value.
        wrongYValues = ["1", "2", "3", "4"]
        correctYValues = ["4", "3", "2", "1"]
        if moveY in wrongYValues:
            moveY = correctYValues[wrongYValues.index(moveY)]
        elif moveY not in wrongYValues:
            print("Invalid.")
            printBoard()
            
        # Check if either of the inputed X or Y values is out of range (greater than 4 or smaller than 1). Happens after all string checks to make sure the input is a number before using int() statements on it, so as to not invoke errors.
        if int(moveX) > 4 or int(moveX) < 1 or int(moveY) > 4 or int(moveY) < 1:
            print("Invalid.")
            printBoard()        
        
        # Check if the spot where the piece is entered is valid.
        elif board[int(moveY)-1][int(moveX)-1] != "_":
            print("Invalid.")
            printBoard()
            
        else:
            
            # Set the corresponding grid square to the piece.
            board[int(moveY)-1][int(moveX)-1] = XORO
            printBoard()
            
            # Set wasXORO to XORO.
            wasXORO = XORO
            
            # Increment the turn by 1.
            turn += 1
            
            # Check whether the piece is X or O.
            if (turn%2) == 0:
                XORO = "O"
            else:
                XORO = "X"
            
            
            # Check if the player has won.
            # Check (1, 4) to (4, 4).
            if board[0][0] == board[0][1] == board[0][2] == board[0][3] == wasXORO:
                printBoard()
                print("%s got 4 in a row!" % wasXORO)
                stillPlaying = input("\nPlay Again? (y/n): ")
                if stillPlaying == "n":
                    quit()
                else:
                    board = cg.generate(4, 4)
                    turn = 1
                    XORO = "X"
                    printBoard()
            # Check (1, 3) to (4, 3).
            elif board[1][0] == board[1][1] == board[1][2] == board[1][3] == wasXORO:
                printBoard()
                print("%s got 4 in a row!" % wasXORO)
                stillPlaying = input("\nPlay Again? (y/n): ")
                if stillPlaying == "n":
                    quit()
                else:
                    board = cg.generate(4, 4)
                    turn = 1
                    XORO = "X"
                    printBoard()
            # Check (1, 2) to (4, 2)
            elif board[2][0] == board[2][1] == board[2][2] == board[2][3] == wasXORO:
                printBoard()
                print("%s got 4 in a row!" % wasXORO)
                stillPlaying = input("\nPlay Again? (y/n): ")
                if stillPlaying == "n":
                    quit()
                else:
                    board = cg.generate(4, 4)
                    turn = 1
                    XORO = "X"
                    printBoard()
            # Check (1, 1) to (4, 1)
            elif board[3][0] == board[3][1] == board[3][2] == board[3][3] == wasXORO:
                printBoard()
                print("%s got 4 in a row!" % wasXORO)
                stillPlaying = input("\nPlay Again? (y/n): ")
                if stillPlaying == "n":
                    quit()
                else:
                    board = cg.generate(4, 4)
                    turn = 1
                    XORO = "X"
                    printBoard()
            # Check ()
