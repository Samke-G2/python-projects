"""
nine_lives.py
author: samke_g2

similar to hangman, but a different implementation
"""
import random

lives = 9

def nineLives():
    words = (
        "Aardvark", "alligator", "ant", "Apple", "Orange", "Banana", "Coconut", "Pineapple",
        "ape", "Life", "loser", "game", "play", "television", "work", "python",
        "hippopotamus", "parrot", "jaguar", "monkey", "awe", "bread", "Winner", "break"
    )

    secret_word = random.choice(words).lower()
    clue = []
    idx = 0

    while idx < len(secret_word):
        clue.append("?")
        idx += 1

    heart = u'\u2764'

    def update_clue(guessed_letter, secret_word, clue):
        index = 0
        while index < len(secret_word):
            if guessed_letter == secret_word[index]:
                clue[index] = guessed_letter
            index += 1

    while lives > 0:
        print(clue)
        print("Lives left: " + heart * lives)
        guess = input("Guess a letter or the whole word. >").lower()

        if len(guess) > 1:
            if guess == secret_word:
                break
            else:
                print("Incorrect, you lost a life.")
                lives -= 1
        else:
            if guess in secret_word:
                update_clue(guess, secret_word, clue)
                # for i in secret_word:                 tried to refine the code and update the clue using index, will try it in another iteration
                #     if guess == i:
                #         clue[index(i)] == guess
                    # else:
                    #     lives-=1
            else:
                print("Incorrect, you lost a life.")
                lives -= 1

nineLives()

if lives > 0:
    print("\nYou won! The secret word was: {}".format(secret_word))
else:
    print("\nYou lost! The secret word was: {}".format(secret_word))
