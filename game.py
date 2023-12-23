import pygame
from pathlib import Path
from ChessVar import ChessVar


WIDTH, HEIGHT = 600, 600
RECT = (0, 0, 600, 600)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Variant Game")

# Board image
img_dir = Path(__file__).parent / "img"
board_img = pygame.transform.scale(
    pygame.image.load(img_dir / "board.png"), (WIDTH, HEIGHT)
)


def redraw_window(win, board_obj):
    win.blit(board_img, (0, 0))
    board_obj.draw(win)
    pygame.display.update()


def click(pos):
    """
    Returns the (row, col) of the square clicked on.
    """
    x = pos[0]
    y = pos[1]

    if RECT[0] < x < RECT[0] + RECT[2]:
        if RECT[1] < y < RECT[1] + RECT[3]:
            # Click is within board
            row = int((y - RECT[1]) / (RECT[3] / 8))
            col = int((x - RECT[0]) / (RECT[2] / 8))
            return row, col


def main():
    game = ChessVar()
    board_obj = game._game_board_obj

    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(10)
        redraw_window(win, board_obj)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos1 = pygame.mouse.get_pos()
                row1, col1 = click(pos1)

                if (
                    row1 is not None and col1 is not None
                ):  # Check if the click is within the board
                    board_obj.select(row1, col1)
                    piece = board_obj.get_piece((row1, col1))

            if event.type == pygame.MOUSEBUTTONUP:
                pos2 = pygame.mouse.get_pos()
                row2, col2 = click(pos2)

                move_legal = game.make_move((row1, col1), (row2, col2))

                if move_legal:
                    board_obj.set_piece((row1, col1), (row2, col2), piece)
                    # Check if game has been won with current move
                    # If so, update game state to reflect that the game has been won
                    if piece.get_piece_color() == "WHITE":
                        if game.is_game_won(game._white_captured_pieces):
                            game.set_game_state("WHITE_WON")
                            print("WHITE has won!")
                    else:
                        if game.is_game_won(game._black_captured_pieces):
                            game.set_game_state("BLACK_WON")
                            print("BLACK has won!")

                    # Update game turn
                    if game.get_game_state() == "UNFINISHED":
                        print("Game has not been won yet.")
                        if board_obj.get_game_turn() == "WHITE":
                            print("Updating game turn to BLACK")
                            board_obj.set_game_turn("BLACK")
                        else:
                            print("Updating game turn to WHITE")
                            board_obj.set_game_turn("WHITE")
                else:
                    print("Invalid move.")


if __name__ == "__main__":
    main()
