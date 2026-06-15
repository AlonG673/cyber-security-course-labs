# -------------------------------------------------------------------
# Script Name:  shellgame.py
# Description:  A classic "Cups and Ball" guessing game built in Python.
# Date:         June 2026
# -------------------------------------------------------------------
import random
cup_list = [" ", "X", " "]
player1_score = 0
computer_score = 0
print ("welcome to the Shell Game\nright now the X is in the middle cup")
print (cup_list)

def list_shuffle():
    random.shuffle(cup_list)
    return cup_list

def player_guess():
    guess = ""
    while guess not in ["0","1","2"]:
        print ("pick one of the three cups\nright-0 middle-1 left-2")
        guess = input("your guess: ")
    return int(guess)

def check_guess(cup_list, guess):
    if cup_list[guess] == "X":
        return "player"
    else:
        return "computer"


start_game = "y"
while True:
    if start_game == "y":
        mixed_cup = list_shuffle()
        cup_guess = player_guess()
        winner = check_guess(mixed_cup, cup_guess)
        print (cup_list)
        if winner == "player":
            print("you won")
            player1_score += 1
        else:
            print("wrong guess")
            computer_score += 1
        print("player score: ", player1_score, "computer score: ", computer_score)

        start_game= (input("do yo want to continue playing? y/n : "))

    else:
        print ("thank you for playing here is the final scores")
        print("player score: ", player1_score, "computer score: ", computer_score)
        break
