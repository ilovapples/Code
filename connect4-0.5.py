slot0 = ["_", "_", "_", "_", "_", "_"]
slot1 = ["_", "_", "_", "_", "_", "_"]
slot2 = ["_", "_", "_", "_", "_", "_"]
slot3 = ["_", "_", "_", "_", "_", "_"]
slot4 = ["_", "_", "_", "_", "_", "_"]
slot5 = ["_", "_", "_", "_", "_", "_"]
slot6 = ["_", "_", "_", "_", "_", "_"]
slot0Indexing = 0
slot1Indexing = 0
slot2Indexing = 0
slot3Indexing = 0
slot4Indexing = 0
slot5Indexing = 0
slot6Indexing = 0
moveIsInt = 1
moveIs = "X"
isFull = [" ", " ", " ", " ", " ", " ", " "]
def printBoard():
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (slot0[5], slot1[5], slot2[5], slot3[5], slot4[5], slot5[5], slot6[5]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (slot0[4], slot1[4], slot2[4], slot3[4], slot4[4], slot5[4], slot6[4]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (slot0[3], slot1[3], slot2[3], slot3[3], slot4[3], slot5[3], slot6[3]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (slot0[2], slot1[2], slot2[2], slot3[2], slot4[2], slot5[2], slot6[2]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (slot0[1], slot1[1], slot2[1], slot3[1], slot4[1], slot5[1], slot6[1]))
    print("|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" % (slot0[0], slot1[0], slot2[0], slot3[0], slot4[0], slot5[0], slot6[0]))
    print("  %s   %s   %s   %s   %s   %s   %s" % (isFull[0], isFull[1], isFull[2], isFull[3], isFull[4], isFull[5], isFull[6]))
printBoard()


while True:
    if (moveIsInt%2) == 0:
        moveIs = "O"
    elif (moveIsInt%2) != 0:
        moveIs = "X"
    if slot0Indexing > 5:
        isFull[0] = "F"
        printBoard()
    if slot1Indexing > 5:
        isFull[1] = "F"
        printBoard()
    if slot2Indexing > 5:
        isFull[2] = "F"
        printBoard()
    if slot3Indexing > 5:
        isFull[3] = "F"
        printBoard()
    if slot4Indexing > 5:
        isFull[4] = "F"
        printBoard()
    if slot5Indexing > 5:
        isFull[5] = "F"
        printBoard()
    if slot6Indexing > 5:
        isFull[6] = "F"
        printBoard()
    if slot0Indexing == 6:              # Check if the board is full and 
        if slot0Indexing == slot1Indexing == slot2Indexing == slot3Indexing == slot4Indexing == slot5Indexing == slot6Indexing:
            print("The board is full!")
            quit()
    move = input("Choose the spot to enter your piece: ")           # Ask for input for move
    
    
    while move == "":
        if move == "":       # Checks if the move is empty, and if it is, asks for more input.
            print("Invalid.")
            printBoard()
            move = input("Choose the spot to enter your piece: ") 


    if int(move) == 1:                  # Checks the move and puts the piece in the proper location
        if slot0[slot0Indexing] == "_":
            slot0[slot0Indexing] = moveIs
            slot0Indexing += 1
            printBoard()
    elif int(move) == 2:
        if slot1[slot1Indexing] == "_":
            slot1[slot1Indexing] = moveIs
            slot1Indexing += 1
            printBoard()
    elif int(move) == 3:
        if slot2[slot2Indexing] == "_":
            slot2[slot2Indexing] = moveIs
            slot2Indexing += 1
            printBoard()
    elif int(move) == 4:
        if slot3[slot3Indexing] == "_":
            slot3[slot3Indexing] = moveIs
            slot3Indexing += 1
            printBoard()
    elif int(move) == 5:
        if slot4[slot4Indexing] == "_":
            slot4[slot4Indexing] = moveIs
            slot4Indexing += 1
            printBoard()
    elif int(move) == 6:
        if slot5[slot5Indexing] == "_":
            slot5[slot5Indexing] = moveIs
            slot5Indexing += 1
            printBoard()
    elif int(move) == 7:
        if slot6[slot6Indexing] == "_":
            slot6[slot6Indexing] = moveIs
            slot6Indexing += 1
            printBoard()
    
    moveIsInt += 1