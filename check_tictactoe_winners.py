
def get_winner(board: list):
    try:
        board[8]
        t = "0"
    except IndexError:
        t = "1"
        # random garbage

    if t == "0":
        converted = [0]*9
        for i in range(9):
            converted[i] = {"O": -1, "X": 1, " ": 0, "_": 0}[board[i]]
        
        to_check = [
            [0,1,2], [3,4,5], [6,7,8], #horizontal
            [0,3,6], [1,4,7], [2,5,8], #vertical
            [0,4,8], [2,4,6] #diagonal
        ]
        for p in to_check:
            sum_of_combo = sum([converted[l] for l in p])
            if sum_of_combo == -3:
                return "O"
            elif sum_of_combo == 3:
                return "X"
            else:
                if p is to_check[-1]:
                    return False

    converted = [[0]*3]*3
    for i in range(3):
        for k in range(3):
            converted[i][k] = {"O": -1, "X": 1, " ": 0, "_": 0}[board[i][k]]

    to_check = [
        # horizontal
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],

        # vertical
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],

        # diagonal
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for p in to_check:
        sum_of_combo = sum([
            converted[p[0][0]][p[0][1]],
            converted[p[1][0]][p[1][1]],
            converted[p[2][0]][p[2][1]],
        ])
        if sum_of_combo == -3:
            return "O"
        elif sum_of_combo == 3:
            return "X"
        else:
            if p is to_check[-1]:
                return False
            continue

if __name__ == "__main__":
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"]
    ]

    print(get_winner(board))