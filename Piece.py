import pygame
from pathlib import Path

# Setup images
img_dir = Path(__file__).parent / "img"

# Piece images
b_pawn = pygame.image.load(img_dir / "black_pawn.png")
b_rook = pygame.image.load(img_dir / "black_rook.png")
b_knight = pygame.image.load(img_dir / "black_knight.png")
b_bishop = pygame.image.load(img_dir / "black_bishop.png")
b_queen = pygame.image.load(img_dir / "black_queen.png")
b_king = pygame.image.load(img_dir / "black_king.png")
w_pawn = pygame.image.load(img_dir / "white_pawn.png")
w_rook = pygame.image.load(img_dir / "white_rook.png")
w_knight = pygame.image.load(img_dir / "white_knight.png")
w_bishop = pygame.image.load(img_dir / "white_bishop.png")
w_queen = pygame.image.load(img_dir / "white_queen.png")
w_king = pygame.image.load(img_dir / "white_king.png")

# Scale images
b_img = [b_pawn, b_rook, b_knight, b_bishop, b_queen, b_king]
w_img = [w_pawn, w_rook, w_knight, w_bishop, w_queen, w_king]

B_img = []
W_img = []

for img in b_img:
    B_img.append(pygame.transform.scale(img, (70, 70)))

for img in w_img:
    W_img.append(pygame.transform.scale(img, (70, 70)))


# Piece class
class Piece:
    """
    Represents a Chess Piece which has a type_char (string) as a
    private data member, as well as get method for piece type and color.
    There is also a method which determines, based on piece type and color, if
    a move is allowed per the rules of Chess.
    It it not currently envisoined that this class will need to communicate
    with other classes (but this may change by the end).
    """

    RECT = (0, 0, 600, 600)
    startX = RECT[0]
    startY = RECT[1]

    def __init__(self, row, col, color):
        """
        Creates a Chess Piece object with the specified type.
        """
        self._piece_row = row
        self._piece_col = col
        self._piece_color = color
        self._selected = False

    def get_selected(self):
        return self._selected

    def set_selected(self, selected):
        self._selected = selected

    def get_piece_row(self):
        """
        Returns row as int.
        """
        return self._piece_row

    def get_piece_col(self):
        """
        Returns col as int.
        """
        return self._piece_col

    def set_row_col(self, end_coords):
        self._piece_row = end_coords[0]
        self._piece_col = end_coords[1]

    def draw_piece(self, win):
        """
        Draws piece on board.
        """
        draw_this = self.get_image()

        x = 5 + self.startX + (self._piece_col * self.RECT[2] / 8)
        y = 5 + self.startY + (self._piece_row * self.RECT[3] / 8)

        if self._selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 70, 70), 5)

        win.blit(draw_this, (x, y))


class Pawn(Piece):
    # Pawn piece which inherits from Piece class
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def get_piece_type(self):
        return "PAWN"

    def get_piece_color(self):
        return self._piece_color

    # Get image of piece
    def get_image(self):
        if self.get_piece_color() == "BLACK":
            return B_img[0]
        else:
            return W_img[0]

    def is_move_sanctioned(self, bearing, directionality, length, move_coords):
        """
        Checks if move is allowed per the rules of Chess for each of the different
        types of pieces. Requires bearing, directionality, length and move_coords parameters
        which are determined by separate methods in the ChessVar class. Returns True if move is
        sanctioned, False if not.
        """
        # Check directionality is correct
        if directionality == "L-SHAPED":
            print("Error: PAWN cannot move in an L-shape.")
            return False

        if self.get_piece_color() == "BLACK":
            # Check bearing is correct
            if bearing != "SOUTH":
                print("Error: BLACK PAWN must move SOUTH.")
                return False

            # First move
            if move_coords[0][0] == 1:
                if length <= 2:
                    return True
                else:
                    print(
                        "Error: BLACK PAWN can only move SOUTH for 1 or 2 spaces on its first move."
                    )
                    return False
            else:
                if length == 1:
                    return True
                else:
                    print(
                        "Error: BLACK PAWN can only move SOUTH for 1 space after its first move."
                    )
                    return False

        else:
            if bearing != "NORTH":
                print("Error: WHITE PAWN must move NORTH.")
                return False

            # First move
            if move_coords[0][0] == 6:
                if length <= 2:
                    return True
                else:
                    print(
                        "Error: WHITE PAWN can only move NORTH for 1 or 2 spaces on its first move."
                    )
                    return False
            else:
                if length == 1:
                    return True
                else:
                    print(
                        "Error: WHITE PAWN can only move NORTH for 1 space after its first move."
                    )
                    return False


