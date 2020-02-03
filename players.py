import board

class Player:
    """One of the two players of the chess game.
    
    Handles move legality, turns, piece movement, and basically the things that the players do.
    """
    def __init__(self, chessboard, is_white):
        self.is_white = is_white
        self.chessboard = chessboard