import random

options = ("rock","paper","scissors")
play = True


while play:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock,paper,scissors) : ")

 
    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer :
        print("It is a tie")
    elif player == "rock" and computer == "scissors":
        print("You won")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")
    ask = input("Do you want to play again? (Y/N) : ").upper()
    if ask!= "Y":
        play = False
    else: 
        continue
    print("Thank you for playing")