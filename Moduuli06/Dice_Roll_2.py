import random

dice_sides = int(input("Anna nopan tahkojen lukumäärä: "))

def dice_roll(dice_sides):
    num = random.randint(1, dice_sides)
    return num

flag = True

while flag == True:
    roll = dice_roll(dice_sides)
    if roll == dice_sides:
        print(roll)
        flag = False
    else:
        print(roll)
