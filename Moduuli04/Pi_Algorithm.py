import random

N = int(input("Anna pisteiden lukumäärä: "))
n = 0
repeats = 0
while repeats <= N:
    x = random.random()*2-1
    y = random.random()*2-1
    if (x**2)+(y**2)<=1:
        n = n+1
    repeats = repeats +1

ans_pi = 4*(n/N)
print("Piin likiarvo:")
print(ans_pi)
