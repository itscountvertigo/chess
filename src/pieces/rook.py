from . import pieces

import move_coords

class Rook(pieces.Piece):
    # This is the piece class for the rook.
    # It inherits from the Piece() parent class in pieces.py
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.piece_value = 5
        self.piece_character = 'B'

        self.in_starting_position = True

        if color == 0:
            self.sprite_path = "assets/default_sprites/black/black_rook.png"
        else:
            self.sprite_path = "assets/default_sprites/white/white_rook.png"

    def legal_moves(self, current_board):
        legal_squares = []

        for left in range(8):
            point_x = self.x - left
            point_y = self.y

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

        for right in range(8):
            point_x = self.x + right
            point_y = self.y

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

        for up in range(8):
            point_x = self.x
            point_y = self.y + up

            if point_y == self.y:
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

        for down in range(8):
            point_x = self.x
            point_y = self.y - down

            if point_y == self.y:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            blocked_by_own_piece = False
            capturing_piece = False

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])
        
        legal_moves = []
        for each in legal_squares:
            legal_moves.append(move_coords.coords_to_move(self.x, self.y, each[0], each[1]))
            # legal_moves.append(chr(ord('`')+(self.x + 1)) + str(self.y + 1) + chr(ord('`')+(each[0] + 1)) + str(each[1] + 1))

        return legal_moves

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []
