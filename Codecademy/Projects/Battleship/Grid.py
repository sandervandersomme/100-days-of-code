

class Grid:
    def __init__(self, name=None, size=10):
        self.size = size
        self.name = name
        self.board = [[Cell(i, j) for i in range(self.size)] for j in range(self.size)]

    def __repr__(self):
        return self.print_grid()

    def locate_ship(self, boat):
        """
        Asks for the coordinates of a ship and if those coordinates are valid, places the ship at those coordinates
        """
        print("Let's place {0}. Please keep in mind that it takes up {1} cells".format(boat.name, boat.size))
        bow_location = None
        stern_location = None
        while bow_location is None:
            bow_location = self.get_coordinates("the bow")
            print("starting location is: ", bow_location)
        while stern_location is None:
            stern_location = self.get_coordinates("the stern")
            print("ending location is: ", stern_location)

        # check if combination of coordinates is free
        # check if combination of coordinates forms a vertical or horizontal line
        # check if distance between coordinates is as long the size of the ship

        # if all checks pass, place ship

    def coordinates_form_line(self, pos_bow, pos_stern):
        return pos_bow[0] == pos_stern[0] or pos_bow[1] == pos_stern[1]

    def line_is_boatsize(self, size, pos_bow, pos_stern):
        return size == abs(pos_bow[0] - pos_stern[0]) + 1 or size == abs(pos_bow[1] - pos_stern[1]) + 1

    def all_cells_are_free(self):
        # check ook of de lengte van de boot niet 2 is
        pass

    def get_coordinates(self, stern_or_bow):
        """
        Asks the player for coordinates, returns coordinates if valid.
        Otherwise, returns None
        """
        coordinate = ask_coordinate(stern_or_bow)
        while True:
            if is_correctly_typed(coordinate):
                xpos, ypos = split_convert_coordinates(coordinate)
                if self.is_within_bounds(xpos, ypos) and self.cell_not_taken(xpos, ypos):
                    return xpos, ypos
            coordinate = ask_coordinate(stern_or_bow)

    def cell_not_taken(self, xpos, ypos):
        """
        Checks if the cell at the entered coordinate is not taken
        """
        return self.board[xpos][ypos].is_available()

    def is_within_bounds(self, xpos, ypos):
        """
        Checks if the entered coordinates are on the playing field
        """
        print(xpos, ypos)
        if 0 > xpos or xpos >= self.size:
            print("The given X-coordinate is not present on the playing field. "
                  "Please enter a letter that is present on the playing field")
            return False
        if 0 > ypos or ypos >= self.size:
            return False
        return True

    def print_grid(self):
        """
        Prints the current grid
        """
        hypens = ''.join(['-' for _ in range(32)])
        title = "{hypens}\n{name}\n{hypens}\n".format(hypens=hypens, name=self.name)
        y_coor = "  " + '  '.join([str(i) for i in range(self.size)]) + '\n'
        field = ""
        for i in range(len(self.board)):
            field += (convert_to_letter(i) + str(self.board[i]) + '\n')
        return title+y_coor+field


class Cell:
    def __init__(self, xpos, ypos, boat=None):
        self.xpos = xpos
        self.ypos = ypos
        self.boat = boat
        self.shot = False

    def __repr__(self):
        return 'X' if self.shot else '-'

    def place_boat(self, boat):
        self.boat = boat

    def has_already_been_shot(self):
        return self.shot

    def is_shot(self):
        self.shot = True

    def is_available(self):
        return False if self.boat else True


def split_convert_coordinates(coordinate):
    xpos = convert_to_int(coordinate[0])
    ypos = int(coordinate[1])
    return xpos, ypos


def ask_coordinate(stern_or_bow):
    return input("Where should {0} of the ship be located? "
                 "Enter it's starting position as follows: A1, B3, E6...\n".format(stern_or_bow))


def is_correctly_typed(coordinates):
    """
    Checks if the coordinates are entered in the correct form
    """
    if len(coordinates) > 2:
        print("the entered coordinate contains to many chars. "
              "Please enter a coordinate containing a single letter and a single number only.")
        return False
    if not coordinates[1].isdigit():
        print("Y-coordinate is not a digit. "
              "Please enter a coordinate where the second character is a number")
        return False
    if not coordinates[0].isalpha():
        print("X-coordinate is not a letter. "
              "Please enter a coordinate where the first character is a letter")
        return False
    if not coordinates[0].isupper():
        print("X-coordinate is not uppercase. "
              "Please enter a coordinate where the first character is an uppercase letter")
        return False
    return True


def convert_to_int(pos):
    """
    Converts the letter-coordinate to a numeric position on the playing field
    """
    return ord(pos) - 65


def convert_to_letter(pos):
    """
    Converts a numeric-position to a Letter-coordinate on the playing field
    """
    return chr(65 + pos)


if __name__ == '__main__':
    gr = Grid()
    print()
    print(gr.is_within_bounds(convert_to_int('U'), 3))
