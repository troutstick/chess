import players
import copy

class Chessboard:
    """Where action in the game takes place. As of now, it's probably best to stick to normal chess rules.
    
    Currently:
    Each board has a list of ranks (rows).
    Each rank is itself a list of files (columns).
    Together they correspond to a coordinate on the board.
    """
    dir_vectors = { # for handling piece moves
        1: (0, 1), #up
        2: (1, 1),
        3: (1, 0), #right
        4: (1, -1),
        5: (0, -1), #down
        6: (-1, -1),
        7: (-1, 0), #left
        8: (-1, 1),
        9: (1, 2), #knight 1 o'clock
        10: (2, 1),
        11: (2, -1),
        12: (1, -2),
        13: (-1, -2),
        14: (-2, -1),
        15: (-2, 1),
        16: (-1, 2),
        17: (2, 0), #Castle kingside
        18: (-2, 0), #queenside
        19: (0, 2), #pawn up 2
        20: (0, -2) #pawn down 2
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
    num_letter = {v: k for k, v in letter_num.items()} #inverse of letter_num

    def __init__(self, num_ranks=8, num_files=8):
        self.ranks = []
        for f in range(num_files):
            file_ = []
            for r in range(num_ranks):
                file_.append(None)
            self.ranks.append(file_)
        self.board_setup()
        self.white = players.Player(self, True) # create the white player
        self.black = players.Player(self, False)

    
    def __repr__(self):
        """With self.ranks as input, print out the board (can only do from white's perspective as of now)."""

        display_eppawn = False # if True, show the virtual en passant pawns on the board
        light_sq_str = " - "
        dark_sq_str = " - "

        def print_rank(rank_index):
            rank = self.ranks[rank_index]
            str_output = ""
            light_sq_bool = True
            for piece in rank:
                if (piece and not isinstance(piece, EPPawn)) or (display_eppawn and piece):
                    if piece.is_white:
                        str_output += ("(" + piece.short_name + ")")
                    else:
                        str_output += (" " + piece.short_name + " ")
                elif (rank_index % 2 and light_sq_bool) or ((not rank_index % 2) and (not light_sq_bool)):
                    str_output += light_sq_str #can be used to change appearance of light squares
                else:
                    str_output += dark_sq_str
                light_sq_bool = not light_sq_bool
                str_output += ""
            print(str_output + '|')

        print("  _a__b__c__d__e__f__g__h_")
        for rank_index in range(7, -1, -1):
            print(rank_index + 1, end='|')
            print_rank(rank_index)
        return ""

    def rank_copy(self, ranks):
        """Return a copy of RANKS."""
        rank_copy = []
        rank_index = 0
        for rank in ranks:
            rank_copy.append([])
            for piece in rank:
                if piece != None:
                    rank_copy[rank_index].append(piece.make_copy())
                else:
                    rank_copy[rank_index].append(None)
            rank_index += 1
        return rank_copy

    def move_notation(self, piece, move_vector):
        """Given a piece and its move vector (consisting of direction and step),
        print move notation i.e. Qxh4.
        """
        def capture_str_helper(dest_str):
            """Returns x if capture."""
            if self.select(dest_str[0], int(dest_str[1])):  # if there's a piece at a given coordinate
                if isinstance(piece, Pawn):
                    capture_str = piece.file_pos + "x"
                else:
                    capture_str = "x"
            else:
                capture_str = ""
            return capture_str

        def name_str_helper(piece):
            if isinstance(piece, Pawn):
                name_str = ""
            else:
                name_str = piece.short_name
            return name_str

        direction, step = move_vector[0], move_vector[1]
        start_file, start_rank = piece.file_pos, piece.rank_pos
        file_index, rank_index = self.vect_select_coord(
            start_file, start_rank, direction, step)

        dest_str = self.index_to_coord(file_index, rank_index)
        capture_str = capture_str_helper(dest_str)
        name_str = name_str_helper(piece)

        return name_str + capture_str + dest_str

    def select(self, file_pos, rank_pos):
        """Return the piece in the 1st file and on the 2nd rank like so:
        >>> Chessboard.select("a", 2)
        
        WARNING: File comes before rank here, as is standard in chess notation.
        """
        file_index = self.letter_num[file_pos]
        rank_index = rank_pos - 1
        return self.select_index(file_index, rank_index)

    def select_index(self, file_index, rank_index):
        if file_index < 0 or rank_index < 0 or file_index > 7 or rank_index > 7:
            raise IllegalMoveException('no negative files/ranks')
        return self.ranks[rank_index][file_index]

    def board_setup(self):
        """Add pieces to the board at game start."""
        def board_setup_helper(is_white):
            if is_white:
                home_rank, pawn_rank, pawn_type = 1, 2, WhitePawn
            else:
                home_rank, pawn_rank, pawn_type = 8, 7, BlackPawn
            self.add_piece("a", home_rank, Rook, is_white)
            self.add_piece("b", home_rank, Knight, is_white)
            self.add_piece("c", home_rank, Bishop, is_white)
            self.add_piece("d", home_rank, Queen, is_white)
            self.add_piece("e", home_rank, King, is_white)
            self.add_piece("f", home_rank, Bishop, is_white)
            self.add_piece("g", home_rank, Knight, is_white)
            self.add_piece("h", home_rank, Rook, is_white)
            self.add_piece("a", pawn_rank, pawn_type, is_white)
            self.add_piece("b", pawn_rank, pawn_type, is_white)
            self.add_piece("c", pawn_rank, pawn_type, is_white)
            self.add_piece("d", pawn_rank, pawn_type, is_white)
            self.add_piece("e", pawn_rank, pawn_type, is_white)
            self.add_piece("f", pawn_rank, pawn_type, is_white)
            self.add_piece("g", pawn_rank, pawn_type, is_white)
            self.add_piece("h", pawn_rank, pawn_type, is_white)
        
        board_setup_helper(True) #do white
        board_setup_helper(False) #do black

    def add_piece(self, file_pos, rank_pos, piece_type, is_white):
        file_index = self.letter_num[file_pos]
        rank_index = rank_pos - 1
        self.add_piece_index(file_index, rank_index, piece_type(is_white, file_pos, rank_pos))

    def add_piece_index(self, file_index, rank_index, piece):
        self.ranks[rank_index][file_index] = piece

    def remove_piece(self, file_pos, rank_pos):
        file_index = self.letter_num.get(file_pos)
        rank_index = rank_pos - 1
        self.add_piece_index(file_index, rank_index, None)

    def remove_eppawn(self, is_white):
        """Remove any virtual en passant pawns for a certain player."""
        for rank in self.ranks:
            for piece in rank:
                if isinstance(piece, EPPawn) and piece.is_white == is_white:
                    self.remove_piece(piece.file_pos, piece.rank_pos)

    def move_piece(self, start_file, start_rank, direction, step=1):
        """Pick a direction and a number of squares to move a piece in."""
        piece = self.select(start_file, start_rank)
        piece_type = type(piece)
        is_white = piece.is_white


        new_file_index, new_rank_index = self.vect_select_coord(start_file, start_rank, direction, step)
        coord = self.index_to_coord(new_file_index, new_rank_index)
        new_file = coord[0]
        new_rank = int(coord[1])
        new_piece = piece_type(is_white, new_file, new_rank, True)

        if isinstance(piece, Pawn):
            target_piece = self.vect_select(
                start_file, start_rank, direction, step)
            if isinstance(target_piece, EPPawn):
                pawn = target_piece.real_pawn
                self.remove_piece(pawn.file_pos, pawn.rank_pos)

        if direction == 19 or direction == 20: #en passant
            if direction == 19:
                eppawn_dir = 1
            else:
                eppawn_dir = 5
            self.add_piece(start_file, start_rank, EPPawn, is_white)
            self.move_piece(start_file, start_rank, eppawn_dir)
            eppawn = self.vect_select(start_file, start_rank, eppawn_dir)
            eppawn.real_pawn = new_piece

        self.add_piece_index(new_file_index, new_rank_index, new_piece) #add piece at new square
        self.remove_piece(start_file, start_rank) #delete piece at old square

    def vect_select(self, start_file, start_rank, direction, step=1):
        """Selects a piece given starting position, direction vector, and step count."""
        file_index, rank_index = self.vect_select_coord(start_file, start_rank, direction, step)
        return self.select_index(file_index, rank_index) # handle out of board exception

    def vect_select_coord(self, start_file, start_rank, direction, step=1):
        """Return indices of coordinate given starting coord, direction vect, and step"""
        assert isinstance(start_file, str), "file must be given as str"
        assert 0 < start_rank < 9, "must have valid rank from 1 and 8"
        start_file_index = self.letter_num[start_file]
        start_rank_index = start_rank - 1
        dir_vect = self.dir_vectors[direction]

        delta_files = dir_vect[0] * step
        delta_ranks = dir_vect[1] * step

        new_file_index = delta_files + start_file_index
        new_rank_index = delta_ranks + start_rank_index
        return new_file_index, new_rank_index

    def index_to_coord(self, file_index, rank_index):
        assert 0 <= file_index < 8, "invalid file index"
        assert 0 <= rank_index < 8, "invalid rank index"
        file_str = self.num_letter.get(file_index)
        rank_str = str(rank_index + 1)
        return file_str + rank_str


    """Direction (from white's perspective):
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

    step = how far the piece moves.
    """

    def same_side(self, piece1, piece2):
        """Checks if two pieces are both owned by same side."""
        return piece1.is_white == piece2.is_white

    def list_pieces(self, is_white, ranks):
        """Returns a list of pieces for a player, given a board state."""
        pieces = []
        for rank in ranks:
            for piece in rank:
                if piece and is_white == piece.is_white: # if piece is owned by your side
                    pieces.append(piece)
        return pieces

    def legal_moves(self, this_piece):
        """Returns a list of valid moves for a piece.
        
        WARNING: This function does NOT account for checks/checkmates/related.
        """
        def legal_pawn_moves(this_piece):
            """En passant. Among other things. Ew."""
            valid_moves = []
            if not isinstance(this_piece, EPPawn):
                forward = this_piece.legal_vect[0]
                twice_forward = this_piece.legal_vect[3]
                diagonals = this_piece.legal_vect[1:3]
                target_piece = self.vect_select(
                    this_piece.file_pos, this_piece.rank_pos, forward)
                if not target_piece:
                    valid_moves.append((forward, 1))

                for direction in diagonals:
                    try:
                        target_piece = self.vect_select(
                            this_piece.file_pos, this_piece.rank_pos, direction)
                        if target_piece and (not self.same_side(this_piece, target_piece)):
                            valid_moves.append((direction, 1))
                        
                    except IllegalMoveException:
                        pass
                
                if not this_piece.has_moved:
                    target_piece = self.vect_select(
                        this_piece.file_pos, this_piece.rank_pos, forward)
                    target_piece2 = self.vect_select(
                        this_piece.file_pos, this_piece.rank_pos, twice_forward)
                    if (not target_piece) and (not target_piece2): #if both squares in front are empty
                        valid_moves.append((twice_forward, 1))

            return valid_moves

        if isinstance(this_piece, Pawn):
            return legal_pawn_moves(this_piece)
        else:
            valid_moves = []
            for direction in this_piece.legal_vect:
                step = 1
                met_opponent = False
                while step <= this_piece.max_step: # should throw exception to deal with inf ranged pieces
                    try:
                        if met_opponent:
                            met_opponent = False
                            break
                        
                        target_piece = self.vect_select(this_piece.file_pos, this_piece.rank_pos, direction, step)
                        if target_piece:
                            if self.same_side(this_piece, target_piece):
                                break
                            else:
                                met_opponent = True
                    except IllegalMoveException:
                        break
                    
                    valid_moves.append((direction, step))
                    step += 1
            return valid_moves

    def all_moves(self, is_white, ranks):
        """List all legal moves for a player from a board state. Does NOT account for check."""
        moves = []
        for piece in self.list_pieces(is_white, ranks):
            moves.append([piece] + self.legal_moves(piece))
        return moves

    def in_check(self, ranks, is_white):
        """Given a board state, this function returns True if a player is in check and False otherwise."""
        current_board = self.rank_copy(self.ranks)
        moves = self.all_moves(is_white, current_board)
        print(moves)
        print('aaa')
        print(current_board)
        for piece_move_list in moves:
            if len(piece_move_list) > 1: # if piece has legal moves
                piece = piece_move_list[0]
                move_vectors = piece_move_list[1:]
                for vect in move_vectors: # try all moves
                    direction = vect[0]
                    step = vect[1]
                    self.move_piece(piece.file_pos, piece.rank_pos, direction, step)
                    new_ranks = self.rank_copy(self.ranks)
                    self.ranks = self.rank_copy(current_board)
                    print(current_board)
                    print('hi')
                    if not self.both_kings_alive(new_ranks):
                        return True
        return False

    def both_kings_alive(self, ranks):
        """Return True if ranks contains 2 kings."""
        all_pieces = self.list_pieces(
            True, ranks) + self.list_pieces(False, ranks)
        num_kings = 0
        for piece in all_pieces:
            if isinstance(piece, King):
                num_kings += 1
        assert num_kings <= 2, "there can't be more than 2 kings"
        return num_kings == 2

class Piece:
    """Kings. Queens. Many other pieces. Woo!"""
    short_name = "N/A"
    name = "N/A"
    piece_dict = {
        1: "King",
        2: "Queen",
        3: "Rook",
        4: "Bishop",
        5: "Knight",
        0: "Pawn"
    }

    def __init__(self, is_white, file_pos, rank_pos, has_moved=False):
        self.is_white = is_white # Boolean
        self.file_pos = file_pos # a, b, c
        self.rank_pos = rank_pos # 1, 2, 3
        self.pos =  str(file_pos) + str(rank_pos) # e3, d4
        self.has_moved = has_moved # useful for castling

    def __repr__(self):
        return self.name + " at " + self.pos

    def make_copy(self):
        """Return an exact copy of this piece."""
        new_piece = type(self)(self.is_white, self.file_pos, self.rank_pos, self.has_moved)
        return new_piece

class King(Piece):
    short_name = "K"
    name = "King"
    legal_vect = list(range(1, 9)) # 8 directions it can move
    max_step = 1

class Queen(Piece):
    short_name = "Q"
    name = "Queen"
    legal_vect = list(range(1, 9))
    max_step = float("inf")

class Bishop(Piece):
    short_name = "B"
    name = "Bishop"
    legal_vect = [2, 4, 6, 8]
    max_step = float("inf")


class Knight(Piece):
    short_name = "N"
    name = "Knight"
    legal_vect = list(range(9, 17))
    max_step = 1


class Rook(Piece):
    short_name = "R"
    name = "Rook"
    legal_vect = [1, 3, 5, 7]
    max_step = float("inf")

class Pawn(Piece):
    short_name = "P"
    name = "Pawn"
    max_step = 1

class WhitePawn(Pawn):
    legal_vect = [1, 2, 8, 19]

class BlackPawn(Pawn):
    legal_vect = [5, 4, 6, 20] # normal forward, capture on diagonals, forward 2 squares (for en passant calculation)

class EPPawn(Pawn): #used for calculating en passant
    short_name = "@"
    name = "EPPawn"
    legal_vect = []
    real_pawn = None # if this pawn dies, real pawn dies too
        
class IllegalMoveException(Exception):
    pass
