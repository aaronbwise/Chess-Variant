
# Chess Variant Game

## Overview
This project implements a variant of the traditional chess game. Developed in Python, it utilizes Pygame for a graphical representation, enhancing the player's interactive experience. The goal is to be the first player to capture all of an opponent's pieces of one type (e.g., all knights, all pawns, etc.).

![alt text](https://github.com/aaronbwise/Chess-Variant/blob/main/board.jpg)

## Features
- **Graphical User Interface**: Utilizes Pygame for a smooth and visually appealing gaming experience.
- **Chess Mechanics**: Implements standard chess rules with an additional unique winning condition.
- **Interactive Gameplay**: Players interact with the game using mouse clicks, making it user-friendly and accessible.

## Installation
To run this game, you need to have Python and Pygame installed. Follow these steps to set it up:

1. Clone the repository:
   ```
   git clone https://github.com/aaronbwise/Chess-Variant.git
   ```
2. Navigate to the cloned directory.

3. Install Pygame (if not already installed):
   ```
   pip install pygame
   ```

4. Run the game:
   ```
   python game.py
   ```

## Usage
After starting the game, players take turns moving their pieces according to standard chess rules. The game tracks the captured pieces, and the first player to capture all of an opponent's specific type of pieces wins.

## Code Structure
- `Board.py`: Defines the Board class, handling the chessboard setup and piece placement.
- `Piece.py`: Contains definitions for different chess pieces and integrates Pygame for rendering.
- `ChessVar.py`: Manages the game's state, rules, and interactions between pieces and the board.
- `game.py`: Main game loop handling user interactions and game window rendering.

## Contributions
This project was created as a final project. Contributions, bug reports, and suggestions are welcome. Please feel free to fork this repository and submit pull requests.


