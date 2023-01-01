from tkinter import *

master = Tk()
master.title("Calculator")
master.geometry("500x650")
master.resizable(False, False)

def one():
    global expression
    expression += "1"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def two():
    global expression
    expression += "2"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def three():
    global expression
    expression += "3"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def four():
    global expression
    expression += "4"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def five():
    global expression
    expression += "5"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def six():
    global expression
    expression += "6"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def seven():
    global expression
    expression += "7"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def eight():
    global expression
    expression += "8"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def nine():
    global expression
    expression += "9"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def add():
    global expression
    expression += "+"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def subtract():
    global expression
    expression += "-"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def multiply():
    global expression
    expression += "*"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def divide():
    global expression
    expression += "÷"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def power():
    global expression
    expression += "^"
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def evalExpress():
    global expression
    global answer
    expressToEval = expression.replace("^", "**")
    expressToEval = expressToEval.replace("÷", "/")
    expression += " = "
    answer = Label(master, text=eval(expressToEval), width=50, font="Arial 24")
    answer.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)

def clear():
    global expression
    expression = ""
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)
    
    answer = Label(master, text="", width=50, font="Arial 24")
    answer.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    
def runCalc():
    global expression
    expression = ""
    expressionLabel = Label(master, text=expression, width=50, font="Arial 24")
    expressionLabel.place(relx=0.5, rely=0.03, anchor=CENTER)
    
    # Buttons
    button1 = Button(master, text="1", font="Courier 20 bold", width=7, height=3, command=one)
    button1.place(relx=0, rely=0.125)
    
    button2 = Button(master, text="2", font="Courier 20 bold", width=7, height=3, command=two)
    button2.place(relx=0.25, rely=0.125)
    
    button3 = Button(master, text="3", font="Courier 20 bold", width=7, height=3, command=three)
    button3.place(relx=0.5, rely=0.125)
    
    button4 = Button(master, text="4", font="Courier 20 bold", width=7, height=3, command=four)
    button4.place(relx=0, rely=0.3125)
    
    button5 = Button(master, text="5", font="Courier 20 bold", width=7, height=3, command=five)
    button5.place(relx=0.25, rely=0.3125)
    
    button6 = Button(master, text="6", font="Courier 20 bold", width=7, height=3, command=six)
    button6.place(relx=0.5, rely=0.3125)
    
    button7 = Button(master, text="7", font="Courier 20 bold", width=7, height=3, command=seven)
    button7.place(relx=0, rely=0.5)
    
    button8 = Button(master, text="8", font="Courier 20 bold", width=7, height=3, command=eight)
    button8.place(relx=0.25, rely=0.5)
    
    button9 = Button(master, text="9", font="Courier 20 bold", width=7, height=3, command=nine)
    button9.place(relx=0.5, rely=0.5)
    
    buttonAdd = Button(master, text="+", font="Courier 20 bold", width=7, height=3, command=add)
    buttonAdd.place(relx=0.75, rely=0.125)
    
    buttonSubtract = Button(master, text="-", font="Courier 20 bold", width=7, height=3, command=subtract)
    buttonSubtract.place(relx=0.75, rely=0.3125)
    
    buttonMultiply = Button(master, text="*", font="Courier 20 bold", width=7, height=3, command=multiply)
    buttonMultiply.place(relx=0.75, rely=0.5)
    
    buttonDivide = Button(master, text="÷", font="Courier 20 bold", width=7, height=3, command=divide)
    buttonDivide.place(relx=0.75, rely=0.6875)
    
    buttonPower = Button(master, text="^", font="Courier 20 bold", width=7, height=3, command=power)
    buttonPower.place(relx=0.5, rely=0.6875)
    
    buttonClear = Button(master, text="C", font="Courier 20 bold", width=7, height=3, command=clear)
    buttonClear.place(relx=0.25, rely=0.6875)
    
    buttonEquals = Button(master, text="=", font="Courier 20 bold", width=7, height=3, command=evalExpress)
    buttonEquals.place(relx=0, rely=0.6875)
    
    mainloop()
    
runCalc()