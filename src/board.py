from pieces import king, queen, rook, knight, bishop, pawn

pieces = [king.King(4, 0, 1),                              # white king
         queen.Queen(3, 0, 1),                            # white queen
         bishop.Bishop(2, 0, 1), bishop.Bishop(5, 0, 1),  # white bishops
         knight.Knight(1, 0, 1), knight.Knight(6, 0, 1),  # white knights
         rook.Rook(0, 0, 1), rook.Rook(7, 0, 1),          # white rooks
         king.King(4, 7, 0),                              # black king
         queen.Queen(3, 7, 0),                            # black queen
         bishop.Bishop(2, 7, 0), bishop.Bishop(5, 7, 0),  # black bishops
         knight.Knight(1, 7, 0), knight.Knight(6, 7, 0),  # black knights
         rook.Rook(0, 7, 0), rook.Rook(7, 7, 0)           # black rooks
        ]

for i in range(8):
    pieces.append(pawn.Pawn(i, 1, 1))  # add white pawns
    pieces.append(pawn.Pawn(i, 6, 0))  # add black pawns

who_to_move = 1
moves = []

# Ply means half-move, as in one movement of the piece. 
# A full 'move', in chess terms, would be both sides moving once (2 ply)
# Use this variable when dealing with engine depth, not move_num!
ply = 1

# Move number for the standard chess notation function in generate_move_text.py. 
# Not used for engine depth, use the ply variable (above this) for that.
move_num = 1