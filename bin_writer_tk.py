
# Import dependencies
from tkinter import *

# Define the window, the dimensions, and the title (in that order)
master = Tk()
windowWidth = 1000
windowHeight = 150
master.geometry(str(windowWidth) + 'x' + str(windowHeight))
master.title("Write Binary")
master.resizable(False, False)

digit_index = 0

def flip_0():
    digit_index = 0
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_1():
    digit_index = 1
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_2():
    digit_index = 2
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_3():
    digit_index = 3
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_4():
    digit_index = 4
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_5():
    digit_index = 5
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_6():
    digit_index = 6
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_7():
    digit_index = 7
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_8():
    digit_index = 8
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_9():
    digit_index = 9
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_10():
    digit_index = 10
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_11():
    digit_index = 11
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_12():
    digit_index = 12
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_13():
    digit_index = 13
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_14():
    digit_index = 14
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_15():
    digit_index = 15
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_16():
    digit_index = 16
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_17():
    digit_index = 17
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_18():
    digit_index = 18
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_19():
    digit_index = 19
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_20():
    digit_index = 20
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_21():
    digit_index = 21
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_22():
    digit_index = 22
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_23():
    digit_index = 23
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_24():
    digit_index = 24
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_25():
    digit_index = 25
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_26():
    digit_index = 26
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_27():
    digit_index = 27
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_28():
    digit_index = 28
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_29():
    digit_index = 29
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_30():
    digit_index = 30
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()
def flip_31():
    digit_index = 31
    if digits[digit_index] == 0:
        digits[digit_index] = 1
    else:
        digits[digit_index] = 0
    mainloop()


def all_zero():
    global digits
    digits = [0 for _ in range(32)]

    exec_str = ''
    for i in range(32):
        exec_str += f'\nbutton_{i} = Button(master, text=digits[{i}], font="Courier 10 bold", command=flip_{i}, width=2, height=1)\nbutton_{i}.place(relx=0.0273*{i}+0.05, rely=0.5, anchor=CENTER)'
    exec(exec_str)
    mainloop()
    
    
def all_one():
    global digits
    digits = [1 for _ in range(32)]

    exec_str = ''
    for i in range(32):
        exec_str += f'\nbutton_{i} = Button(master, text=digits[{i}], font="Courier 10 bold", command=flip_{i}, width=2, height=1)\nbutton_{i}.place(relx=0.0273*{i}+0.05, rely=0.5, anchor=CENTER)'
    exec(exec_str)
    mainloop()


def main():
    all_zero()
    
    all_to_zero = Button(master, text="Set all to 0", font="Courier 10 bold", command=all_zero).place(relx=0.25, rely=0.5, anchor=CENTER)
    all_to_one = Button(master, text="Set all to 1", font="Courier 10 bold", command=all_one)

    mainloop()

    
main()