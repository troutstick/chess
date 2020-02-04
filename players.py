import board

class Player:
    """One of the two players of the chess game.
    
    Handles move legality, turns, piece movement, and basically the things that the players do.
    """
    def __init__(self, board, is_white):
        self.is_white = is_white
        self.board = board

    def display_board(self):
        print(self.board)
        if self.is_white:
            print("White to move.")
        else:
            print("Black to move.")


    def play(self):
        """Make a move."""
        has_moved = False
        while not has_moved:
            try:
                self.board.list_pieces(self.is_white)
                self.display_board()
                all_legal_moves = self.board.all_moves(self.is_white)
                piece_dict = board.Piece.piece_dict
                available_piece_names = set()
                for piece_list in all_legal_moves:
                    if len(piece_list) > 1:
                        piece = piece_list[0]
                        available_piece_names.add(piece.name)
                while True:
                    try:
                        piece_type_str = ""
                        available_nums = set()
                        for num, name in piece_dict.items():
                            if name in available_piece_names:
                                piece_type_str += (str(num) + ". " + name + " | ")
                                available_nums.add(num)
                        print(piece_type_str)
                        input_num = int(input("Please enter a number to select what kind of piece you want to move: "))
                        if not input_num in available_nums:
                            raise IndexError('invalid num')
                        else:
                            break
                    except IndexError or ValueError:
                        print("Invalid input. Please move a piece with a legal move.")
                selected_name = piece_dict.get(input_num)

                piece_str = ""
                select_dict = {}
                key_num = 1
                for piece_list in all_legal_moves:
                    piece = piece_list[0]
                    if len(piece_list) > 1 and piece.name == selected_name:
                        piece_str += (str(key_num) + ". " + str(piece) + " | ")
                        select_dict.update({key_num: piece_list})
                        key_num += 1
                if len(select_dict) > 1:
                    while True:
                        try:
                            print("0. Go back. | " + piece_str) # display available options to player
                            input_num = int(input("Please enter a number to select a piece to move: "))
                            if input_num == 0:
                                raise ReturnException
                            if input_num >= key_num or input_num < 0:
                                raise IndexError
                            break
                        except ValueError or IndexError:
                            print(
                                f"Invalid input. Please enter a number from 1 through {key_num-1}.")
                else:
                    input_num = 1 #skip loop if there's only one of a piece i.e. don't waste time selecting which king you want

                piece_move_list = select_dict.get(input_num)
                selected_piece = piece_move_list[0]
                legal_moves = piece_move_list[1:]
                self.play_piece(selected_piece, legal_moves)
                has_moved = True
                self.board.remove_eppawn(not self.is_white) # remove opponent's virtual en passant pawns
            except ReturnException:
                print("Returning.")



    def play_piece(self, piece, piece_moves):
        """Takes input for a piece to choose a particular move and moves it accordingly."""
        start_file, start_rank = piece.file_pos, piece.rank_pos
        coord_str = ""
        select_move_dict = {}
        key_num = 1
        for move_vector in piece_moves:
            direction = move_vector[0]
            step = move_vector[1]
            file_index, rank_index = self.board.vect_select_coord(start_file, start_rank, direction, step)
            dest_str = self.board.index_to_coord(file_index, rank_index)

            if self.board.select(dest_str[0], int(dest_str[1])): # if move will make a capture
                if isinstance(piece, board.Pawn):
                    capture_str = piece.file_pos + "x"
                else:
                    capture_str = "x"
            else:
                capture_str = ""

            if isinstance(piece, board.Pawn):
                name_str = ""
            else:
                name_str = piece.name
            coord_str += (str(key_num) + ". " + name_str + capture_str + dest_str + " | ") #print move notation i.e. Qxh4
            select_move_dict.update({key_num: move_vector})
            key_num += 1
        while True:
            try:
                print("0. Go back. | " + coord_str)
                input_num = int(input("Enter the move you want to make: "))
                if input_num == 0:
                    raise ReturnException("go back")
                if input_num >= key_num or input_num < 0:
                    raise ValueError
                break
            except ValueError:
                print(f"Invalid input. Please enter a number from 1 through {key_num-1}.")
        while True:
            try:
                break_num = int(input("Enter 1 to confirm your move. 0 to go back: "))
                if break_num == 1:
                    break
                elif break_num == 0:
                    raise ReturnException
                else:
                    print("Invalid input.")
            except ValueError:
                print("Please enter a number.")

        move_vector = select_move_dict.get(input_num)
        direction, step = move_vector[0], move_vector[1]
        self.board.move_piece(start_file, start_rank, direction, step)

class ReturnException(Exception):
    pass
