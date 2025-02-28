# Number Guesser project                                28/02/2025                                 16:33

# intro the concept of the number guesser
print("Can you guess the whole number, between 1 and 100, that I'm thinking about?")
number = 69

# Start with user input
guess = int(input("What's your guess? "))
print("  ")

# a function that tells the user to guess again

# a function that tells the user that they are right

# A loop that keeps checking if the input is the same as the number

while guess != number:
    
    if guess > number:
        print("That's not it. Guess lower.")
        guess = int(input("Try again: "))
        print("  ")
    elif guess < number:
        print("That's not it. Guess higher.")
        guess = int(input("Try again: "))
        print("  ")
        
print("WELL DONE! YOU GUESSED MY NUMBER :D ")
         

