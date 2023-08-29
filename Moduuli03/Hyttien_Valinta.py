
valinta = input("Valitse LUX, A, B tai C:\n ")
if valinta == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif valinta == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif valinta == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif valinta == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

