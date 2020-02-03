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

    def __str__(self):
        def print_rank(rank):
            str_output = ""
            for piece in rank:
                if piece:
                    if piece.is_white:
                        str_output += ("(" + piece.name + ")")
                    else:
                        str_output += (" " + piece.name + " ")
                        
                else:
                    str_output += " - "
                str_output += ""
            print(str_output)

        for rank_index in range(7, -1, -1):
            print_rank(self.ranks[rank_index])
        return ""

    def select(self, file_pos, rank_pos):
        """Return the piece in the 1st file and on the 2nd rank like so:
        >>> Chessboard.select("A", 2)
        
        WARNING: File comes before rank here, as is standard in chess notation.
        """
        file_index = self.letter_num[file_pos]
        rank_index = rank_pos - 1
        return self.ranks[rank_index][file_index]

    def board_setup(self):
        def board_setup_helper(is_white):
            if is_white:
                home_rank, pawn_rank = 1, 2
            else:
                home_rank, pawn_rank = 8, 7
            self.add_piece("A", home_rank, Rook(is_white))
            self.add_piece("B", home_rank, Knight(is_white))
            self.add_piece("C", home_rank, Bishop(is_white))
            self.add_piece("D", home_rank, Queen(is_white))
            self.add_piece("E", home_rank, King(is_white))
            self.add_piece("F", home_rank, Bishop(is_white))
            self.add_piece("G", home_rank, Knight(is_white))
            self.add_piece("H", home_rank, Rook(is_white))
            self.add_piece("A", pawn_rank, Pawn(is_white))
            self.add_piece("B", pawn_rank, Pawn(is_white))
            self.add_piece("C", pawn_rank, Pawn(is_white))
            self.add_piece("D", pawn_rank, Pawn(is_white))
            self.add_piece("E", pawn_rank, Pawn(is_white))
            self.add_piece("F", pawn_rank, Pawn(is_white))
            self.add_piece("G", pawn_rank, Pawn(is_white))
            self.add_piece("H", pawn_rank, Pawn(is_white))
        
        board_setup_helper(True)
        board_setup_helper(False)

    def add_piece(self, file_pos, rank_pos, piece):
        file_index = self.letter_num[file_pos]
        rank_index = rank_pos - 1
        self.ranks[rank_index][file_index] = piece

    def move_piece(self, start_file, start_rank, direction, num_squares=0):
        """Pick a direction and a number of squares to move a piece in.
        
        Direction (from white's perspective):
        0 = ???
        1 = Up
        2 = Up-right diagonally
        3 = Right
        4 = Down-right diagonally
        5 = Down
        6 = Down-left diagonally
        7 = Left
        8 = Up-left diagonally

        Numbers + 8: Same but for knight, e.g.
        9 = Up 2, Right 1
        """
        piece = self.select(start_file, start_rank)
        piece_type = type(piece)
        piece = None
        # finish this uwu



c = Chessboard # TEMPORARY: for easier access

class Piece:
    name = ""
    """Kings. Queens. Many other pieces. Woo!"""
    def __init__(self, is_white):
        self.is_white = is_white # Boolean

    def __repr__(self):
        return self.name

class King(Piece):
    name = "K"

class Queen(Piece):
    name = "Q"

class Bishop(Piece):
    name = "B"

class Knight(Piece):
    name = "N"

class Rook(Piece):
    name = "R"

class Pawn(Piece):
    name = "P"