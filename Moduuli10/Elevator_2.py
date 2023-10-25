class Elevator:
    def __init__(self, id, bottom_floor, top_floor, current_floor = 0):
        self.id = id
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        self.current_floor -= 1
    def move_to_floor(self, desired_floor):
        if desired_floor > self.current_floor and desired_floor <= self.top_floor:
            for i in range(self.current_floor, desired_floor):
                Elevator.go_up(self)
        elif desired_floor < self.current_floor and desired_floor >= self.bottom_floor:
            for i in range(self.current_floor, desired_floor, -1):
                Elevator.go_down(self)
        else:
            print(f"Rakennuksessa on vain {self.floors} kerrosta")

class House:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators
        self.elevators = []
        for i in range(1,num_elevators+1):
            self.elevators.append(Elevator(f"Hissi-{i}", self.bottom_floor, self.top_floor))

    def operate_elevator(self, id, desired_floor):
        self.elevators[id].move_to_floor(desired_floor)


def main():
    talo = House(-1, 10, 3)
    talo.operate_elevator(1, 3)
    talo.operate_elevator(0, 10)
    talo.operate_elevator(2, -1)
    for i in talo.elevators:
        print(f"{i.id}: kerros {i.current_floor}")

main()
