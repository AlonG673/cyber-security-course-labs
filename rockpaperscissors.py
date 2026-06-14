# Class project 1– “Rock, Paper, Scissors”
import random

player1_score = 0
player2_score = 0
computer_score = 0
print("welcome to the game Rock, Paper, Scissors")


def player():
    print("for paper press 1")
    print("for scissors press 2")
    print("for rock press 3")
    while True:
        try:
            b = int(input("enter your choice: "))
            if b == 1 or b == 2 or b == 3:
                return b
            else:
                print("enter valid choice")
        except ValueError:
            print("invalid input! Please enter a number (1, 2, or 3).")

while True:
    print("choose your opponent")
    print("press 1 to play against the Computer\npress 2 to play against Player2")
    a = input("enter your choice: ")
    if a == "1" or a == "2":
        break
    else:
        print("invalid input, choose your opponent")

while True:
    print("\nnew round begin")

    if a == "1":
        print("playing against computer...")
        b = player()
        computer = random.randint(1, 3)
        if ( b == 1 and computer == 3 or b == 2 and computer == 1 or b == 3 and computer == 2 ):
            print("you win")
            player1_score += 1
        elif ( b == 1 and computer == 1 or b == 2 and computer == 2 or b == 3 and computer == 3 ):
            print("a tie")
        else:
            print("you lose")
            computer_score += 1
        print (f"player score: {player1_score}, computer score: {computer_score}")

    elif a == "2":
        print("playing against Player2...")
        print("Player 1 turn:")
        p1_choice = player()
        print("Player 2 turn:")
        p2_choice = player()
        if ( p1_choice == 1 and p2_choice == 3 or p1_choice == 2 and p2_choice == 1 or p1_choice == 3 and p2_choice == 2 ):
            print("player 1 win")
            player1_score += 1
        elif ( p1_choice == 1 and p2_choice == 1 or p1_choice == 2 and p2_choice == 2 or p1_choice == 3 and p2_choice == 3 ):
            print("a tie")
        else:
            print("player 2 win")
            player2_score += 1
        print( f"player 1 score: {player1_score}, player 2 score: {player2_score}")

    print("\nWhat would you like to do next?")
    print("press 1 to play another round")
    print("press 2 to change opponent (resets scores)")
    print("press 3 to quit")
    next_step = input("enter your choice: ")

    if next_step == "3":
        print("Thanks for playing!")
        break

    elif next_step == "2":
        player1_score = 0
        player2_score = 0
        computer_score = 0

        while True:
            print("\nchoose your new opponent")
            print("press 1 to play against the Computer\npress 2 to play against Player2")
            a = input("enter your choice: ")
            if a == "1" or a == "2":
                break
            else:
                print("invalid input, choose your opponent")