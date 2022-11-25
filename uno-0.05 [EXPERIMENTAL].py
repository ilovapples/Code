import random               # I AM NOT COMPLETE. I WILL COME BACK!!! MARK MY WORDS!!!!!!!!!!!!!!!!!!!!!!!!!
user1Hand = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
user1HandComputer = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
user1Handindexing = 0
user1HandComputerindexing = 0
user2Hand = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
user2HandComputer = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
user2Handindexing = 0
user2HandComputerindexing = 0
colors = ["Yellow", "Green", "Red", "Blue"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
other = ["Wild Card"]
def randomCard():
    randomColor = random.choice(colors)
    randomNumber = random.choice(numbers)
    return [(randomColor + " " + randomNumber + " Card"), {"color": randomColor, "number": randomNumber}]
def cardDeal(cardCount, user):
    if user == 1:
        user1Handindexing = 0
        user1HandComputerindexing = 0
        user1RandomCard = randomCard()
        for x in range(cardCount): 
            user1Hand[user1Handindexing] = user1RandomCard[0]
            user1HandComputer[user1HandComputerindexing] = user1RandomCard[1]
            user1Handindexing += 1
    elif user == 2:
        user2Handindexing = 0
        user2HandComputerindexing = 0
        use2RandomCard = randomCard()
        for x in range(cardCount):
            user2Hand[user2Handindexing] = user2CardColor + " " + user2CardNumber + " Card"
            user2HandComputer[user2HandComputerindexing] = {"color": user2CardColor, "number": user2CardNumber}
            user2Handindexing += 1
def printHands():
    print(" ________________")
    print("|Player 1 Hand:  |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n" % (user1Hand[0], user1Hand[1], user1Hand[2], user1Hand[3], user1Hand[4], user1Hand[5], user1Hand[6], user1Hand[7], user1Hand[8], user1Hand[9], user1Hand[10], user1Hand[11], user1Hand[12], user1Hand[13], user1Hand[14], user1Hand[15], user1Hand[16], user1Hand[17], user1Hand[18], user1Hand[19], user1Hand[20]))
    print("\n\n ____________________")
    print("|Player 2 Hand:      |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n| %s | %s | %s\n" % (user2Hand[0], user2Hand[1], user2Hand[2], user2Hand[3], user2Hand[4], user2Hand[5], user2Hand[6], user2Hand[7], user2Hand[8], user2Hand[9], user2Hand[10], user2Hand[11], user2Hand[12], user2Hand[13], user2Hand[14], user2Hand[15], user2Hand[16], user2Hand[17], user2Hand[18], user2Hand[19], user2Hand[20]))
cardDeal(7, 1)
cardDeal(7, 2)
printHands()
firstCard = 0
while firstCard < 5:
    firstCard = random.choice()
print("The first card is: %s" % [firstCard])
def turn():
    play = input("Player 1 Play: ").lower()
    if play == user1Hand[0].lower() or play == user1Hand[1].lower():
        print("ok")
turn()