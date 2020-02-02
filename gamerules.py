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
        self.board_setup()
    
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

    def board_setup(self):
        def board_setup_helper(home_rank, pawn_rank, is_white):
            if is_white:
                home_rank, pawn_rank = 1, 2
            else:
                home_rank, pawn_rank = 8, 7
            self.select("A", home_rank) = Rook(is_white)
            self.select("B", home_rank) = Knight(is_white)
            self.select("C", home_rank) = Bishop(is_white)
            self.select("D", home_rank) = Queen(is_white)
            self.select("E", home_rank) = King(is_white)
            self.select("F", home_rank) = Bishop(is_white)
            self.select("G", home_rank) = Knight(is_white)
            self.select("H", home_rank) = Rook(is_white)
            self.select("A", pawn_rank) = Pawn(is_white)
            self.select("B", pawn_rank) = Pawn(is_white)
            self.select("C", pawn_rank) = Pawn(is_white)
            self.select("D", pawn_rank) = Pawn(is_white)
            self.select("E", pawn_rank) = Pawn(is_white)
            self.select("F", pawn_rank) = Pawn(is_white)
            self.select("G", pawn_rank) = Pawn(is_white)
            self.select("H", pawn_rank) = Pawn(is_white)
        
        board_setup_helper(True)
        board_setup_helper(False)


c = Chessboard # TEMPORARY: for easier access

class Piece:
    """Kings. Queens. Many other pieces. Woo!"""
    def __init__(self, file_pos, rank_pos, is_white):
        self.file_pos = file_pos
        self.rank_pos = rank_pos
        self.is_white = is_white # Boolean

class King(Piece):

class Queen(Piece):

class Bishop(Piece):

class Knight(Piece):

class Rook(Piece):

class Pawn(Piece):