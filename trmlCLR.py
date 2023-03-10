import os
from platform import system as getos
clearFunc = ""
if getos() == "Windows":
    clearFunc = 'cls'
else:
    clearFunc = 'clear'


def clear():
    os.system(clearFunc)

