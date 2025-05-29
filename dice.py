"""
Write a program to simulate the throw of two dice (each between 1 and 6).
Print the numbers representing the two throws:
    ● If the numbers on the two dice are not equal, t
    he player’s score is thesum of the numbers thrown. 
    Print the score.
        ● If the numbers on the two dice are equal, 
        the player scores twice thesum of the number thrown. 
        
        Print “You threw a double”, and the score.
"""
"""
WELCOME to the dice throwing game:

throw the two dices
dice 1 
dice 2
if dice 1 != dice 2 
    sum = dice 1 + dice 2
    print("Your Score is: ", sum)
else
    sum = 2 * (dice 1 + dice 2)
    print("You threw a double: ", ":)", sum )
"""

import random

print("WELCOME TO THE DICE THROWING GAME \n")

x = input ("Press enter to throw the two dices\n")

dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)

print("Dice_1: ", dice_1)
print("Dice_2: ", dice_2)
print("")


if dice_1 != dice_2:
    Score = dice_1 + dice_2
    print("Your Score is: ", Score,)
    print("")

else :
    Score = 2 * (dice_1 + dice_2)
    print("You threw a double: ", Score,":)" )
    print("")




