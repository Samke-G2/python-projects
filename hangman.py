# Hangman Project                               # 03/05/2025                                    17:21
from wordlist import words
import random


# First, I'll have a word


# Next, I'll have user input guessing that word


# Then a function to check if the user's word is my word
# If not, the function asks the user to guess a letter in my word, then checks if the letter is present.
# If the letter is present, the program will say so and show the position of the letter
# If not it will increment a count,
# when the count reaches 6 the user will lose the game and the word will be displayed



# solution


# Dictionary of key(number) and value(tuple):
hangman_art = {
    0: (" ___  ",
        "|   | ",
        "|   ",
        "|   ",
        "|   "),
    
    1: (" ___  ",
        "|   O  ",
        "|    ",
        "|    ",
        "|       "),
    
    2: (" ___  ",
        "|   O  ",
        "|   |  ",
        "|    ",
        "|       "),
    
    3: (" ___  ",
        "|   O  ",
        "|  /|  ",
        "|    ",
        "|       "),
    
    4: (" ___  ",
        "|   O  ",
        "|  /|\\  ",     # A single backslash \ in a string is an escape senquence out of the string. so to literally print a backlash, we put 2 of them
        "|    ",
        "|       "),
    
    5: (" ___  ",
        "|   O  ",
        "|  /|\\  ",
        "|  /   ",
        "|       "),
    
    6: (" ___  ",
        "|   O  ",
        "|  /|\\  ",
        "|  / \\  ",
        "|       ")
    
}

def display_hangman(guesses):
    for line in hangman_art[guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)
    x_guesses = 0
    guessed_letters = set()
    
    while True:
        display_hangman(x_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
            
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess: 
                    hint[i] = guess
        else:
            x_guesses += 1
            
        if "_" not in hint:
            display_hangman(x_guesses)
            display_answer(answer)
            print("YOU WIN!!!")
            break
        elif x_guesses >= len(hangman_art) - 1:
            display_hangman(x_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            break
            
            

if __name__ == "__main__":
    main()