import simple_colors
board = [
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
]
col1Indx = 5
col2Indx = 5
col3Indx = 5
col4Indx = 5
col5Indx = 5
col6Indx = 5
col7Indx = 5
moveIsInt = 1
moveIs = "X"
isFull = [" ", " ", " ", " ", " ", " ", " "]
def printBoard():
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6]))
    print("  %s  %s  %s  %s  %s  %s  %s" % (isFull[0], isFull[1], isFull[2], isFull[3], isFull[4], isFull[5], isFull[6]))
printBoard()


while True:
    if (moveIsInt%2) == 0:
        moveIs = "O"
    elif (moveIsInt%2) != 0:
        moveIs = "X"
       
    move = input("Choose the spot to enter your piece: ")           # Ask for input for move
    
    
    while move == "":
        if move == "":       # Checks if the move is empty, and if it is, asks for more input.
            print("Invalid.")
            printBoard()
            move = input("Choose the spot to enter your piece: ") 


    if int(move) == 1:                  # Checks the move and puts the piece in the proper location
        if slot0[slot0Indexing] == "__":
            slot0[slot0Indexing] = moveIs
            slot0Indexing += 1
            printBoard()
    elif int(move) == 2:
        if slot1[slot1Indexing] == "__":
            slot1[slot1Indexing] = moveIs
            slot1Indexing += 1
            printBoard()
    elif int(move) == 3:
        if slot2[slot2Indexing] == "__":
            slot2[slot2Indexing] = moveIs
            slot2Indexing += 1
            printBoard()
    elif int(move) == 4:
        if slot3[slot3Indexing] == "__":
            slot3[slot3Indexing] = moveIs
            slot3Indexing += 1
            printBoard()
    elif int(move) == 5:
        if slot4[slot4Indexing] == "__":
            slot4[slot4Indexing] = moveIs
            slot4Indexing += 1
            printBoard()
    elif int(move) == 6:
        if slot5[slot5Indexing] == "__":
            slot5[slot5Indexing] = moveIs
            slot5Indexing += 1
            printBoard()
    elif int(move) == 7:
        if slot6[slot6Indexing] == "__":
            slot6[slot6Indexing] = moveIs
            slot6Indexing += 1
            printBoard()
    
    moveIsInt += 1
