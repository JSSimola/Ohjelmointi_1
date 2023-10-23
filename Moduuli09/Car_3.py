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

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus



def main():
    auto1 = Auto("ABC-123", 142)
    ajoaika = 1.5
    print(f"{auto1.rekkari:s}, {auto1.huippunopeus:d} km/h, {auto1.nopeus}, {auto1.matka}")
    Auto.kiihdytä(auto1, 60)
    Auto.kulje(auto1, ajoaika)
    print(f"Auton nopeus: {auto1.nopeus} km/h")
    print(f"Ajoaika: {ajoaika}h")
    print(f"Kuljettu matka: {auto1.matka} km")


main()
