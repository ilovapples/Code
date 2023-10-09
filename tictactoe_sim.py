from check_tictactoe_winners import *

temp_board = [" "]*9
p = {}
for i in range(9):
    temp_board[i] = "X"
    p[i] = {}
    for j in range(9):
        if temp_board[j] == " ":
            temp_board[j] = "O"
            p[i][j] = {}
        for k in range(9):# 3
            if temp_board[k] == " ":
                temp_board[k] = "X"
                p[i][j][k] = {}
            for l in range(9):# 4
                if temp_board[l] == " ":
                    temp_board[l] = "O"
                    p[i][j][k][l] = {}
                for m in range(9):# 5
                    if temp_board[m] == " ":
                        temp_board[m] = "X"
                        if get_winner(temp_board):
                            p[i][j][k][l][m] = f"{get_winner(temp_board)} won"
                        else:
                            p[i][j][k][l][m] = {}
                    for n in range(9):# 6
                        if temp_board[n] == " ":
                            temp_board[n] = "O"
                            if get_winner(temp_board):
                               p[i][j][k][l][m][n] = f"{get_winner(temp_board)} won"
                            else:
                               p[i][j][k][l][m][n] = {}
                        