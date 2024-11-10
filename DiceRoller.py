import random as rd

#(feel free to take the ASCII art of the die faces; I don't care what you use them for, they're die faces.)

die_side1 = """
+-------+
|       |
|   o   |
|       |
+-------+ 
"""

die_side2 = """
+-------+
| o     |   
|       |
|     o |
+-------+
"""

die_side3 = """
+-------+
| o     |
|   o   |
|     o |
+-------+
"""

die_side4 = """
+-------+
| o   o |
|       |
| o   o |
+-------+
"""

die_side5 = """
+-------+
| o   o | 
|   o   |
| o   o |
+-------+
"""

die_side6 = """
+-------+
| o   o |
| o   o |
| o   o |
+-------+
"""

dice = [die_side1, die_side2, die_side3, die_side4, die_side5, die_side6] # Dice values list

die_value = {
    die_side1: 1,
    die_side2: 2,
    die_side3: 3,
    die_side4: 4,
    die_side5: 5,
    die_side6: 6,
} # Dictionary of the corresponding values

die_roll = rd.choice(dice) # Randomly take a die face from the list above

print(f"{die_roll}\nYou rolled a {die_value[die_roll]}") # Prints the die faces as well as the values