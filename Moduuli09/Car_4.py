import random

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
    race_cars = []
    for i in range(1, 11):
        new_car = Auto(f"ABC-{i}", random.randint(100,200))
        race_cars.append(new_car)
    while True:
        for i in race_cars:
            if i.matka <= 10000:
                print(i.rekkari)
                i.kiihdytä(random.randint(-10,15))
                print(i.nopeus)
                i.kulje(1)
                print(i.matka)
                print("----------")
            else:
                break










main()
