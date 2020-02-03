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
        all_legal_moves = self.board.all_moves(self.is_white)
        print("You may move these pieces:")
     
        piece_str = ""
        select_dict = {}
        key_num = 1
        for piece_list in all_legal_moves:
            if len(piece_list) > 1:
                piece = piece_list[0]
                piece_str += (str(key_num) + ". " + str(piece) + " | ")
                select_dict.update({key_num: piece_list})
                key_num += 1

        print(piece_str)
        input_num = int(input("Please enter a number to select a piece to move: "))
        piece_move_list = select_dict.get(input_num)
        selected_piece = piece_move_list[0]
        legal_moves = piece_move_list[1:]
        self.play_piece(selected_piece, legal_moves)



    def play_piece(self, piece, piece_moves):
        """Takes input for a piece to choose on a particular move. Spits out move vector"""
        start_file, start_rank = piece.file_pos, piece.rank_pos
        coord_str = ""
        select_move_dict = {}
        key_num = 1
        for move_vector in piece_moves:
            direction = move_vector[0]
            step = move_vector[1]
            file_index, rank_index = self.board.vect_select_coord(start_file, start_rank, direction, step)
            coord_str += (str(key_num) + ". " + self.board.index_to_coord(file_index, rank_index) + " | ")
            select_move_dict.update({key_num: move_vector})
            key_num += 1
        print(coord_str)
        while True:
            input_num1 = int(input("Enter the move you want to make: "))
            input_num2 = int(input("Please reenter your choice: "))
            if input_num1 == input_num2:
                break
            print("Invalid input. Please try again.")
        move_vector = select_move_dict.get(input_num1)
        direction, step = move_vector[0], move_vector[1]
        self.board.move_piece(start_file, start_rank, direction, step)