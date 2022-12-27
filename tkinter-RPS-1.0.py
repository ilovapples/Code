# Import dependencies
from tkinter import *
import random

# Define the window, the dimensions, and the title (in that order)
master = Tk()
windowWidth = 350
windowHeight = 300
master.geometry(str(windowWidth) + 'x' + str(windowHeight))
master.title("Rock Paper Scissors")
master.resizable(False, False)

options = [
    ['Rock', 0], 
    ['Paper', 1], 
    ['Scissors', 2]
]
computerChoice = random.choice(options)


def chooseRock():
    global chosenItem
    chosenItem = ['Rock', 0]
    
    global showRock
    global showPaper
    global showScissors
    showRock = Label(master, text="You chose: Rock", width=50)
    showRock.place(relx=0.5, rely=0.4675, anchor=CENTER)
    
    global coverOutcome
    coverOutcome = Label(master, text="", width=50)
    coverOutcome.place(relx=0.5, rely=0.8, anchor=CENTER)
    
def choosePaper():
    global chosenItem
    chosenItem = ['Paper', 1]
    
    global showPaper
    global showRock
    global showScissors
    showPaper = Label(master, text="You chose: Paper ", width=50)
    showPaper.place(relx=0.5, rely=0.4675, anchor=CENTER)

    global coverOutcome
    coverOutcome = Label(master, text="", width=50)
    coverOutcome.place(relx=0.5, rely=0.8, anchor=CENTER)
    
def chooseScissors():
    global chosenItem
    chosenItem = ['Scissors', 2]
    
    global showScissors
    global showPaper
    global showRock
    showScissors = Label(master, text="You chose: Scissors", width=50)
    showScissors.place(relx=0.5, rely=0.4675, anchor=CENTER)

    global coverOutcome
    coverOutcome = Label(master, text="", width=50)
    coverOutcome.place(relx=0.5, rely=0.8, anchor=CENTER)
    
def pickWinner():
    global outcome
    outcome = "Undetermined"
    global showWinner
    try:
        if chosenItem == computerChoice:
            outcome = "Tied"
        else:
            if chosenItem[1] == 0 and computerChoice[1] == 1:
                outcome = "Lost"
            elif chosenItem[1] == 0 and computerChoice[1] == 2:
                outcome = "Won"
            elif chosenItem[1] == 1 and computerChoice[1] == 0:
                outcome = "Won"
            elif chosenItem[1] == 1 and computerChoice[1] == 2:
                outcome = "Lost"
            elif chosenItem[1] == 2 and computerChoice[1] == 0:
                outcome = "Lost"
            elif chosenItem[1] == 2 and computerChoice[1] == 1:
                outcome = "Won"
    
        showWinner = Label(master, text="You " + outcome + "! You chose " + chosenItem[0] + ", and the computer chose " + computerChoice[0] + ".", font='Arial 8 bold', width=50)
        showWinner.place(relx=0.5, rely=0.8, anchor=CENTER)
    except NameError:
        print("Can't continue without user selection!")
    mainloop()
    
def confirmChoice():
    try:
        if chosenItem == ["", 0]:
            print("Can't continue without user selection!")
        else:
            pickWinner()
    except NameError:
        print("Can't continue without user selection!")
    
def reset():
    global chosenItem
    chosenItem = ["", 0]
    global outcome
    outcome = "Undefined"
    global showWinner
    showWinner = None    
    global computerChoice
    global options
    computerChoice = random.choice(options)
    global coverOutcome
    coverOutcome = Label(master, text="", width=50)
    coverOutcome.place(relx=0.5, rely=0.8, anchor=CENTER)
    global coverChosenChoice
    coverChosenChoice = Label(master, text="", width=75)
    coverChosenChoice.place(relx=0.5, rely=0.4675, anchor=CENTER)
    mainloop()
# Define the function to start Rock Paper Scissors
def openRPS():
    # Define "title"
    rps_label = Label(master, text="Rock Paper Scissors", font='Arial 17 bold')
    rps_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    # Define buttons to select option
    rock = Button(master, text="ROCK", font='Courier 14 bold', command=chooseRock)
    rock.place(relx=0.175, rely=0.35, anchor=CENTER)
    
    paper = Button(master, text="PAPER", font='Courier 14 bold', command=choosePaper)
    paper.place(relx=0.43, rely=0.35, anchor=CENTER)
    
    scissors = Button(master, text="SCISSORS", font='Courier 14 bold', command=chooseScissors)
    scissors.place(relx=0.75, rely=0.35, anchor=CENTER)
    
    # Define a button to confirm selection
    confirmButton = Button(master, text="Confirm Selection", font='Arial 13', command=confirmChoice)
    confirmButton.place(relx=0.5, rely=0.575, anchor=CENTER)

    # Define a reset button
    resetButton = Button(master, text="Restart Game", font='Courier 10 bold', command=reset)
    resetButton.place(relx=0.5, rely=0.9515, anchor=CENTER)
    mainloop()
    
openRPS()