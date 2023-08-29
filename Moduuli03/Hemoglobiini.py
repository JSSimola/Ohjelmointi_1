gender = str(input("Anna sukupuolesi (mies/nainen): "))

hemoglobin = float(input("Anna hemoglobiiniarvosi: "))

if gender == "mies":
    if hemoglobin < 134:
        print("Hemoglobiiniarvosi on alhainen")
    elif 134 < hemoglobin < 195:
        print("Hemoglobiiniarvosi on normaali")
    elif hemoglobin > 195:
        print("Hemoglobiiniarvosi on korkea")
    else:
        print("Väärä arvo")
elif gender == "nainen":
    if hemoglobin < 117:
        print("Hemoglobiiniarvosi on alhainen")
    elif 117 < hemoglobin < 175:
        print("Hemoglobiiniarvosi on normaali")
    elif hemoglobin > 175:
        print("Hemoglobiiniarvosi on korkea")
    else:
        print("Väärä arvo")
else:
    print("Yritä uudelleen")
