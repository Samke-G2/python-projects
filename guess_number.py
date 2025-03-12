# Number Guesser project                                28/02/2025                                 16:33
import random

# intro the concept of the number guesser
print(" ")
print("Can you guess the whole number, between 1 and 100, that I'm thinking about?")
number = random.randint(1, 100)

tries = 0

while True:
    try:
        # Start with user input
        guess = int(input("What's your guess? "))
        print(" ")
        
        # While loop displays as long as the number is incorrect
            
        if guess > number:
            print("That's not it. Guess lower.")
            print("  ")
            tries += 1
        elif guess < number:
            print("That's not it. Guess higher.")
            print("  ")
            tries += 1
        else:
            # print statement for when number is correct        
            print("WELL DONE! YOU GUESSED MY NUMBER :D ")
            tries += 1
            break   
    except ValueError:
        print("Please enter a valid number")
        
print(f"It only took you {tries} tries.")
