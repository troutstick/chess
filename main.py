import board
import players

class Game:
    """The thing we're playing. Basically the main loop."""
    def __init__(self):
        self.board = board.Chessboard()
        self.white = self.board.white
        print("White makes a move!")
        self.black = self.board.black
        print("Black makes a move!")
        self.turn = 0

    def sim(self):
        """Play game."""
        try:
            while True:
                self.white.play()
                self.black.play()
                self.turn += 1
        except GameOverException:
            print("Game over!")

class GameOverException(Exception):
    pass

g = Game()

a = g.board  # TEMPORARY: for easier access
a
n = a.list_pieces(True)[1]
r = a.list_pieces(True)[0]
p = a.list_pieces(True)[10]
if False:
    print(a.legal_moves(n))
    print(a.legal_moves(r))
    print(a.legal_moves(p))
g.sim()
