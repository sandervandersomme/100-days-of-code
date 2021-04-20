from Player import Player

class Game:
    def __init__(self):
        self.players = [Player(input("Enter first players name: ")),
                        Player(input("Enter second players name: "))]


    def setup_board(self):
        """
        Each player arranges their boats across their field
        """
        for player in self.players:
            print("{0}, please arrange your ships".format(player.name))
            print("Your ships: {0}".format(player.boats))
            player.arrange_ships()

    def start_game(self):
        current_player = 0
        print("{0}s turn".format(self.players[current_player]))
        # switch player
        # current_player = 1 - current_player



if __name__ == '__main__':
    game = Game()
    game.setup_board()
    game.start_game()