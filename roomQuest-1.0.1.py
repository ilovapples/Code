import os
def clear():
    os.system('cls')
bedRoom1 = "YOU"        # Defines room syntax
bedRoom2 = "   "
kitchen = "   "
entrance = "   "
hallWay = "   "
mainRoom = "   "
longHallWay = "   "
currentRoom = "bedroom1"
def printBuilding():
    
    print("|‾‾‾‾‾‾‾‾‾‾‾|     |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")                                               # Function to print the building the player is moving through
    print("|    %s    |     |       %s      |" % (bedRoom1, kitchen))
    print("|____   ____|     |_______   ______|  |‾‾‾‾‾‾‾‾‾|")
    print("     | |                  | |         |   %s   |" % bedRoom2)
    print("|‾‾‾‾   ‾‾‾‾|             | |         |___   ___|")
    print("|    %s    |_____________| |_____________| |______" % entrance)
    print("|                        %s              %s      |" % (hallWay, longHallWay))
    print("|____| |____|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾")
    print("                                 |‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾|")
    print("                                 |                   |")
    print("                                 |        %s        |" % mainRoom)
    print("                                 |                   |")
    print("                                 |___________________|")
def printBuildingCompact():
    clear()
    print("|‾‾‾‾‾‾‾‾‾‾‾|     |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n|    %s    |     |       %s      |\n|____   ____|     |_______   ______|  |‾‾‾‾‾‾‾‾‾|\n     | |                  | |         |   %s   |\n|‾‾‾‾   ‾‾‾‾|             | |         |___   ___|\n|    %s    |_____________| |_____________| |______\n|                        %s              %s      |\n|____| |____|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾\n                                 |‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾|\n                                 |                   |\n                                 |        %s        |\n                                 |                   |\n                                 |___________________|" % (bedRoom1, kitchen, bedRoom2, entrance, hallWay, longHallWay, mainRoom))         # Function to print the building the player is moving through
