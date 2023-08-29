year = int(input("Anna vuosiluku: "))

if (year % 4 == 0 and year % 100 != 0):
    print("Vuosi on karkausvuosi")
elif (year % 100 == 0 and year % 400 == 0 and year % 4 == 0):
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")