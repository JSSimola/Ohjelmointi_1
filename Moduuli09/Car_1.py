class Auto:
    nopeus = 0
    matka = 0

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus

def main():
    auto1 = Auto("ABC-123", 142)
    print(f"{auto1.rekkari:s}, {auto1.huippunopeus:d} km/h, {auto1.nopeus}, {auto1.matka}")

main()
