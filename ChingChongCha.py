# Rock, Paper, Scissors (AKA "Ching Chong Cha", from obscure childhood memories ig)                     28/02/2025                      17:26
import random

# Options from the computer and user to choose from
options = ("rock", "paper", "scissors")

# if statements that compare the choices (in a function, we know from 'calculator' that free-standing if satements don't really work well)
# Nine possible outcomes, 3 are a tie (one line for those), 3 are wins (seperate wins), the rest can just be grouped as losses
def game1():

    playing = True
    
    while playing:
        # Player input, checking it to see if it's valid
        xer = None
        while xer not in options:
            xer = input("What's your choice?: ").lower()
        # computer chooses, a random valid choice
        yer = random.choice(options)
        # printing both choices
        print(" ")
        print(f"Player: {xer}")
        print(f"Computer: {yer}")
        print(" ")
        # comparing the choices to determine winner automatically
        if xer == yer:
            print("It's a tie.")
            print(f"You and the computer both chose {xer}.")
            print(" ")
        elif  xer == "paper" and yer == "rock":
            print(f"You win with {xer} ")
            print(" ")
        elif xer == "rock" and yer == "scissors":
            print(f"You win with {xer}")
            print(" ")
        elif xer == "scissors" and yer == "paper":
            print(f"You win with {xer}")
            print(" ")
        else:
            print("You lose")
            print(" ")
        # Play again option to repeat games as many times as I want
        play_again = input("Play again? (y/n): ").lower()
        print(" ")
        if not play_again == "y":
            playing = False
    # End-of-game message
    print("Thanks for playing! ")
    print(" ")


# run the game to see if it works
print("ROCK, PAPER, SCISSORS! (with optional repeats)")
print(" ")
game1()

# After i've created this one, maybe create a best-out-of-three version??..... I DID!!!

# The best-out-of-whatever version uses some counters and a while loop
def game2(n):
    xCount = 0
    yCount = 0
    winner = n/2
    
    while xCount < winner and yCount < winner :
        yer = random.choice(options)
        xer = input("What's your choice?: ").lower()
        while xer not in options:
            xer = input("What's your choice?: ").lower()
        print(f"Player: {xer}")
        print(f"Computer: {yer}")
        
        if xer == yer:
            print("It's a tie.")
            print(f"You and the computer both chose {xer}.")
            print(" ")
        elif  xer == "paper" and yer == "rock":
            print(f"You win with {xer} ")
            print(" ")
            xCount += 1 
        elif xer == "rock" and yer == "scissors":
            print(f"You win with {xer}")
            print(" ")
            xCount += 1
        elif xer == "scissors" and yer == "paper":
            print(f"You win with {xer}")
            print(" ")
            xCount += 1
        else:
            print("You lose")
            print(" ")
            yCount += 1
               
    print(f"Player won {xCount} and Computer won {yCount}")
    print("Thanks for playing! ")


# first as player how many possible rounds the want
n = int(input("ROCK, PAPER, SCISSORS - BEST OUT OF? "))
print(" ")
# then run the game
game2(n)
