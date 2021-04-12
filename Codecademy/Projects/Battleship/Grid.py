

class Grid:
    def __init__(self, name=None):
        self.size = 10
        self.name = name
        self.board = [[Cell(i, j) for i in range(self.size)] for j in range(self.size)]

    def __repr__(self):
        return self.print_grid()

    def print_grid(self):
        hypens = ''.join(['-' for i in range(32)])
        title = "{hypens}\n{name}\n{hypens}\n".format(hypens=hypens, name=self.name)
        y_coor = "  " + '  '.join([str(i) for i in range(self.size)]) + '\n'
        field = ""
        for i in range(len(self.board)):
            field += (chr(65+i) + str(self.board[i]) + '\n')
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

    def is_shot(self):
        self.shot = True


if __name__ == '__main__':
    pass
    # playing_field = Grid("test bord")
    # playing_field.print_grid()