class Rook(Piece):
    # Rook piece which inherits from Piece class
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def get_piece_type(self):
        return "ROOK"

    def get_piece_color(self):
        return self._piece_color

    # Get image of piece
    def get_image(self):
        if self.get_piece_color() == "BLACK":
            return B_img[1]
        else:
            return W_img[1]

    def is_move_sanctioned(self, bearing, directionality, length, move_coords):
        """
        Checks if move is allowed per the rules of Chess for each of the different
        types of pieces. Requires bearing, directionality, length and move_coords parameters
        which are determined by separate methods in the ChessVar class. Returns True if move is
        sanctioned, False if not.
        """
        # Can move any number of spaces forward, backward, left or right
        if directionality == "PERPENDICULAR":
            return True
        else:
            return False


class Knight(Piece):
    # Knight piece which inherits from Piece class
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def get_piece_type(self):
        return "KNIGHT"

    def get_piece_color(self):
        return self._piece_color

    # Get image of piece
    def get_image(self):
        if self.get_piece_color() == "BLACK":
            return B_img[2]
        else:
            return W_img[2]

    def is_move_sanctioned(self, bearing, directionality, length, move_coords):
        """
        Checks if move is allowed per the rules of Chess for each of the different
        types of pieces. Requires bearing, directionality, length and move_coords parameters
        which are determined by separate methods in the ChessVar class. Returns True if move is
        sanctioned, False if not.
        """
        # Can move in an L-shape
        if directionality == "L-SHAPED":
            return True
        else:
            return False


class Bishop(Piece):
    # Bishop piece which inherits from Piece class
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def get_piece_type(self):
        return "BISHOP"

    def get_piece_color(self):
        return self._piece_color

    # Get image of piece
    def get_image(self):
        if self.get_piece_color() == "BLACK":
            return B_img[3]
        else:
            return W_img[3]

    def is_move_sanctioned(self, bearing, directionality, length, move_coords):
        """
        Checks if move is allowed per the rules of Chess for each of the different
        types of pieces. Requires bearing, directionality, length and move_coords parameters
        which are determined by separate methods in the ChessVar class. Returns True if move is
        sanctioned, False if not.
        """
        # Can move any number of spaces diagonally
        if directionality == "DIAGONAL":
            return True
        else:
            return False


class Queen(Piece):
    # Queen piece which inherits from Piece class
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def get_piece_type(self):
        return "QUEEN"

    def get_piece_color(self):
        return self._piece_color

    # Get image of piece
    def get_image(self):
        if self.get_piece_color() == "BLACK":
            return B_img[4]
        else:
            return W_img[4]

    def is_move_sanctioned(self, bearing, directionality, length, move_coords):
        """
        Checks if move is allowed per the rules of Chess for each of the different
        types of pieces. Requires bearing, directionality, length and move_coords parameters
        which are determined by separate methods in the ChessVar class. Returns True if move is
        sanctioned, False if not.
        """
        # Cannot move in an L-shape
        if directionality == "L-SHAPED":
            return False
        # Can move any number of spaces forward, backward, left, right, or diagonally
        else:
            return True


class King(Piece):
    # King piece which inherits from Piece class
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def get_piece_type(self):
        return "KING"

    def get_piece_color(self):
        return self._piece_color

    # Get image of piece
    def get_image(self):
        if self.get_piece_color() == "BLACK":
            return B_img[5]
        else:
            return W_img[5]

    def is_move_sanctioned(self, bearing, directionality, length, move_coords):
        """
        Checks if move is allowed per the rules of Chess for each of the different
        types of pieces. Requires bearing, directionality, length and move_coords parameters
        which are determined by separate methods in the ChessVar class. Returns True if move is
        sanctioned, False if not.
        """
        # King can move 1 space in any direction
        if length == 1:
            return True
        else:
            return False
