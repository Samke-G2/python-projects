# Rock, Paper, Scissors (AKA "Ching Chong Cha", from obscure childhood memories ig)                     28/02/2025                      17:26

# User input from teh first user ( the computer, ideally)
computer = "Rock"

# User input from teh second user (person playing the game vs computer)
player_1 = input("What's your choice?: ")

# if statements that compare the choices (in a function, we know from 'calculator' that free-standing if satements don't really work well)
# OR I could assign the possible numbers some number values and compare those (dunno how, just seems like it would be interesting to do)

# Nine possible outcomes, i think
def game(xer, yer):
    if xer == yer:
        print("It's a tie.")
        # Then another function for repeating, maybe
    elif  xer == "Paper" and yer == "Rock":
        print(f"{xer} wins! ")
    elif xer == "Paper" and yer == "Scissors":a



# After i've created this one, maybe create a best-out-of-three version??




