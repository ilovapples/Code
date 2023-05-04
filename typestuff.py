from pyautogui import write, keyDown, keyUp
from time import sleep
import requests
import xml.sax

xml.sax.make_parser()
sleep(2)

for i in range(1000):
    # keyDown("f5")
    # sleep(0.0000001)
    # keyUp("f5")
    f = requests.get("https://camo.githubusercontent.com/da7a5a29acd22d454226dca6838dd4bde3b7d61ae17a3a85798eca9fb4fed810/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d652f7b426f426b694e4e7d2f636f756e742e737667")
    print(f.text)
    sleep(0.5)