

class Boat:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parts_sunk = 0

    def __repr__(self):
        return self.name

    def increase_sunken_parts(self):
        self.parts_sunk += 1

    def is_destroyed(self):
        return self.parts_sunk == self.size


if __name__ == '__main__':
    carrier = Boat("Carrier", 5)
    battleship = Boat("Battleship", 4)
    destroyer = Boat("Destroyer", 3)
    submarine = Boat("Submarine", 3)
    patrol_boat = Boat("Patrol_boat", 2)