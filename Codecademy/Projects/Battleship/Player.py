from Grid import Grid
from Boat import Boat


class Player:
    def __init__(self, name):
        self.name = name
        self.ship_arrangement = Grid("{0}s field".format(self.name))
        self.boats = self.create_boats()

    def __repr__(self):
        return self.name

    def create_boats(self):
        types = [("Carrier", 5), ("Battleship", 4), ("Destroyer", 3), ("Submarine", 3), ("Patrol boat", 2)]
        boats = [Boat("{0}s {1}".format(self.name, type), size) for type, size in types]
        return boats

    def arrange_ships(self):
        for boat in self.boats:
            pass




if __name__ == '__main__':
    player1 = Player("Sander")
    for boat in player1.boats:
        print(boat)