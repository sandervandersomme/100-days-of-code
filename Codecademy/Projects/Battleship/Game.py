from Player import Player

class Game:
    def __init__(self):
        self.players = [Player(input("Enter first players name: ")),
                        Player(input("Enter second players name: "))]


    def start_arrange_phase(self):
        # for player in self.players:
        player = self.players[0]
        print("{0}, please arrange your ships".format(player.name))
        print("Your ships: {0}".format(player.boats))



if __name__ == '__main__':
    game = Game()
    game.start_arrange_phase()