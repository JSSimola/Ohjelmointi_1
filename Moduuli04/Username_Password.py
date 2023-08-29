n = 0

while n < 5:
    username = input("Username: ")
    password = input("Password: ")
    if username == "python" and password == "rules":
        print("Tervetuloa")
        break
    else:
        n = n+1
        print("Pääsy evätty")
