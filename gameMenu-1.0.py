import random
import os


def clear():
    os.system('cls')


def games():
    def hangMan():
        stillPlaying = "y"
        head = " "
        leftArm = " "
        torso = " "
        rightArm = " "
        leftLeg = " "
        rightLeg = " "
        punishment = 0
        letterNumber = 0
        wrongLetterIndexing = 0
        letterIndexing = 0
        wordIndexing = 0
        word = input("Word (Hide this!): ")
        letter = ["", "", "", "", "", "", "", "",
                  "", "", "", "", "", "", "", "", "", ""]
        correctLetters = ["", "", "", "", "", "", "",
                          "", "", "", "", "", "", "", "", "", "", ""]
        wrongLetters = [" ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " "]

        def printHangMan():
            clear()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWrong Letters:       /¯¯¯¯¯¯\\")
            print(" %s %s %s %s             |      |" % (
                wrongLetters[0], wrongLetters[1], wrongLetters[2], wrongLetters[3]))
            print(" %s %s %s %s             %s      |" % (
                wrongLetters[4], wrongLetters[5], wrongLetters[6], wrongLetters[7], head))
            print(" %s %s %s %s            %s%s%s     |" % (
                wrongLetters[8], wrongLetters[9], wrongLetters[10], wrongLetters[11], leftArm, torso, rightArm))
            print(" %s %s %s %s            %s %s   __/__" %
                  (wrongLetters[12], wrongLetters[13], wrongLetters[14], wrongLetters[15], leftLeg, rightLeg))
            print("\n           %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (letter[0], letter[1], letter[2], letter[3], letter[4], letter[
                  5], letter[6], letter[7], letter[8], letter[9], letter[10], letter[11], letter[12], letter[13], letter[14], letter[15], letter[16], letter[17]))
        for i in range(len(word)):
            letter[letterNumber] = "_"
            correctLetters[letterNumber] = word.lower()[letterNumber]
            letterNumber += 1
        printHangMan()
        while stillPlaying == "y":
            letterGuess = input("Guess a letter: ")
            letterGuess = letterGuess.lower()
            if letterGuess == "reset":
                letter = ["", "", "", "", "", "", "", "",
                          "", "", "", "", "", "", "", "", "", ""]
                wrongLetters = [" ", " ", " ", " ", " ", " ", " ",
                                " ", " ", " ", " ", " ", " ", " ", " ", " "]
                correctLetters = ["", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", ""]
                word = input("\nWord (Hide this!): ")
                for i in range(len(word)):
                    letter[letterNumber] = "_"
                    correctLetters[letterNumber] = word.lower()[letterNumber]
                    letterNumber += 1
                printHangMan()
            elif letterGuess == "menu":
                games()
            else:
                # Overly simple code to create the "Hang Man" if the letter isn't in the word.
                if letterGuess not in word:
                    print("The letter %s is not in the word." % letterGuess)
                    wrongLetters[wrongLetterIndexing] = letterGuess
                    wrongLetterIndexing += 1
                    if punishment == 0:
                        head = "O"
                    elif punishment == 1:
                        torso = "|"
                    elif punishment == 2:
                        leftArm = "/"
                    elif punishment == 3:
                        rightArm = "\\"
                    elif punishment == 4:
                        leftLeg = "/"
                    elif punishment == 5:
                        rightLeg = "\\"
                    punishment += 1
                    printHangMan()
                    if punishment > 6:
                        print("You Lost! The word was %s." % word)
                        quit()
                # Overly complicated code to check if a letter is in the string.
                elif letterGuess in word:
                    print("The letter %s is in the word!" % letterGuess)
                    wordIndexing = word.index(letterGuess)
                    for x in range(word.count(letterGuess)):
                        letter[word.index(
                            letterGuess, (wordIndexing))] = letterGuess
                        wordIndexing += 1
                        checkForLetterGuess = word.find(
                            letterGuess, wordIndexing)
                        if checkForLetterGuess < 0:
                            break
                        elif checkForLetterGuess > -1:
                            letter[word.find(
                                letterGuess, (wordIndexing))] = letterGuess
                    printHangMan()
                if correctLetters == letter:            # Ends the game
                    print("You won Hang Man! The word was %s." % word)
                    quit()

    def ticTacToe():
        board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

        def printBoard():
            clear()
            print("_____________")
            print("|_%s_|_%s_|_%s_|" % (board[0], board[1], board[2]))
            print("|_%s_|_%s_|_%s_|" % (board[3], board[4], board[5]))
            print("|_%s_|_%s_|_%s_|" % (board[6], board[7], board[8]))
        printBoard()
        stillPlaying = "y"
        turn = 1
        xoroTurn = "X"
        wasxoroTurn = ""

        def gameEnd():
            stillPlaying = input("Play Again? (y/n): ")
            if stillPlaying == "y":
                board[0] = "_"
                board[1] = "_"
                board[2] = "_"
                board[3] = "_"
                board[4] = "_"
                board[5] = "_"
                board[6] = "_"
                board[7] = "_"
                board[8] = "_"
                printBoard()
            elif stillPlaying == "n":
                quit()
        while stillPlaying == "y":
            move = input("Move: ")
            if move == "r":
                board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                printBoard()
            elif move == "":
                print("Invalid Move.")
            elif move == "menu":
                games()
            elif move == "help":
                print("Commands are:\n\n\"r\" to reset board\nAny number 1 to 9 to choose where to put your piece.\n\"?\" or \"help\" to bring up the help menu.")
            elif move == "?":
                print("Commands are:\n\n\"r\" to reset board\nAny number 1 to 9 to choose where to put you piece.\n\"?\" or \"help\" to bring up the help menu.")
            elif int(move) > 9:
                print("Invalid Move.")
            elif int(move) < 1:
                print("Invalid Move.")
            elif board[int(move)-1] != "_":
                print("Invalid Move.")
            else:
                board[int(move)-1] = xoroTurn
                wasxoroTurn = xoroTurn
                turn += 1
                if (turn % 2) == 0:
                    xoroTurn = "O"
                elif (turn % 2) != 0:
                    xoroTurn = "X"
                printBoard()
                if board[int(move)-1] is board[0]:
                    if board[0] == wasxoroTurn:
                        if board[0] == board[1] == board[2]:
                            print("%s got 3 in a row!" % wasxoroTurn)
                            gameEnd()
                        if board[0] == board[3] == board[6]:
                            print("%s got 3 in a row!" % wasxoroTurn)
                            gameEnd()
                        if board[0] == board[4] == board[8]:
                            print("%s got 3 in a row!" % wasxoroTurn)
                            gameEnd()
                if board[int(move)-1] is board[1]:
                    if board[1] == wasxoroTurn:
                        if board[1] == board[4] == board[7]:
                            print("%s got 3 in a row!" % wasxoroTurn)
                            gameEnd()
                        if board[0] == board[1] == board[2]:
                            print("%s got 3 in a row!" % wasxoroTurn)
                            gameEnd()
                if board[int(move)-1] is board[2]:
                    if board[2] == wasxoroTurn:
                        if board[2] == board[4] == board[6]:
                            print("%s got 3 in a row!" % wasxoroTurn)
                            gameEnd()
                        if board[0] == board[1] == board[2]:
                            print("%s got 3 in a row!" % wasxoroTurn)
                            gameEnd()

    def rps():
        stillPlaying = "y"
        while stillPlaying == "y":
            user_action = input("Choose (Rock, Paper, Scissors): ").lower()
            actions = ["Rock", "Paper", "Scissors"]
            computer_action = random.choice(actions)
            if user_action == "menu":
                games()
            else:
                print("\nYou chose %s, computer chose %s." %
                      (user_action,     computer_action))
                if user_action == computer_action:
                    print("You tied! Both players chose %s." % computer_action)
                elif user_action == "rock":
                    if computer_action == "Paper":
                        print("You lost! %s beats %s." %
                              (computer_action, user_action))
                    elif computer_action == "Scissors":
                        print("You won! %s beats %s." %
                              (user_action, computer_action))
                elif user_action == "paper":
                    if computer_action == "Rock":
                        print("You won! %s beats %s." %
                              (user_action, computer_action))
                    elif computer_action == "Scissors":
                        print("You lost! %s beats %s." %
                              (computer_action, user_action))
                elif user_action == "scissors":
                    if computer_action == "Paper":
                        print("You won! %s beats %s." %
                              (user_action, computer_action))
                    elif computer_action == "Rock":
                        print("You lost! %s beats %s." %
                              (computer_action, user_action))
                stillPlaying = input("\nPlay Again? (y/n): ")
                if stillPlaying == "n":
                    games()

    def roomQuest():
        bedRoom1 = "YOU"        # Defines room syntax
        bedRoom2 = "   "
        kitchen = "   "
        entrance = "   "
        hallWay = "   "
        mainRoom = "   "
        longHallWay = "   "
        currentRoom = "bedroom1"

        def printBuilding():

            # Function to print the building the player is moving through
            print("|‾‾‾‾‾‾‾‾‾‾‾|     |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|    %s    |     |       %s      |" % (bedRoom1, kitchen))
            print("|____   ____|     |_______   ______|  |‾‾‾‾‾‾‾‾‾|")
            print("     | |                  | |         |   %s   |" % bedRoom2)
            print("|‾‾‾‾   ‾‾‾‾|             | |         |___   ___|")
            print("|    %s    |_____________| |_____________| |______" % entrance)
            print("|                        %s              %s      |" %
                  (hallWay, longHallWay))
            print("|____| |____|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾")
            print("                                 |‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾|")
            print("                                 |                   |")
            print("                                 |        %s        |" % mainRoom)
            print("                                 |                   |")
            print("                                 |___________________|")

        def printBuildingCompact():
            clear()
            print("|‾‾‾‾‾‾‾‾‾‾‾|     |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n|    %s    |     |       %s      |\n|____   ____|     |_______   ______|  |‾‾‾‾‾‾‾‾‾|\n     | |                  | |         |   %s   |\n|‾‾‾‾   ‾‾‾‾|             | |         |___   ___|\n|    %s    |_____________| |_____________| |______\n|                        %s              %s      |\n|____| |____|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾\n                                 |‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾|\n                                 |                   |\n                                 |        %s        |\n                                 |                   |\n                                 |___________________|" % (
                bedRoom1, kitchen, bedRoom2, entrance, hallWay, longHallWay, mainRoom))         # Function to print the building the player is moving through
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
                    clear()
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
                # Moves left from long hall way to hall way.
                elif currentRoom == "longHallWay":
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
            if move == "menu":
                games()

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
                # Moves left from long hall way to hall way.
                elif currentRoom == "longHallWay":
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
            if move == "menu":
                games()

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
                # Moves left from long hall way to hall way.
                elif currentRoom == "longHallWay":
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
            if move == "menu":
                games()

    def numberGuess():
        min = 0
        max = 10
        stillPlaying = "y"
        number = random.randint(min, max)
        while stillPlaying == "y":
            print("The number is between %d and %d. Can you guess it?" %
                  (min, max))
            userChoice = input("Guess: ")
            if userChoice == "menu":
                games()
            elif int(userChoice) == number:
                print("You got it right! The number was %d." % number)
                stillPlaying = input("Play Again? (y/n): ")
                if stillPlaying == "n":
                    quit()
                elif stillPlaying == "y":
                    max += 5
                    number = random.randint(min, max)
            elif userChoice == "":
                print("Please enter a guess and try again.")
            elif int(userChoice) != number:
                print("Nope! The number is not %s. Try Again!" % userChoice)
    game = input(
        "What game do you want to play? (Hangman, Tic Tac Toe, RPS, Room Quest, Number Guess): ").lower()
    if game == "hangman":
        hangMan()
    elif game == "tic tac toe":
        ticTacToe()
    elif game == "rps":
        rps()
    elif game == "room quest":
        roomQuest()
    elif game == "number guess":
        numberGuess()


games()
