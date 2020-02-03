import board

class Player:
    """One of the two players of the chess game.
    
    Handles move legality, turns, piece movement, and basically the things that the players do.
    """
    def __init__(self, board, is_white):
        self.is_white = is_white
        self.board = board

    def play(self):
        """Make a move."""
        self.board.list_pieces(self.is_white)
        print(self.board)
        legal_moves = self.board.all_moves(self.is_white)
        print(legal_moves)
        print("You may move these pieces:")
        piece_str = ""
        for piece_list in legal_moves:
            if len(piece_list) > 1:
                piece_str += (str(piece_list[0]) + " ")
        print(piece_str)
        