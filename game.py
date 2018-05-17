# coding: utf-8

from random import randint, choice
from time import sleep
import sys


# list with the 3 otpions
options_play = ["rock", "paper", "scissors"]

# Computer will choose one option from the list
computer = choice(options_play).lower()

player = True

while True:

    player = input("Please choose: rock, paper or scissors \nIf you want to stop playing, choose: break $ ")
    player = player.lower()


    if player in options_play:
        print('\n')
        print("You have chosen {0} and the other player has chosen {1}".format(player, computer))

        print("Computing")
        for i in range(3):

            print(".")
            sys.stdout.flush()
            sleep(1)

    elif player == "break":
        for word in 'Bye!':
            sys.stdout.write(word)
            sys.stdout.flush()
            sleep(0.5)
        sys.stdout.write('\n')
        sys.stdout.flush()
        print(u"\u2661")
        break

    else:
        print("Sorry, we cannot play with this input!")

        player = input("Please choose: rock, paper or scissors $ ")

    if player == computer:
        print("Tie!")
        #print("*****")

    elif (player == "rock" and computer == "paper") or (player == "Paper" and computer == "Scissors") or (player == "Scissors" and computer == "Rock"):
        
        print("You lose! :(")
        #print("*****")

    else:
        print("You win! :) ")
        #print("*****")

    print("*****")   
    
    computer = choice(options_play).lower()