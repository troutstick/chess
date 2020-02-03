import board
import players

c = board.Chessboard  # TEMPORARY: for easier access
a = c()
a
n = a.list_pieces(True)[1]
r = a.list_pieces(True)[0]
p = a.list_pieces(True)[10]
print(a.legal_moves(n))
print(a.legal_moves(r))
print(a.legal_moves(p))
