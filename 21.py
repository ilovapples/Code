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
    for i in range(len((house_cards))):
        cardTotal += deck[house_cards[i][1]].index(house_cards[i][0]) + 1
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
    player_Count = int(input("How many people are playing? (Including the house) (Integer 1-10): "))
    for player in range(player_Count):
        giveCard(False, player, 2)

    turn = 1
    currentPlayer = "the House"
    # Start game loop
    while True:
        # if turn%player_Count:
        #     NOT DONE
            
        
        #BUG CATCHER: Makes sure the currentPlayer variable is never equal to "Player 0"
        if currentPlayer == "Player 0":
            currentPlayer = "the House"
        print("It's %s's turn." % currentPlayer)
        move = input("Hit, Stand, or Show? (or help): ").lower()
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
        else:
            print(f"\nInvalid move. You chose {move}, but {move} is not one of hit, stand, show, or help.\n")
            turn -= 1    
        turn += 1
gameLoop()