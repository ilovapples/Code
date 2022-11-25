import os
def clear():
    os.system('cls')
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
letter = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
correctLetters = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
wrongLetters = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
def printHangMan():
    clear()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWrong Letters:       /¯¯¯¯¯¯\\")
    print(" %s %s %s %s             |      |" % (wrongLetters[0], wrongLetters[1], wrongLetters[2], wrongLetters[3]))
    print(" %s %s %s %s             %s      |" % (wrongLetters[4], wrongLetters[5], wrongLetters[6], wrongLetters[7], head))
    print(" %s %s %s %s            %s%s%s     |" % (wrongLetters[8], wrongLetters[9], wrongLetters[10], wrongLetters[11], leftArm, torso, rightArm))
    print(" %s %s %s %s            %s %s   __/__" % (wrongLetters[12], wrongLetters[13], wrongLetters[14], wrongLetters[15], leftLeg, rightLeg))
    print("\n           %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (letter[0], letter[1], letter[2], letter[3], letter[4], letter[5], letter[6], letter[7], letter[8], letter[9], letter[10], letter[11], letter[12], letter[13], letter[14], letter[15], letter[16], letter[17]))
for i in range(len(word)):
    letter[letterNumber] = "_"
    correctLetters[letterNumber] = word.lower()[letterNumber]
    letterNumber += 1
printHangMan()
while stillPlaying == "y":
    letterGuess = input("Guess a letter: ")
    letterGuess = letterGuess.lower()
    if letterGuess == "reset":
        letter = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        wrongLetters = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        correctLetters = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        word = input("\nWord (Hide this!): ")
        for i in range(len(word)):
            letter[letterNumber] = "_"
            correctLetters[letterNumber] = word.lower()[letterNumber]
            letterNumber += 1
        printHangMan()
    else:
        if letterGuess not in word:                                     # Overly simple code to create the "Hang Man" if the letter isn't in the word.
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
        elif letterGuess in word:                                   # Overly complicated code to check if a letter is in the string.
            print("The letter %s is in the word!" % letterGuess)
            wordIndexing = word.index(letterGuess)
            for x in range(word.count(letterGuess)):
                letter[word.index(letterGuess, (wordIndexing))] = letterGuess
                wordIndexing += 1
                checkForLetterGuess = word.find(letterGuess, wordIndexing)
                if checkForLetterGuess < 0:
                    break
                elif checkForLetterGuess > -1:
                    letter[word.find(letterGuess, (wordIndexing))] = letterGuess
            printHangMan()
        if correctLetters == letter:            # Ends the game
            print("You won Hang Man! The word was %s." % word)
            quit()