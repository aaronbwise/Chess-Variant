from Piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King


class Board:
    """
    Represents a Board which has a game_board as a private data member,
    as well as get and set methods for Chess piece locations. It is not
    currently envisioned that this will interact with other classes (but
    this may change by the end).
    """

    def __init__(self, rows=8, cols=8):
        """
        Initializes a Board object with Chess pieces in starting locations.
        Uppercase letters represent black pieces, lowercase letters represent white pieces.
        """
        self._rows = rows
        self._cols = cols

        self._board = [[0 for x in range(self._cols)] for _ in range(self._rows)]
        self._board[0][0] = Rook(0, 0, "BLACK")
        self._board[0][1] = Knight(0, 1, "BLACK")
        self._board[0][2] = Bishop(0, 2, "BLACK")
        self._board[0][3] = Queen(0, 3, "BLACK")
        self._board[0][4] = King(0, 4, "BLACK")
        self._board[0][5] = Bishop(0, 5, "BLACK")
        self._board[0][6] = Knight(0, 6, "BLACK")
        self._board[0][7] = Rook(0, 7, "BLACK")
        self._board[1][0] = Pawn(1, 0, "BLACK")
        self._board[1][1] = Pawn(1, 1, "BLACK")
        self._board[1][2] = Pawn(1, 2, "BLACK")
        self._board[1][3] = Pawn(1, 3, "BLACK")
        self._board[1][4] = Pawn(1, 4, "BLACK")
        self._board[1][5] = Pawn(1, 5, "BLACK")
        self._board[1][6] = Pawn(1, 6, "BLACK")
        self._board[1][7] = Pawn(1, 7, "BLACK")

        self._board[7][0] = Rook(7, 0, "WHITE")
        self._board[7][1] = Knight(7, 1, "WHITE")
        self._board[7][2] = Bishop(7, 2, "WHITE")
        self._board[7][3] = Queen(7, 3, "WHITE")
        self._board[7][4] = King(7, 4, "WHITE")
        self._board[7][5] = Bishop(7, 5, "WHITE")
        self._board[7][6] = Knight(7, 6, "WHITE")
        self._board[7][7] = Rook(7, 7, "WHITE")
        self._board[6][0] = Pawn(6, 0, "WHITE")
        self._board[6][1] = Pawn(6, 1, "WHITE")
        self._board[6][2] = Pawn(6, 2, "WHITE")
        self._board[6][3] = Pawn(6, 3, "WHITE")
        self._board[6][4] = Pawn(6, 4, "WHITE")
        self._board[6][5] = Pawn(6, 5, "WHITE")
        self._board[6][6] = Pawn(6, 6, "WHITE")
        self._board[6][7] = Pawn(6, 7, "WHITE")

        self._game_turn = "WHITE"

    def get_game_board(self):
        """
        Get method which returns the current board.
        """
        return self._board

    def get_game_turn(self):
        """
        Get method which returns the current game turn.
        """
        return self._game_turn

    def set_game_turn(self, game_turn):
        """
        Set method which sets the game turn.
        """
        self._game_turn = game_turn

    def get_piece(self, location):
        """
        Get method which returns the piece at the given location.
        """
        row = location[0]
        col = location[1]
        return self._board[row][col]

    def set_piece(self, start_location, end_location, piece):
        """
        Set method which sets the piece at the given location.
        """
        print(f"start_location: {start_location}, end_location: {end_location}")
        # Set piece at start location to empty
        self._board[start_location[0]][start_location[1]] = 0

        # Set piece at end location to piece
        self._board[end_location[0]][end_location[1]] = piece

        # Update piece row and col
        piece.set_row_col(end_location)

    def print_board(self):
        """
        Prints the Chess piece locations on the current board.
        """
        for row in self._board:
            print(row)

    def draw(self, win):
        for i in range(self._rows):
            for j in range(self._cols):
                if self._board[i][j] != 0:
                    self._board[i][j].draw_piece(win)

    def select(self, row, col):
        for i in range(self._rows):
            for j in range(self._cols):
                if self._board[i][j] != 0:
                    self._board[i][j]._selected = False

        if self._board[row][col] != 0:
            self._board[row][col].set_selected(True)


def main():
    print("Testing Board class...")
    board = Board()
    board.draw()


if __name__ == "__main__":
    main()
