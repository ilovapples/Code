# from playsound import playsound
from pyautogui import typewrite
from time import sleep
def type(stuff):
    # playsound("countdown.wav")
    sleep(3)
    for i in stuff:
        typewrite(i)
        sleep(0.000001)
type(input("What do you want to type?: "))
