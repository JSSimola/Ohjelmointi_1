month = int(input("Anna kuukauden numero: "))

season = ("kevät", "kesä", "syksy", "talvi")

if (month == 12 or 1 <= month <= 2):
    print(season[3])
elif (3 <= month <= 5):
    print(season[0])
elif (6 <= month <= 8):
    print(season[1])
elif (9 <= month <= 11):
    print(season[2])
else:
    print("virheellinen syöte")
