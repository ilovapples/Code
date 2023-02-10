from termcolor import colored
import os
import time
import random

board = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
]

background_color = 'on_blue'
text_color = 'white'


def numlen(num):
    return len(str(num))
    

def randomly_fill_board(spots: int=2):
    coords = []
    for i in range(spots):
        coords.append([random.randint(0, 3), random.randint(0, 3)])
        
    nums = [
        1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 4
    ]
    
    for i in coords:
        board[i[0]][i[1]] == random.choice(nums)

def print_board():
    printable = '___________________________________________\n|                                         |\n'
    for i in range(4):
        for k in range(3):
            printable += '| '
            
            if k == 0:
                for q in range(4):
                    printable += "|" + colored("‾‾‾‾‾‾‾", text_color, background_color) + "| "
            elif k == 2:
                for q in range(4):
                    printable += "|" + colored("_______", text_color, background_color) + "| "
            else:
                for q in range(4):
                    if numlen(board[i][q])%2 == 0:
                        printable += ("|"
                                        + colored(" ", text_color, background_color)*int((7 - numlen(board[i][q]))/2)
                                        + colored(f"{board[i][q]}", text_color, background_color)
                                        + colored(" ", text_color, background_color)*int((7 - numlen(board[i][q]))/2 + 1)
                                        + "| "
                        )
                    else:
                        printable += ("|"
                                        + colored(" ", text_color, background_color)*int((7 - numlen(board[i][q]))/2)
                                        + colored(f"{board[i][q]}", text_color, background_color)
                                        + colored(" ", text_color, background_color)*int((7 - numlen(board[i][q]))/2)
                                        + "| "
                        )
            printable += '| \n'
        if i == 3:
            printable += '|_________________________________________|\n'
        else:
            printable += '|                                         |\n'
    print(printable)


print_board()
randomly_fill_board(2)
print_board()