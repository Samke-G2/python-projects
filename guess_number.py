# Number Guesser project                                28/02/2025                                 16:33

# intro the concept of the number guesser
print("Can you guess the whole number, between 1 and 100, that I'm thinking about?")
number = 69

# Start with user input
guess = int(input("What's your guess? "))
print("  ")

# While loop displays as long as the number is incorrect
while guess != number:
    
    if guess > number:
        print("That's not it. Guess lower.")
        guess = int(input("Try again: "))
        print("  ")
    elif guess < number:
        print("That's not it. Guess higher.")
        guess = int(input("Try again: "))
        print("  ")
        
# print statement for when number is correct        
print("WELL DONE! YOU GUESSED MY NUMBER :D ")
