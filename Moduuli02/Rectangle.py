base = float(input("Anna suorakulmion kanta metreinä: "))
height = float(input("Anna suorakulmion korkeus metreinä: "))
radius = (base * 2) + (height * 2)
area = base * height
print(f"Suorakulmiosi piiri on: {radius:6.1f} m^2")
print(f"Suorakulmiosi pinta-ala on: {area:6.1f} m^2")