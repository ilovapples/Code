import random
min = 0
max = 10
stillPlaying = "y"
number = random.randint(min, max)
while stillPlaying == "y":
    print("The number is between %d and %d. Can you guess it?" % (min, max))
    userChoice = input("Guess: ")
    if int(userChoice) == number:
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