printBuilding()
while True:
    move = input("Move (Down, Up, Left, Right): ").lower()
    if move == "down":                  # Checks what to do 
        if currentRoom == "bedroom1":       # Moves down from bedroom 1 to entrance
            bedRoom1 = "   "
            entrance = "YOU"
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "entrance"
            printBuildingCompact()
        elif currentRoom == "entrance":     # Moves down from entrance to out of the building
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            print("You left the building.")
            quit()
        elif currentRoom == "kitchen":      # Moves down from kitchen to hallway
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "hallWay":
            printBuildingCompact()
            print("You can't move down.")
        elif currentRoom == "longHallWay":     # Moves down long hall way to main room
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "YOU"
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "mainRoom"
            printBuildingCompact()
        elif currentRoom == "bedroom2":     # Moves down from bedroom 2 to long hall way
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move down.")
    elif move == "right":
        if currentRoom == "bedroom1":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "entrance":         # Moves right from entrance to hall way
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "hallWay":          # Moves right from hall way to long hall way
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "longHallWay":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move right.")
    elif move == "left":
        if currentRoom == "bedroom1":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "hallWay":          # Moves left from hall way to entrace
            hallWay = "   "
            entrance = "YOU"
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "entrance"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "entrance":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "longHallWay":      # Moves left from long hall way to hall way.
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move left.")
    elif move == "up":              # Checks what to do if move is up.
        if currentRoom == "hallWay":        # Moves up from hallway to kitchen
            bedRoom1 = "   "
            entrance = "   "
            kitchen = "YOU"
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "kitchen"
            printBuildingCompact()
        elif currentRoom == "entrance":     # Moves up from entrance to bedroom1
            entrance = "   "
            bedRoom1 = "YOU"
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "bedroom1"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "bedroom1":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "mainRoom":         # Moves up from main room to the long hall way
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "longHallWay":      # Moves up from long hall way to bedroom 2
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "YOU"
            longHallWay = "   "
            currentRoom = "bedroom2"
            printBuildingCompact()
            
            
    if move == "d":                  # Checks what to do 
        if currentRoom == "bedroom1":       # Moves down from bedroom 1 to entrance
            bedRoom1 = "   "
            entrance = "YOU"
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "entrance"
            printBuildingCompact()
        elif currentRoom == "entrance":     # Moves down from entrance to out of the building
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            print("You left the building.")
            quit()
        elif currentRoom == "kitchen":      # Moves down from kitchen to hallway
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "hallWay":
            printBuildingCompact()
            print("You can't move down.")
        elif currentRoom == "longHallWay":     # Moves down long hall way to main room
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "YOU"
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "mainRoom"
            printBuildingCompact()
        elif currentRoom == "bedroom2":     # Moves down from bedroom 2 to long hall way
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move down.")
    elif move == "r":
        if currentRoom == "bedroom1":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "entrance":         # Moves right from entrance to hall way
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "hallWay":          # Moves right from hall way to long hall way
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "longHallWay":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move right.")
    elif move == "l":
        if currentRoom == "bedroom1":
            print("You can't move left.")
            printBuildingCompact()
        elif currentRoom == "hallWay":          # Moves left from hall way to entrace
            hallWay = "   "
            entrance = "YOU"
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "entrance"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "entrance":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "longHallWay":      # Moves left from long hall way to hall way.
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move left.")
    elif move == "u":              # Checks what to do if move is up.
        if currentRoom == "hallWay":        # Moves up from hallway to kitchen
            bedRoom1 = "   "
            entrance = "   "
            kitchen = "YOU"
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "kitchen"
            printBuildingCompact()
        elif currentRoom == "entrance":     # Moves up from entrance to bedroom1
            entrance = "   "
            bedRoom1 = "YOU"
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "bedroom1"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "bedroom1":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "mainRoom":         # Moves up from main room to the long hall way
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "longHallWay":      # Moves up from long hall way to bedroom 2
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "YOU"
            longHallWay = "   "
            currentRoom = "bedroom2"
            printBuildingCompact()

    if move == "2":                  # Checks what to do 
        if currentRoom == "bedroom1":   # Moves down from bedroom 1 to entrance
            bedRoom1 = "   "
            entrance = "YOU"
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "entrance"
            printBuildingCompact()
        elif currentRoom == "entrance":     # Moves down from entrance to out of the building
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            print("You left the building.")
            quit()
        elif currentRoom == "kitchen":      # Moves down from kitchen to hallway
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "hallWay":
            printBuildingCompact()
            print("You can't move down.")
        elif currentRoom == "longHallWay":     # Moves down long hall way to main room
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "YOU"
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "mainRoom"
            printBuildingCompact()
        elif currentRoom == "bedroom2":     # Moves down from bedroom 2 to long hall way
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move down.")
    elif move == "6":
        if currentRoom == "bedroom1":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "entrance":         # Moves right from entrance to hall way
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "hallWay":          # Moves right from hall way to long hall way
            hallWay = "   "
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "longHallWay":
            printBuildingCompact()
            print("You can't move right.")
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move right.")
    elif move == "4":
        if currentRoom == "bedroom1":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "hallWay":          # Moves left from hall way to entrace
            hallWay = "   "
            entrance = "YOU"
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "entrance"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "entrance":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "longHallWay":      # Moves left from long hall way to hall way.
            hallWay = "YOU"
            entrance = "   "
            kitchen = "   "
            bedRoom1 = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "hallWay"
            printBuildingCompact()
        elif currentRoom == "mainRoom":
            printBuildingCompact()
            print("You can't move left.")
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move left.")
    elif move == "8":              # Checks what to do if move is up.
        if currentRoom == "hallWay":        # Moves up from hallway to kitchen
            bedRoom1 = "   "
            entrance = "   "
            kitchen = "YOU"
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "kitchen"
            printBuildingCompact()
        elif currentRoom == "entrance":     # Moves up from entrance to bedroom1
            entrance = "   "
            bedRoom1 = "YOU"
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "   "
            currentRoom = "bedroom1"
            printBuildingCompact()
        elif currentRoom == "kitchen":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "bedroom1":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "mainRoom":         # Moves up from main room to the long hallway
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "   "
            longHallWay = "YOU"
            currentRoom = "longHallWay"
            printBuildingCompact()
        elif currentRoom == "bedroom2":
            printBuildingCompact()
            print("You can't move up.")
        elif currentRoom == "longHallWay":      # Moves up from long hall way to bedroom 2
            entrance = "   "
            bedRoom1 = "   "
            kitchen = "   "
            hallWay = "   "
            mainRoom = "   "
            bedRoom2 = "YOU"
            longHallWay = "   "
            currentRoom = "bedroom2"
            printBuildingCompact()