from . import pieces

class Bishop(pieces.Piece):
    # This is the piece class for the bishop.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
    def legal_moves(self, current_board):
        legal_squares = []

        for tl in range(8):
            point_x = self.x - tl
            point_y = self.y + tl

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for tr in range(8):
            point_x = self.x + tr
            point_y = self.y + tr

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for bl in range(8):
            point_x = self.x - bl
            point_y = self.y - bl

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for br in range(8):
            point_x = self.x + br
            point_y = self.y - br

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        return legal_squares

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []
