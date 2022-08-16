import random

def roll_dice():
    return random.randint(1,6)

def roll_dice_probability(n):
    count = 0
    for i in range(n):
        if roll_dice() == 6:
            count += 1
    return count/n

print(roll_dice_probability(100000))
