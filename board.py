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
        17: "TODO 0-0"
        18: "TODO 0-0-0"
        19: (0, 2)
        20: (0, -2)
    }

    letter_num = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
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
            self.add_piece("a", home_rank, Rook, is_white)
            self.add_piece("b", home_rank, Knight, is_white)
            self.add_piece("c", home_rank, Bishop, is_white)
            self.add_piece("d", home_rank, Queen, is_white)
            self.add_piece("e", home_rank, King, is_white)
            self.add_piece("f", home_rank, Bishop, is_white)
            self.add_piece("g", home_rank, Knight, is_white)
            self.add_piece("h", home_rank, Rook, is_white)
            self.add_piece("a", pawn_rank, Pawn, is_white)
            self.add_piece("b", pawn_rank, Pawn, is_white)
            self.add_piece("c", pawn_rank, Pawn, is_white)
            self.add_piece("d", pawn_rank, Pawn, is_white)
            self.add_piece("e", pawn_rank, Pawn, is_white)
            self.add_piece("f", pawn_rank, Pawn, is_white)
            self.add_piece("g", pawn_rank, Pawn, is_white)
            self.add_piece("h", pawn_rank, Pawn, is_white)
        
        board_setup_helper(True)
        board_setup_helper(False)

    def add_piece(self, file_pos, rank_pos, piece_type, is_white):
        file_index = self.letter_num[file_pos]
        rank_index = rank_pos - 1
        self.add_piece_index(file_index, rank_index, piece_type(is_white, file_pos, rank_pos))

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

        17 = Kingside castling
        18 = Queenside castling
        19 = Pawn up 2 squares
        20 = Pawn down 2 squares

        num_squares represents how far the piece moves.
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
        self.add_piece_index(file_index, rank_index, piece_type(is_white)) #add piece at new square
        self.remove_piece(start_file, start_rank) #delete piece at old square

    def list_pieces(self, is_white):
        """Returns a list of pieces for a player."""
        pieces = []
        for rank in self.ranks:
            for piece in rank:
                if piece and is_white == piece.is_white: # if piece is owned by your side
                    pieces.append(piece)
        return pieces

    def legal_moves(self, piece):
        """Returns a list of valid moves for a piece."""
        pass

c = Chessboard # TEMPORARY: for easier access

class Piece:
    name = "N/A"
    """Kings. Queens. Many other pieces. Woo!"""
    def __init__(self, is_white, file_pos, rank_pos):
        self.is_white = is_white # Boolean
        self.file_pos = file_pos # a, b, c
        self.rank_pos = rank_pos # 1, 2, 3
        self.pos =  file_pos + str(rank_pos) # e3, d4
        self.has_moved = False # useful for castling

    def __repr__(self):
        return self.name + "@" + self.pos

class King(Piece):
    name = "K"
    legal_vect = list(range(1, 9)) # 8 directions it can move
    max_step = 1

class Queen(Piece):
    name = "Q"
    legal_vect = list(range(1, 9))
    max_step = float("inf")

class Bishop(Piece):
    name = "B"
    legal_vect = [2, 4, 6, 8]
    max_step = float("inf")


class Knight(Piece):
    name = "N"
    legal_vect = [list(range(9, 17))]
    max_step = 1


class Rook(Piece):
    name = "R"
    legal_vect = [1, 3, 5, 7]
    max_step = float("inf")

class Pawn(Piece):
    name = "P"
    legal_vect = [1, 2, 8, 19, 20]
    max_step = 1


class IllegalMoveException(Exception):
    pass
