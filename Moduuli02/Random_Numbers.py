import random

# Ei saa nollaa ekaksi luvuksi :(
#def digitgen(n):
#    min = 10 ** (n-1)
#   max = 10 ** n-1
#    return random.randint(min, max)

def digitgen1(n_1):
    numbers = "0123456789"
    code = ""
    for i in range(0,n_1):
        code+= random.choice(numbers)
    return code

def digitgen2(n_2):
    numbers = "123456"
    code = ""
    for i in range(0,n_2):
        code+= random.choice(numbers)
    return code

print("Kolmen numeron koodi:")
print(digitgen1(3))
print("Neljän numeron koodi:")
print(digitgen2(4))
