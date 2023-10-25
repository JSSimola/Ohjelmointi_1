import random

class Car:
    def __init__(self, registry, top_speed, current_speed = 0, distance = 0):
        self.registry = registry
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, muutos):
        self.current_speed = self.current_speed + muutos
        if self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance += hours * self.current_speed

class Race:
    def __init__(self, name, length_km, participants):
        self.name = name
        self.length_km = length_km
        self.participants = participants

    def an_hour_passes(self):
        for i in self.participants:
            i.accelerate(random.randint(-10, 15))
            i.drive(1)

    def print_situation(self):
        print("Registry, Top Speed, Current Speed, Distance Traveled")
        for i in self.participants:
            print(f"{i.registry}, {i.top_speed}km/h, {i.current_speed}km/h, {i.distance}km")

    def race_over(self):
        for i in self.participants:
            if i.distance >= self.length_km:
                return True
            else:
                return False
def main():
    participants = []
    for i in range(1, 11):
        new_car = Car(f"ABC-{i}", random.randint(100,200))
        participants.append(new_car)
    the_race = Race("Suuri romuralli", 8000, participants)
    hour_counter = 0
    while the_race.race_over() == False:
        if hour_counter % 10 == 0:
            the_race.print_situation()
        hour_counter += 1
        the_race.an_hour_passes()
    the_race.print_situation()

main()
