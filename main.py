import board
import players

class Game:
    """The thing we're playing. Basically the main loop."""
    def __init__(self):
        self.board = board.Chessboard()
        self.white = self.board.white
        self.black = self.board.black
        self.turn = 0

    def sim(self):
        try:
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
print(a.legal_moves(n))
print(a.legal_moves(r))
print(a.legal_moves(p))
g.sim()
