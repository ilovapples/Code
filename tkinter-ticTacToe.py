from tkinter import *
master = Tk()
master.geometry("320x320")
master.title("Tic Tac Toe")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
xoro = "X"
xoroint = 1

def checkForWin():
    if " " not in board:
        if board[0] == board[1] == board[2] == "X" or board[0] == board[1] == board[2] == "O":
            quit()
        elif board[3] == board[4] == board[5] == "X" or board[3] == board[4] == board[5] == "O":
            quit()
        elif board[6] == board[7] == board[8] == "X" or board[6] == board[7] == board[8] == "O":
            quit()
        
        elif board[0] == board[3] == board[6] == "X" or board[0] == board[3] == board[6] == "O":
            quit()
        elif board[1] == board[4] == board[7] == "X" or board[1] == board[4] == board[7] == "O":
            quit()
        elif board[2] == board[5] == board[8] == "X" or board[2] == board[5] == board[8] == "O":
            quit()
        
        elif board[0] == board[4] == board[8] == "X" or board[0] == board[4] == board[8] == "O":
            quit()
        elif board[2] == board[4] == board[6] == "X" or board[2] == board[4] == board[6] == "O":
            quit()
        else:
            quit()
    elif " " in board:
        if board[0] == board[1] == board[2] == "X" or board[0] == board[1] == board[2] == "O":
            quit()
        if board[3] == board[4] == board[5] == "X" or board[3] == board[4] == board[5] == "O":
            quit()
        if board[6] == board[7] == board[8] == "X" or board[6] == board[7] == board[8] == "O":
            quit()
        
        if board[0] == board[3] == board[6] == "X" or board[0] == board[3] == board[6] == "O":
            quit()
        if board[1] == board[4] == board[7] == "X" or board[1] == board[4] == board[7] == "O":
            quit()
        if board[2] == board[5] == board[8] == "X" or board[2] == board[5] == board[8] == "O":
            quit()
        
        if board[0] == board[4] == board[8] == "X" or board[0] == board[4] == board[8] == "O":
            quit()
        if board[2] == board[4] == board[6] == "X" or board[2] == board[4] == board[6] == "O":
            quit()
        
def click0():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[0] == " ":
        board[0] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)
    
    space0 = Button(master, font='Courier 40 bold', text=board[0], width=3, height=1, command=click0)
    space0.place(relx=0, rely=0)
    
    checkForWin()

def click1():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[1] == " ":
        board[1] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)

    space1 = Button(master, font='Courier 40 bold', text=board[1], width=3, height=1, command=click1)
    space1.place(relx=0.33, rely=0)

    checkForWin()

def click2():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[2] == " ":
        board[2] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)
    
    space2 = Button(master, font='Courier 40 bold', text=board[2], width=3, height=1, command=click2)
    space2.place(relx=0.66, rely=0)

    checkForWin()

def click3():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[3] == " ":
        board[3] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)
    
    space3 = Button(master, font='Courier 40 bold', text=board[3], width=3, height=1, command=click3)
    space3.place(relx=0, rely=0.33)

    checkForWin()

def click4():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[4] == " ":
        board[4] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)
    
    space4 = Button(master, font='Courier 40 bold', text=board[4], width=3, height=1, command=click4)
    space4.place(relx=0.33, rely=0.33)

    checkForWin()

def click5():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[5] == " ":
        board[5] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)
    
    space5 = Button(master, font='Courier 40 bold', text=board[5], width=3, height=1, command=click5)
    space5.place(relx=0.66, rely=0.33)

    checkForWin()

def click6():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[6] == " ":
        board[6] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)
    
    space6 = Button(master, font='Courier 40 bold', text=board[6], width=3, height=1, command=click6)
    space6.place(relx=0, rely=0.66)

    checkForWin()

def click7():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[7] == " ":
        board[7] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)
    
    space7 = Button(master, font='Courier 40 bold', text=board[7], width=3, height=1, command=click7)
    space7.place(relx=0.33, rely=0.66)

    checkForWin()

def click8():
    global xoro
    global xoroint
    if xoroint%2 == 0:
        xoro = "O"
    else:
        xoro = "X"
    
    if board[8] == " ":
        board[8] = xoro
        xoroint += 1
        print(board)
    else:
        print(board)
    
    space8 = Button(master, font='Courier 40 bold', text=board[8], width=3, height=1, command=click8)
    space8.place(relx=0.66, rely=0.66)

    checkForWin()

def runTicTacToe():
    space0 = Button(master, font='Courier 40 bold', text=board[0], width=3, height=1, command=click0)
    space0.place(relx=0, rely=0)

    space1 = Button(master, font='Courier 40 bold', text=board[1], width=3, height=1, command=click1)
    space1.place(relx=0.33, rely=0)

    space2 = Button(master, font='Courier 40 bold', text=board[2], width=3, height=1, command=click2)
    space2.place(relx=0.66, rely=0)

    space3 = Button(master, font='Courier 40 bold', text=board[3], width=3, height=1, command=click3)
    space3.place(relx=0, rely=0.33)

    space4 = Button(master, font='Courier 40 bold', text=board[4], width=3, height=1, command=click4)
    space4.place(relx=0.33, rely=0.33)

    space5 = Button(master, font='Courier 40 bold', text=board[5], width=3, height=1, command=click5)
    space5.place(relx=0.66, rely=0.33)

    space6 = Button(master, font='Courier 40 bold', text=board[6], width=3, height=1, command=click6)
    space6.place(relx=0, rely=0.66)

    space7 = Button(master, font='Courier 40 bold', text=board[7], width=3, height=1, command=click7)
    space7.place(relx=0.33, rely=0.66)

    space8 = Button(master, font='Courier 40 bold', text=board[8], width=3, height=1, command=click8)
    space8.place(relx=0.66, rely=0.66)

    mainloop()

runTicTacToe()