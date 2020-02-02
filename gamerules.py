class Chessboard:
    """Where action in the game takes place. As of now, it's probably best to stick to normal chess rules.
    
    Currently:
    Each board has a list of ranks (rows).
    Each rank is itself a list of files (columns).
    Together they correspond to a coordinate on the board.
    """
    letter_num = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7
    }
    def __init__(self, num_ranks=8, num_files=8):
        self.ranks = []
        for f in range(num_files):
            file = []
            for r in range(num_ranks):
                file.append(None)
            self.ranks.append(file)
    
    def __repr__(self):
        return "Hi. I'm a chessboard."

    def select(self, file_pos, rank_pos):
        """Return the item in the 1st file and on the 2nd rank like so:
        >>> Chessboard.select("A", 2)
        
        WARNING: File comes before rank here, as is standard in chess notation.
        """
        file_index = self.letter_num[file_pos]
        rank_index = rank_pos - 1
        return self.ranks[rank_index][file_index]

c = Chessboard # TEMPORARY: for easier access

class Piece:
    """Kings. Queens. Many other pieces. Woo!"""

class King:

class Queen:

class Bishop:

class Knight:

class Rook:

class Pawn: