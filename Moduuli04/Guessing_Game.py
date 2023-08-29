import random

x = random.randint(1,10)

while True:
    user_input = int(input("Arvaa luku välillä 1-10: "))
    if user_input == x:
        break
    elif user_input < x:
        print("Liian pieni arvaus")
    elif user_input > x:
        print("Liian suuri arvaus")

print("Oikein")

