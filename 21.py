import random

# List of every possible card in the game
suites = ["Hearts ♥", "Clubs ♣", "Diamonds ♦", "Spades ♠"]
deck = {
    "Hearts ♥": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
    "Clubs ♣": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
    "Diamonds ♦": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
    "Spades ♠": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
}

house_cards = []
player_cards = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
def giveCard(house_or_not: bool, player: int, cardCount: int):
    if house_or_not:
        for _ in range(cardCount):
            suite = random.choice(suites)
            card = random.choice(deck[suite])
            house_cards.append([card, suite])
    else:
        if player < 1 or player > 10:
            print("\nInvalid player.\n")
        else:
            for _ in range(cardCount):
                suite = random.choice(suites)
                card = random.choice(deck[suite])
                player_cards[player - 1].append([card, suite])
def printHouseCards():
    cardTotal = 0
    index = 0
    for _ in range(len((house_cards))):
        cardTotal += deck[house_cards[index][1]].index(house_cards[index][0]) + 1
        index += 1
    # Print the houses cards
    print("\n___________________")
    print("| House's Cards   |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("Card Total: %d\n\n" % cardTotal)
    cardNum = 0
    for _ in range(len(house_cards)):
        print(str(cardNum+1) + ": " + house_cards[cardNum] + "\n")
        cardNum += 1
    print("\n")
def printPlayerCards(player: int):
    # Print the given players cards
    if player < 1 or player > 10:
        print("\nInvalid player.\n")
    else:
        print("\n___________________" + "_" * len(str(player)))
        print("| Player %d's Cards |" % player)
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾" + "‾" * len(str(player)))
        cardNum = 0
        for _ in range(len(player_cards[player-1])):
            print(str(cardNum+1) + ": " + player_cards[player-1][cardNum] + "\n")
            cardNum += 1
        print("\n")
def gameLoop():
    # Give cards to each player
    giveCard(True, 0, 2)
    player_Count = int(input("How many people are playing? (Integer 1-10): "))
    playerToBeGivenCards = 0
    for _ in range(player_Count):
        giveCard(False, playerToBeGivenCards, 2)
        playerToBeGivenCards += 1
        
    turn = 1
    currentPlayer = "the House"
    totalPlayers = player_Count + 1
    # Start game loop
    while True:
        if turn%totalPlayers == 1:
            currentPlayer = "the House"
        if turn%totalPlayers == 0:
            currentPlayer = "Player " + str(totalPlayers)
        else:
            currentPlayer = "Player " + str(turn - 1)
        
        print("It's %s's turn." % currentPlayer)
        move = input("Hit or Stand? (or help): ").lower()
        if move == "help":
            print("\nCommands are: \nhelp, to open this help menu\nshow, to show your cards and card total\n")
        elif move == "show":
            if currentPlayer == "the House":
                printHouseCards()
            else:
                printPlayerCards(int(currentPlayer[-1]))
        elif move == "hit":
            if currentPlayer == "the House":
                giveCard(True, 0, 1)
            else:
                giveCard(False, int(currentPlayer[-1]), 1)
        elif move == "stand":
            continue
        
        turn += 1
gameLoop()