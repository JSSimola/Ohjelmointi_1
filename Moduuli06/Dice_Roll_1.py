import random
def dice_roll():
    num = random.randint(1, 6)
    return num

flag = True

while flag == True:
    roll = dice_roll()
    if roll == 6:
        print(roll)
        flag = False
    else:
        print(roll)
