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
    goal_reached = True
    while goal_reached == True:
        for i in race_cars:
            i.kiihdytä(random.randint(-10,15))
            i.kulje(1)
            if i.matka >= 10000:
                goal_reached = False
                break
    print("Rekisterinumero, Huippunopeus, Nopeus, Kuljettu matka")
    for i in race_cars:
        print(f"{i.rekkari}, {i.huippunopeus}km/h, {i.nopeus}km/h, {i.matka}km")

main()
