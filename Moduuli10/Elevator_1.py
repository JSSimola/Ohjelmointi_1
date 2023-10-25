class Elevator:
    def __init__(self, name, floors, current_floor = 0):
        self.name = name
        self.floors = floors
        self.current_floor = current_floor

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        self.current_floor -= 1
    def move_to_floor(self, desired_floor):
        if desired_floor > self.current_floor and desired_floor <= self.floors:
            for i in range(self.current_floor, desired_floor):
                Elevator.go_up(self)
        elif desired_floor < self.current_floor and desired_floor >= 0:
            for i in range(self.current_floor, desired_floor, -1):
                Elevator.go_down(self)
        else:
            print(f"Rakennuksessa on vain {self.floors} kerrosta")
def main():
    h = Elevator("h", 10)
    h.move_to_floor(5)
    print(f"Siirryit kerrokseen: {h.current_floor}")
    h.move_to_floor(0)
    print(f"Siirryit kerrokseen: {h.current_floor}")

main()
