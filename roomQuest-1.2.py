import os
import platform
from getkey import keys, getkey
if platform.system() == "Windows":
    clearMethod = 'cls'
else:
    clearMethod = 'clear'
def clear():
    os.system(clearMethod)
rooms = ["bedRoom1", "entrance", "hallWay", "kitchen", "longHallWay", "bedRoom2", "mainRoom", "hasLeft", "shed", "startOfLongHallway"]
inBedRoom1 = ["YOU", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
inEntrance = ["   ", "YOU", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
inHallWay = ["   ", "   ", "YOU", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
inKitchen = ["   ", "   ", "   ", "YOU", "   ", "   ", "   ", "   ", "   ", "   "]
inLongHallWay = ["   ", "   ", "   ", "   ", "YOU", "   ", "   ", "   ", "   ", "   "]
inBedRoom2 = ["   ", "   ", "   ", "   ", "   ", "YOU", "   ", "   ", "   ", "   "]
inMainRoom = ["   ", "   ", "   ", "   ", "   ", "   ", "YOU", "   ", "   ", "   "]
outside = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "YOU", "   ", "   "]
inShed = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "YOU", "   "]
inStartOfLongHallway = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "YOU"]
nowhere = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
inRoom = inBedRoom1
def printBuilding():
    clear()
    print("|‾‾‾‾‾‾‾‾‾‾‾|     |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")                                               # Function to print the building the player is moving through
    print("|    %s    |     |       %s      |" % (inRoom[0], inRoom[3]))
    print("|____   ____|     |_______   ______|  |‾‾‾‾‾‾‾‾‾|")
    print("     | |                  | |         |   %s   |" % inRoom[5])
    print("|‾‾‾‾   ‾‾‾‾|             | |         |___   ___|")
    print("|           |_____________| |_____________| |______")
    print("|    %s         %s     %s              %s      |" % (inRoom[1], inRoom[9], inRoom[2], inRoom[4]))
    print("|____| |____|‾‾‾‾| |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾")
    print("                 | |             |‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾|")
    print("             |‾‾‾   ‾‾‾|_________|                   |")
    print("     %s     |   %s             |        %s        |" % (inRoom[7], inRoom[8], inRoom[6]))
    print("             |_________|‾‾‾‾‾‾‾‾‾|                   |")
    print("                                 |___________________|")
def roomERROR(move):
    printBuilding()
    print("You can't move %s." % move)
def leave():
    printBuilding()

printBuilding()
while True:
    key = ""
    print("Move (wasd, arrows): ", end='')
    while True:
        key = getkey()
        print(key)
        if key.lower() in "wasd":
            move = key.lower()
            break
        elif key in [keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT]:
            move = {keys.UP: "w", keys.DOWN: "s", keys.LEFT: "a", keys.RIGHT: "d"}[key]
            break
    # move = input("Move (Down, Up, Left, Right): ").lower()
    if move == "":
        print("Invalid Move")
        printBuilding()
    else:

        if inRoom == inBedRoom1:
            if move == "s":
                inRoom = inEntrance
                printBuilding()

            elif move == "d":
                roomERROR("right")

            elif move == "a":
                roomERROR("left")

            elif move == "w":
                roomERROR("up")


        elif inRoom == inEntrance:
            if move == "s":
                inRoom = outside
                printBuilding()

            elif move == "d":
                inRoom = inStartOfLongHallway
                printBuilding()

            elif move == "a":
                roomERROR("left")

            elif move == "w":
                inRoom = inBedRoom1
                printBuilding()


        elif inRoom == inStartOfLongHallway:
            if move == "s":
                inRoom = inShed
                printBuilding()
            elif move == "d":
                inRoom = inHallWay
                printBuilding()
            elif move == "a":
                inRoom = inEntrance
                printBuilding()
            elif move == "w":
                roomERROR("up")


        elif inRoom == inHallWay:
            if move == "s":
                roomERROR("down")

            elif move == "d":
                inRoom = inLongHallWay
                printBuilding()

            elif move == "a":
                inRoom = inStartOfLongHallway
                printBuilding()

            elif move == "w":
                inRoom = inKitchen
                printBuilding()


        elif inRoom == inKitchen:
            if move == "s":
                inRoom = inHallWay
                printBuilding()

            elif move == "d":
                roomERROR("right")

            elif move == "a":
                roomERROR("left")

            elif move == "w":
                roomERROR("up")


        elif inRoom == inLongHallWay:
            if move == "s":
                inRoom = inMainRoom
                printBuilding()

            elif move == "d":
                roomERROR("right")

            elif move == "a":
                inRoom = inHallWay
                printBuilding()

            elif move == "w":
                inRoom = inBedRoom2
                printBuilding()


        elif inRoom == inBedRoom2:
            if move == "s":
                inRoom = inLongHallWay
                printBuilding()

            elif move == "d":
                roomERROR("right")


            elif move == "a":
                roomERROR("left")

            elif move == "w":
                roomERROR("up")

        
        elif inRoom == inMainRoom:
            if move == "s":
                roomERROR("down")
            
            elif move == "d":
                roomERROR("right")

            elif move == "a":
                inRoom = inShed
                printBuilding()

            elif move == "w":
                inRoom = inLongHallWay
                printBuilding()
        

        elif inRoom == inShed:
            if move == "s":
                roomERROR("down")
            elif move == "d":
                inRoom = inMainRoom
                printBuilding()
            elif move == "a":
                roomERROR("left")
            elif move == "w":
                inRoom = inStartOfLongHallway
                printBuilding()

        
        elif inRoom == outside:
            if move == "s":
                inRoom = nowhere
                printBuilding()
                quit()
            elif move == "d":
                roomERROR("right")
            elif move == "a":
                inRoom = nowhere
                printBuilding()
                quit()
            elif move == "w":
                inRoom = inEntrance
                printBuilding()
