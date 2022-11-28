import os
import platform
clearFunc = ''
if platform.system == "Windows":
    clearFunc = 'cls'
else:
    clearFunc = 'clear'
def clear():
    os.system(clearFunc)