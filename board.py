import players

class Chessboard:
    """Where action in the game takes place. As of now, it's probably best to stick to normal chess rules.
    
    Currently:
    Each board has a list of ranks (rows).
    Each rank is itself a list of files (columns).
    Together they correspond to a coordinate on the board.
    """
    dir_vectors = { # for handling piece moves
        1: (0, 1),
        2: (1, 1),
        3: (1, 0),
        4: (1, -1),
        5: (0, -1),
        6: (-1, -1),
        7: (-1, 0),
        8: (-1, 1),
        9: (1, 2),
        10: (2, 1),
        11: (2, -1),
        12: (1, -2),
        13: (-1, -2),
        14: (-2, -1),
        15: (-2, 1),
        16: (-1, 2)
    }

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
        self.white = players.Player(self, True) # create the white player
        self.black = players.Player(self, False)

    
    def __repr__(self):
        def print_rank(rank_index):
            rank = self.ranks[rank_index]
            str_output = ""
            light_sq = True
            for piece in rank:
                if piece:
                    if piece.is_white:
                        str_output += ("(" + piece.name + ")")
                    else:
                        str_output += (" " + piece.name + " ")
                elif (rank_index % 2 and light_sq) or ((not rank_index % 2) and (not light_sq)):
                    str_output += " - " #can be used to change appearance of light squares
                else:
                    str_output += " - "
                light_sq = not light_sq
                str_output += ""
            print(str_output + '|')

        print("  _a__b__c__d__e__f__g__h_")
        for rank_index in range(7, -1, -1):
            print(rank_index + 1, end='|')
            print_rank(rank_index)
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
        """Add pieces to the board at game start."""
        def board_setup_helper(is_white):
            if is_white:
                home_rank, pawn_rank = 1, 2
            else:
                home_rank, pawn_rank = 8, 7
            self.add_piece("A", home_rank, Rook, is_white)
            self.add_piece("B", home_rank, Knight, is_white)
            self.add_piece("C", home_rank, Bishop, is_white)
            self.add_piece("D", home_rank, Queen, is_white)
            self.add_piece("E", home_rank, King, is_white)
            self.add_piece("F", home_rank, Bishop, is_white)
            self.add_piece("G", home_rank, Knight, is_white)
            self.add_piece("H", home_rank, Rook, is_white)
            self.add_piece("A", pawn_rank, Pawn, is_white)
            self.add_piece("B", pawn_rank, Pawn, is_white)
            self.add_piece("C", pawn_rank, Pawn, is_white)
            self.add_piece("D", pawn_rank, Pawn, is_white)
            self.add_piece("E", pawn_rank, Pawn, is_white)
            self.add_piece("F", pawn_rank, Pawn, is_white)
            self.add_piece("G", pawn_rank, Pawn, is_white)
            self.add_piece("H", pawn_rank, Pawn, is_white)
        
        board_setup_helper(True)
        board_setup_helper(False)

    def add_piece(self, file_pos, rank_pos, piece_type, is_white):
        file_index = self.letter_num[file_pos]
        rank_index = rank_pos - 1
        self.add_piece_index(file_index, rank_index, piece_type(is_white))

    def add_piece_index(self, file_index, rank_index, piece):
        self.ranks[rank_index][file_index] = piece

    def remove_piece(self, file_pos, rank_pos):
        file_index = self.letter_num[file_pos]
        rank_index = rank_pos - 1
        self.add_piece_index(file_index, rank_index, None)

    def move_piece(self, start_file, start_rank, direction, num_squares=1):
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

        num_squares represents how far the piece moves, and is not needed for knight.
        """
        piece = self.select(start_file, start_rank)
        piece_type = type(piece)
        is_white = piece.is_white

        file_index = self.letter_num[start_file]
        rank_index = start_rank - 1
        
        dir_vect = self.dir_vectors[direction]
        delta_files = dir_vect[0] * num_squares
        delta_ranks = dir_vect[1] * num_squares
        file_index += delta_files
        rank_index += delta_ranks
        self.add_piece_index(file_index, rank_index, piece_type(is_white))
        self.remove_piece(start_file, start_rank)

    def list_pieces(self, is_white):
        """Returns a list of pieces for a player and their positions on the board."""
        for rank in self.ranks:
            return


c = Chessboard # TEMPORARY: for easier access

class Piece:
    name = "N/A"
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
