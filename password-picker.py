"""
Password Picker
author: Samke_g2 (Coding Projects in Python)

A program to pick a "random password" using some lists of sorts.
"""
import random
import string

print("Welcome to the Password Picker!")

adjectives = ["sleepy", "slow", "smelly", "wet", "fat",
                "red", "orange", "yellow", "green",
                "blue", "purple", "fluffy", "white", "proud", "brave"
]

nouns = [
            "apple", "dinosaur", "ball", "toaster",
            "toast", "goat", "dragon", "hammer",
            "duck", "panda"
]

while True:
    adjective = random.choice(adjectives)

    noun = random.choice(nouns)

    number = random.randint(0, 100)

    special_char = random.choice(string.punctuation)

    password = adjective + noun +str(number) + special_char
    print(f"Your new password is: {password} ")

    response = input("Would you like another password? (y / n) : ").lower()
    if response == "n":
        break
    else:
        continue
