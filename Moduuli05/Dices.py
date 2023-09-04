import random

list = []

n_dice = int(input("Anna noppien lukumäärä: "))

for i in range(0,n_dice):
    dice_roll = random.randint(1,6)
    list.append(dice_roll)

answer = sum(list)

print(answer)