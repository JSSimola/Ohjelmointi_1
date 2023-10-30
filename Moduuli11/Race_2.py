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

class ElectricCar(Car):
    def __init__(self, registry, top_speed, battery_capacity, current_speed, distance):
        super().__init__(registry, top_speed, current_speed, distance)
        self.battery_capacity = battery_capacity

class CombustionEngineCar(Car):
    def __init__(self, registry, top_speed, fuel_tank_volume, current_speed, distance):
        super().__init__(registry, top_speed, current_speed, distance)
        self.fuel_tank_volume = fuel_tank_volume

def main():
    car_1 = ElectricCar("ABC-15", 180, 52.5, 120, 0)
    car_2 = CombustionEngineCar("ACD-123", 165, 32.3, 110, 0)
    car_1.drive(3)
    car_2.drive(3)
    print(f"Sähköauton matkamittari 3h jälkeen: {car_1.distance}")
    print(f"Polttomoottoriauton matkamittari 3h jälkeen: {car_2.distance}")

main()
