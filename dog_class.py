"""
Project name: Dog clauses
author: Samke_g2 and chatGPT

This program was created when I asked chatGPT to explain to me what classes were and it gave me an example with this dog class.
After that, it challenged me to extend the class by adding the "eat" method with some specifications.

The specifications were:
1) The method should take one parameter: food (a string).
2) If the dog eats "treat":
    - Increase energy by 5.
    - Print: "Milo loved the treat! Energy is now 105." (or whatever the new energy is).

3) If the dog eats "dog food":
    - Inccrease the energy by 10
    - Print: "Milo ate dog food. Energy is now 110."

4) If it's anything else:
    Print: "Milo didn't like that."

5) Cap the energy at 100 — it can't go higher.

Bonus(optional)
- Reject food if energy is already 100, and print: "Milo is full and doesn't want to eat right now."
"""

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = 100  # starts fully energized

    def bark(self):
        print(f"{self.name} says: Woof!")

    def sleep(self, hours):
        self.energy += hours * 10
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} slept for {hours} hours and now has {self.energy} energy.")

    def play(self, minutes):
        energy_used = minutes * 2
        if self.energy >= energy_used:
            self.energy -= energy_used
            print(f"{self.name} played for {minutes} minutes. Energy is now {self.energy}.")
        else:
            print(f"{self.name} is too tired to play. Try letting them sleep.")

    def eat(self, food):        # I added this method to the class
        food = food.lower()
        if self.energy >= 100:
            print(f"{self.name} is full and doesn't want to eat right now.")
        else:
            if food == "treat":
                self.energy += 5
                if self.energy > 100:
                    self.energy = 100
                print(f"{self.name} loved the treat! Energy is now {self.energy}.")
            elif food == "dog food":
                self.energy += 10
                if self.energy > 100:
                    self.energy = 100
                print(f"{self.name} ate dog food. Energy is now {self.energy}.")
            else:
                print(f"{self.name} didn't like that.")

        # chatGPT suggested I cap the energy at 100 like so: (apparently it's a more elegant method as it avoids repeating code)
        # if food == "treat":
        #     self.energy = min(self.energy + 5, 100)
        #     print(f"{self.name} loved the treat! Energy is now {self.energy}.")
        # elif food == "dog food":
        #     self.energy = min(self.energy + 10, 100)
        #     print(f"{self.name} ate dog food. Energy is now {self.energy}.")
