from random import randint

def roll(dice, sides):

    rolls = []
    total = 0

    for roll in range(1, dice+1):
        result = randint(1, sides)
        rolls.append(result)
        total += result

    return rolls, total