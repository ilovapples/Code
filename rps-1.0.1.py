import random
stillPlaying = "y"
while stillPlaying == "y":
    user_action =  input("Choose (Rock, Paper, Scissors): ").lower()
    actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(actions)
    print("\nYou chose %s, computer chose %s." % (user_action,     computer_action))
    if user_action == computer_action:
        print("You tied! Both players chose %s." % computer_action)
    elif user_action == "rock":
        if computer_action == "Paper":
            print("You lost! %s beats %s." % (computer_action, user_action))
        elif computer_action == "Scissors":
            print("You won! %s beats %s." % (user_action, computer_action))
    elif user_action == "paper":
        if computer_action == "Rock":
            print("You won! %s beats %s." % (user_action, computer_action))
        elif computer_action == "Scissors":
            print("You lost! %s beats %s." % (computer_action, user_action))
    elif user_action == "scissors":
        if computer_action == "Paper":
            print("You won! %s beats %s." % (user_action, computer_action))
        elif computer_action == "Rock":
            print("You lost! %s beats %s." % (computer_action, user_action))
    stillPlaying = input("\nPlay Again? (y/n): ")