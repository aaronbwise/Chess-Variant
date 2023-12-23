from Piece import Piece
from Board import Board


class ChessVar:
    """
    Represents a ChessVar which has a game_board and game_state as
    private data members, as well as necessary get/set methods. Will
    eventually have private data member(s) which keep track of the
    pieces captured by each player. It currently interacts with the
    Board class and Piece class, but may interact with other classes by
    the end.
    """

    def __init__(self):
        """
        Initializes a ChessVar object with starting board, turn, and
        game state as private data members. Some way to keep track of
        captured pieces will be added later.
        """
        self._game_board_obj = Board()
        self._game_state = "UNFINISHED"
        self._white_captured_pieces = {}
        self._black_captured_pieces = {}
        print("\n --- Starting new game! --- \n")

    def get_game_state(self):
        """
        Get method which returns the current game state.
        """
        return self._game_state

    def set_game_state(self, game_state):
        """
        Set method which sets the game state.
        """
        self._game_state = game_state

    def get_white_captured_pieces(self):
        """
        Get method which returns the white captured pieces.
        """
        return self._white_captured_pieces

    def set_white_captured_pieces(self, piece_type):
        """
        Set method which sets the white captured pieces.
        """
        if piece_type not in self._white_captured_pieces:
            self._white_captured_pieces[piece_type] = 1
        else:
            self._white_captured_pieces[piece_type] += 1

    def get_black_captured_pieces(self):
        """
        Get method which returns the black captured pieces.
        """
        return self._black_captured_pieces

    def set_black_captured_pieces(self, piece_type):
        """
        Set method which sets the black captured pieces.
        """
        if piece_type not in self._black_captured_pieces:
            self._black_captured_pieces[piece_type] = 1
        else:
            self._black_captured_pieces[piece_type] += 1

    def get_move_coords(self, start_location, end_location):
        """
        Function which returns the coordinates of the move as
        a tuple of tuples.
        """
        return start_location, end_location

    def categorize_move(self, move_coords):
        """
        Function which categorizes (and returns as a tuple)
        the type of move by returning the bearing, directionality
        and length of the move based on start and end locations.
        """
        # Categorize according to:
        # 1) north, south, east or west
        if move_coords[0][0] > move_coords[1][0]:
            bearing = "NORTH"
        elif move_coords[0][0] < move_coords[1][0]:
            bearing = "SOUTH"
        elif move_coords[0][1] > move_coords[1][1]:
            bearing = "WEST"
        elif move_coords[0][1] < move_coords[1][1]:
            bearing = "EAST"
        else:
            bearing = None

        # 2) perpendicular or diagonal or L-shaped
        if (
            move_coords[0][1] == move_coords[1][1]
            or move_coords[0][0] == move_coords[1][0]
        ):
            directionality = "PERPENDICULAR"
        elif abs(move_coords[0][0] - move_coords[1][0]) == abs(
            move_coords[0][1] - move_coords[1][1]
        ):
            directionality = "DIAGONAL"
        else:
            directionality = "L-SHAPED"

        # 3) length of move
        if directionality == "PERPENDICULAR":
            length = abs(move_coords[0][0] - move_coords[1][0]) + abs(
                move_coords[0][1] - move_coords[1][1]
            )
        elif directionality == "DIAGONAL":
            length = abs(move_coords[0][0] - move_coords[1][0])
        else:
            length = None

        return bearing, directionality, length

    def is_move_unobstructed(self, piece_obj, directionality, length, move_coords):
        """
        Checks if proposed move is obstructed (or if same color piece at end location),
        thereby preventing move. Will return True if move is unobstructed, False otherwise.
        """
        # First checks what is at the end location (nothing, friend, or foe).
        # Then if directionality == "L-SHAPED", return True
        # Then cycle through coordinates on path from move_coords[0] to move_coords[1]
        # and if any are != "-", return False.

        # First check if friend, foe, or nothing at end location
        end_coords = move_coords[1]

        piece_at_end_location = self._game_board_obj.get_piece(end_coords)
        print(f"What is at end location? {piece_at_end_location}")

        # Get piece attributes
        if piece_at_end_location == 0:
            piece_at_end_location_color = None
            piece_at_end_location_type = None
        else:
            piece_at_end_location_color = piece_at_end_location.get_piece_color()
            piece_at_end_location_type = piece_at_end_location.get_piece_type()

        # 1. Friend at end location. Obstructed. Nothing captured.
        if piece_obj.get_piece_color() == piece_at_end_location_color:
            print("Error: There is a piece of the same color at the end location.")
            return False

        # 2. L-Shaped move.
        if length is None:
            # Nothing at end location. Unobstructed. Nothing captured.
            if piece_at_end_location_color is None:
                return True
            # Foe at end location. Unobstructed. Captured.
            else:
                print(
                    f"{piece_at_end_location_color} {piece_at_end_location_type}"
                    f" is at the end location; it will be captured."
                )
                # Capture piece
                if piece_at_end_location_color == "WHITE":
                    self.set_black_captured_pieces(piece_at_end_location_type)
                else:
                    self.set_white_captured_pieces(piece_at_end_location_type)
                return True

        # 3. Length == 1.
        if length == 1:
            # Nothing at end location. Unobstructed. Nothing captured.
            if piece_at_end_location_color is None:
                if piece_obj.get_piece_type() == "PAWN":
                    # Check if pawn is moving diagonally
                    if directionality == "DIAGONAL":
                        print("Error: PAWN cannot move diagonally unless capturing.")
                        return False
                    else:
                        return True
                else:
                    return True
            # Foe at end location. Unobstructed.
            else:
                # Check if PAWN is moving PERPENDICULAR - cannot capture
                if piece_obj.get_piece_type() == "PAWN":
                    if directionality == "PERPENDICULAR":
                        print("Error: PAWN cannot capture moving PERPENDICULAR.")
                        return False
                    else:
                        print(
                            f"{piece_at_end_location_color} {piece_at_end_location_type}"
                            f" is at the end location; it will be captured."
                        )
                        # Capture piece
                        if piece_at_end_location_color == "WHITE":
                            self.set_black_captured_pieces(piece_at_end_location_type)
                        else:
                            self.set_white_captured_pieces(piece_at_end_location_type)
                        return True
                else:
                    print(
                        f"{piece_at_end_location_color} {piece_at_end_location_type}"
                        f" is at the end location; it will be captured."
                    )
                    # Capture piece
                    if piece_at_end_location_color == "WHITE":
                        self.set_black_captured_pieces(piece_at_end_location_type)
                    else:
                        self.set_white_captured_pieces(piece_at_end_location_type)
                    return True

        # 4. Length > 1.
        if length > 1:
            # 1. Determine if range is positive or negative
            # 2. Exlude with slice the first coord (start location)
            # 3. Include end location
            # 4. Create dict of coords to traverse
            if move_coords[0][0] > move_coords[1][0]:
                y_coords = [
                    y for y in range(move_coords[0][0], move_coords[1][0] - 1, -1)
                ][1:]
            elif move_coords[0][0] < move_coords[1][0]:
                y_coords = [y for y in range(move_coords[0][0], move_coords[1][0] + 1)][
                    1:
                ]
            else:
                y_coords = [move_coords[0][0]]

            if move_coords[0][1] > move_coords[1][1]:
                x_coords = [
                    x for x in range(move_coords[0][1], move_coords[1][1] - 1, -1)
                ][1:]
            elif move_coords[0][1] < move_coords[1][1]:
                x_coords = [x for x in range(move_coords[0][1], move_coords[1][1] + 1)][
                    1:
                ]
            else:
                x_coords = [move_coords[0][1]]

            # Dict of coords
            if directionality == "DIAGONAL":
                coords_list = list(zip(y_coords, x_coords))

            elif directionality == "PERPENDICULAR":
                coords_list = [(y, x) for y in y_coords for x in x_coords]

            else:
                print(f"Error: {directionality} is not a valid directionality.")
                return False

            print(f"Coords list: {coords_list}")
            # Cycle through coords_dict and check if any are != "-"
            # Check last coord separately to determine if capture is necessary
            for coords in coords_list:
                # Are we at the end location?
                if coords == end_coords:
                    # Nothing at end location. Unobstructed. Nothing captured.
                    if piece_at_end_location_color is None:
                        return True
                    else:
                        # Check if PAWN moving PERPENDICULAR - cannot capture
                        if piece_obj.get_piece_type() == "PAWN":
                            if directionality == "PERPENDICULAR":
                                print(
                                    "Error: PAWN cannot capture moving PERPENDICULAR."
                                )
                                return False
                            else:
                                print(
                                    f"{piece_at_end_location_color} {piece_at_end_location_type}"
                                    f" is at the end location; it will be captured."
                                )
                                # Capture piece
                                if piece_at_end_location_color == "WHITE":
                                    self.set_black_captured_pieces(
                                        piece_at_end_location_type
                                    )
                                else:
                                    self.set_white_captured_pieces(
                                        piece_at_end_location_type
                                    )
                                return True
                        else:
                            print(
                                f"{piece_at_end_location_color} {piece_at_end_location_type}"
                                f" is at the end location; it will be captured."
                            )
                            # Capture piece
                            if piece_at_end_location_color == "WHITE":
                                self.set_black_captured_pieces(
                                    piece_at_end_location_type
                                )
                            else:
                                self.set_white_captured_pieces(
                                    piece_at_end_location_type
                                )
                            return True

                else:
                    if self._game_board_obj.get_piece(coords) != 0:
                        print("Error: There is a piece obstructing the move.")
                        return False

    def is_move_legal(
        self,
        piece_obj,
        bearing,
        directionality,
        length,
        move_coords,
    ):
        """
        Checks if move is legal according to is_move_sanctioned() from Piece class
        and is_move_unobstructed(). Will return True if move is legal,
        False otherwise.
        """
        # 1. Move is sanctioned within Chess rules
        move_sanctioned = piece_obj.is_move_sanctioned(
            bearing, directionality, length, move_coords
        )
        print(f"Is move sanctioned? {move_sanctioned}")

        # 2. Move is unobstructed
        move_unobstructed = self.is_move_unobstructed(
            piece_obj, directionality, length, move_coords
        )
        print(f"Is move unobstructed? {move_unobstructed}")

        if move_sanctioned and move_unobstructed:
            return True
        else:
            return False

    def is_game_won(self, captured_pieces_dict):
        """
        Cycles through captured pieces dictionary and checks if 2 knights,
        2 bishops, 2 rooks, 1 queen, 1 king, or 8 pawns have been
        captured. If so, returns True. Otherwise, returns False.
        """
        print(f"Captured pieces dictionary: {captured_pieces_dict}")
        win_dict = {
            "KNIGHT": 2,
            "BISHOP": 2,
            "ROOK": 2,
            "QUEEN": 1,
            "KING": 1,
            "PAWN": 8,
        }
        for piece_type, count in captured_pieces_dict.items():
            if count == win_dict[piece_type]:
                return True
            return False

    def make_move(self, start_location, end_location):
        """
        Takes two parameters: strings that represent the square
        moved from and the square moved to. If the square being
        moved from does not contain a piece belonging to the player
        whose turn it is, or if the indicated move is not legal, or
        if the game has already been won, then it returns False.
        Otherwise, it makes the indicated move, removes any captured
        piece, updates the game state if necessary, updates whose turn
        it is, and returns True.
        """
        # First check if game has been won
        if self._game_state != "UNFINISHED":
            print("Error: A move is not allowed; the game has already been won.")
            return False

        # If no piece at start location, return False
        if self._game_board_obj.get_piece(start_location) == 0:
            print("Error: There is no piece at the start location.")
            return False
        piece = self._game_board_obj.get_piece(start_location)

        # Next check if piece belongs to player whose turn it is
        # Whose turn is it?
        game_turn = self._game_board_obj.get_game_turn()
        print(f"It is {game_turn}'s turn.")

        # Get piece attributes
        piece_type = piece.get_piece_type()
        piece_color = piece.get_piece_color()

        print(f"The piece selected to move is: {piece_color} {piece_type}")

        if game_turn == "WHITE":
            if piece_color == "BLACK":
                print("Error: It's WHITE's turn and the selected piece is BLACK.")
                return False
        else:
            if piece_color == "WHITE":
                print("Error: It's BLACK's turn and the selected piece is WHITE.")
                return False

        # Get move coordinates
        move_coords = self.get_move_coords(start_location, end_location)
        print(f"Move coordinates: {move_coords}")

        # Categorize type of move
        bearing, directionality, length = self.categorize_move(move_coords)
        print(f"bearing, direction and length: {bearing, directionality, length}")

        # Check if the move is legal
        if self.is_move_legal(piece, bearing, directionality, length, move_coords):
            print(f"Moving {piece} from {start_location} to {end_location} is legal")
            return True
            # # Move piece and update board
            # self._game_board_obj.set_piece(start_location, end_location, piece)
        else:
            print("Move is either not sanctioned or obstructed!")
            return False
