# Amazons board game.
brokenPiece = "X"
# Player 1 Characters
chr1 = {
    "piece": "1",
    "x": 0,
    "y": 0,
}
chr2 = {
    "piece": "2",
    "x": 5,
    "y": 0,
}
# Player 2 Characters
chr3 = {
    "piece": "3",
    "x": 0,
    "y": 5,
}
chr4 = {
    "piece": "4",
    "x": 5,
    "y": 5,
}
# Defines the board.
board = [
    ["_", "_", "_", "_", "_", "_"], 
    ["_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_"], 
    ["_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_"], 
    ["_", "_", "_", "_", "_", "_"]
]

def printBoard():
    board[chr1["y"]][chr1["x"]] = chr1["piece"]
    board[chr2["y"]][chr2["x"]] = chr2["piece"]
    board[chr3["y"]][chr3["x"]] = chr3["piece"]
    board[chr4["y"]][chr4["x"]] = chr4["piece"]
    print("")
    printBoard = "____" * 6 + "_\n"
    y = 0
    x = 0
    for _ in range(6):
        for _ in range(6):
            printBoard += "|_" + board[y][x] + "_"
            x += 1
            if x > 5:
                x = 0
        printBoard += "|\n"
        y += 1
    print(printBoard)


def convertY(y):
    wrongY = [0, 1, 2, 3, 4, 5]
    correctY = [5, 4, 3, 2, 1, 0]
    return correctY[wrongY.index(y)]


printBoard()

stillPlaying = "y"
while stillPlaying == "y":
    piece = input("Which piece do you want to move? (1, 2, 3, 4): ")
    direction = input("Which direction? (WASD, name directions, numpad numbers): ").lower()
    pieces = "1234"
    directions = "2-4-6-8-left-right-down-up-s-w-a-d"
    if piece not in pieces:
        printBoard()
        print("Invalid.")
    elif direction[:direction.index("-")] not in directions or direction[(direction.index("-"))+1:] not in directions:
        printBoard()
        print("Invalid.")
    else:
        print(direction[:direction.index("-")])
        print(direction[(direction.index("-")+1):])