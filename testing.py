def printBoard(cols, rows):
    customBoard = changeBoardSize(cols, rows)
    print("_" * (1+4*cols))
    board = ""
    for i in range(rows):
        board += "|"
        for j in range(cols):
            board += "___|"
        board += "\n"
    print(board)
def changeBoardSize(cols, rows):
    customBoard = []
    for _ in range(rows):
        customBoard.append([])
        for _ in range(cols):
            customBoard[-1].append("_")
    return customBoard
while True:
    printBoard(int(input("X: ")), int(input("Y: ")))