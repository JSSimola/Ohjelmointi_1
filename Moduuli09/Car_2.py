class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus = 0, matka = 0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


def main():
    auto1 = Auto("ABC-123", 142)
    print(f"{auto1.rekkari:s}, {auto1.huippunopeus:d} km/h, {auto1.nopeus}, {auto1.matka}")
    Auto.kiihdytä(auto1, 30)
    Auto.kiihdytä(auto1, 70)
    Auto.kiihdytä(auto1, 50)
    print(f"{auto1.nopeus} km/h")
    Auto.kiihdytä(auto1, -200)
    print(f"{auto1.nopeus} km/h")

main()
