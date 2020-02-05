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
        """Play game."""
        try:
            print("White to move.")
            while True:
                self.white.play()
                print("White makes a move!")
                self.black.play()
                print("Black makes a move!")
                self.turn += 1
        except GameOverException:
            print("Game over!")

class GameOverException(Exception):
    pass

g = Game()

a = g.board  # TEMPORARY: for easier access
a
if False:
    print(a.legal_moves(n))
    print(a.legal_moves(r))
    print(a.legal_moves(p))
g.sim()
