# Rock, Paper, Scissors (AKA "Ching Chong Cha", from obscure childhood memories ig)                     28/02/2025                      17:26
import random

# User input from the first user ( the computer, ideally)
options = ("rock", "paper", "scissors")
# computer = random.choice(options)

# User input from teh second user (person playing the game vs computer)
# player = None
# while player not in options:
#     player = input("What's your choice?: ").lower()

# counters for the second part (best out of three)
xerCount = 0
yerCount = 0

# if statements that compare the choices (in a function, we know from 'calculator' that free-standing if satements don't really work well)
# OR I could assign the possible numbers some number values and compare those (dunno how, just seems like it would be interesting to do)

# Nine possible outcomes, i think
def game1():

    playing = True
    while playing: 
        xer = None
        while xer not in options:
            xer = input("What's your choice?: ").lower()
        yer = random.choice(options)
        print(" ")
        print(f"Player: {xer}")
        print(f"Computer: {yer}")
        print(" ")
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
            
        play_again = input("Play again? (y/n): ").lower()
        print(" ")
        if not play_again == "y":
            playing = False
    print("Thanks for playing! ")


# run the if-statement function with the input value(s)
game1()

# After i've created this one, maybe create a best-out-of-three version??

# The best-out-of-three versiion uses some counters and a while loop
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


# print("ROCK, PAPER, SCISSORS - BEST OUT OF THREE")
# print(" ")
# game2(3)

