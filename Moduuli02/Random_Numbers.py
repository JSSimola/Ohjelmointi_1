import random

# 3 numeroinen koodi

def digitgen(n):
    min = 10 ** (n-1)
    max = 10 ** n-1
    return random.randint(min, max)

def digitgen2(n_2):
    numbers = "0123456"
    code = ""
    for _ in range(0,n_2):
        code+= random.choice(numbers)
    return code

print("Kolmen numeron koodi:")
print(digitgen(3))
print("Neljän numeron koodi:")
print(digitgen2(4))

