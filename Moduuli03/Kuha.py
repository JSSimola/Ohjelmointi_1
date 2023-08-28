kuha = float(input("Anna Kuhan pituus:"))

if kuha < 37:
    print("Palauta Kuha vesistöön!")
    margin = 37 - kuha
    print("Alimittaa: " + str(margin) + "cm")
else:
    print("Hyvä saalis!")
