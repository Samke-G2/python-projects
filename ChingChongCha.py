# Rock, Paper, Scissors (AKA "Ching Chong Cha", from obscure childhood memories ig)                     28/02/2025                      17:26

# User input from the first user ( the computer, ideally)
computer = "Rock"

# User input from teh second user (person playing the game vs computer)
player_1 = input("What's your choice?: ")

# counters for the second part (best out of three)
xerCount = 0
yerCount = 0

# if statements that compare the choices (in a function, we know from 'calculator' that free-standing if satements don't really work well)
# OR I could assign the possible numbers some number values and compare those (dunno how, just seems like it would be interesting to do)

# Nine possible outcomes, i think
def game1(xer, yer, xerCount, yerCount):
    if xer == yer:
        print("It's a tie.")
        player_1 = input("What's your choice?: ")
        game2(computer, player_1, xerCount, yerCount)
    elif  xer == "Paper" and yer == "Rock":
        print(f"{xer} wins! ")
        xerCount += 1
    elif xer == "Paper" and yer == "Scissors":
        print(f"{yer} wins! ")
        yerCount += 1
    elif xer == "Rock" and yer == "Paper":
        print(f"{yer} wins! ")
        yerCount += 1
    elif xer == "Rock" and yer == "Scissors":
        print(f"{xer} wins! ")
        xerCount += 1
    elif xer == "Scissors" and yer == "Paper":
        print(f"{xer} wins! ")
        xerCount += 1
    elif xer == "Scissors" and yer == "Rock":
        print(f"{yer} wins! ")
        yerCount += 1
        
def game2(xer, yer, xerCount, yerCount):
    if xer == yer:
        print("It's a tie.")
        player_1 = input("What's your choice?: ")
        game1(computer, player_1, xerCount, yerCount)
    elif  xer == "Paper" and yer == "Rock":
        print(f"{xer} wins! ")
        xerCount += 1
    elif xer == "Paper" and yer == "Scissors":
        print(f"{yer} wins! ")
        yerCount += 1
    elif xer == "Rock" and yer == "Paper":
        print(f"{yer} wins! ")
        yerCount += 1
    elif xer == "Rock" and yer == "Scissors":
        print(f"{xer} wins! ")
        xerCount += 1
    elif xer == "Scissors" and yer == "Paper":
        print(f"{xer} wins! ")
        xerCount += 1
    elif xer == "Scissors" and yer == "Rock":
        print(f"{yer} wins! ")
        yerCount += 1


# run the if-statement function with the input value(s)
game2(computer, player_1, xerCount, yerCount)

# After i've created this one, maybe create a best-out-of-three version??

# The best-out-of-three versiion uses some counters and a while loop


# while xerCount + yerCount < 3 :
#     game2(computer, player_1, xerCount, yerCount)




def best3(xer, yer):
    xCount = 0
    yCount = 0
    
    while xCount+yCount < 3:
        if xer == yer:
            print("It's a tie.")
            player_1 = input("What's your choice?: ")
            game1(computer, player_1, xerCount, yerCount)
        elif  xer == "Paper" and yer == "Rock":
            print(f"{xer} wins! ")
            xerCount += 1
        elif xer == "Paper" and yer == "Scissors":
            print(f"{yer} wins! ")
            yerCount += 1
        elif xer == "Rock" and yer == "Paper":
            print(f"{yer} wins! ")
            yerCount += 1
        elif xer == "Rock" and yer == "Scissors":
            print(f"{xer} wins! ")
            xerCount += 1
        elif xer == "Scissors" and yer == "Paper":
            print(f"{xer} wins! ")
            xerCount += 1
        elif xer == "Scissors" and yer == "Rock":
            print(f"{yer} wins! ")
            yerCount += 1
