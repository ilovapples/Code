# VERSION 1.3.1
# Requires 'check_tictactoe_winners.py'

import os
import platform
clearValue = ""
if platform.system == "Windows":
    clearValue = 'cls'
else:
    clearValue = 'clear'

from check_tictactoe_winners import *


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
        
    if move == "r":
        board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        printBoard()
    elif move == "":
        print("Invalid Move.")
    elif move == "help":
        print("Commands are:\n\n\"r\" to reset board\nAny number 1 to 9 to choose where to put your piece.\n\"?\" or \"help\" to bring up the help menu.")
    elif move == "?":
        print("Commands are:\n\n\"r\" to reset board\nAny number 1 to 9 to choose where to put you piece.\n\"?\" or \"help\" to bring up the help menu.")


    elif int(move) < 10 and int(move) > 0:
        if board[int(move)-1] == "_":
            board[int(move)-1] = xoroTurn
            printBoard()
            turn += 1
            wasxoroTurn = xoroTurn
            if turn%2 == 0:
                xoroTurn = "O"
            else:
                xoroTurn = "X"
        else:
            print("Invalid Move.")

        if get_winner(board):
            print(f"Player {get_winner(board)} got 3 in a row!")
            gameEnd()
        elif not get_winner(board) and board.count("_") == 0:
            print("It's a tie!")
            gameEnd()

    else:
        print("Invalid move.")