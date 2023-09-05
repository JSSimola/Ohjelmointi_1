user_int = int(input("Anna kokonaisluku: "))

flag_prime = False

if user_int > 1:
    for i in range(2,user_int):
        if user_int % i == 0:
            flag_prime = True
else:
    print("1 on alkuluku")
    quit()

if flag_prime == True:
    print("Luku ei alkuluku")
else:
    print("Luku on alkuluku")
