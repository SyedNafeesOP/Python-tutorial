# Dice Rolling Simulator: Write a program that simulates rolling dice. Allow the user to input the number of dice and the number of sides on each die, then roll them and display the results.

import random
while True:
    Turn=random.randint(1,6)
    print(Turn)
    Turn1=input("want to roll the dice again (quit/play)")
    if Turn1=="play":
        continue
    else:
       break

# another
import random

while True:
    num_dice = int(input("Enter the number of dice: "))
    num_sides = int(input("Enter the number of sides on each die: "))

    for _ in range(num_dice):
        result = random.randint(1, num_sides)
        print("Result:", result)

    play_again = input("Want to roll the dice again? (yes/no): ")
    if play_again.lower() != "yes":
        break

