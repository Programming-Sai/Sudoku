
# Sudoku Game

Welcome to the Sudoku game implemented in Python. This project includes a Sudoku board generator and a game interface that allows users to play Sudoku, validate moves, and see possible moves for each cell.


## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Programming-Sai/Sudoku.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Sudoku
   ```
3. Run the game:
   ```sh
   python Sudoku_Game.py
   ```


## Features

- **Board Generation**: Automatically generates a complete and valid Sudoku board.
- **Puzzle Creation**: Creates a playable Sudoku puzzle by removing random numbers from the completed board.
- **User Interaction**: Allows users to input values, see possible moves, and validate their moves.
- **Game Validation**: Checks for duplicate values in rows, columns, and subgrids to ensure the board remains valid.
- **Help Option**: Provides instructions and rules for the game.

## Files

- `Sudoku_Board.py`: Contains the `Board` class, which defines all methods related to board generation, cell value validation, and board display.
- `Sudoku_Player.py`: Contains the `Player` class, which defines methods for user input, move validation, and game interactions.
- `Sudoku_Game.py`: The main game file that brings together the board and player classes to implement the Sudoku game.
- `Game.txt`: Contains the game instructions and rules.
- `__pycache__`: A directory created by Python to store compiled bytecode files.

## How to Play

1. **Run the Game**:
   - Execute the `Sudoku_Game.py` file to start the game.
   - You will see an initial board with some cells marked as '.' to indicate an empty cell.

2. **Game Options**:
   - Select `1` for Help: Displays the game rules and instructions.
   - Select `2` for New Game: Starts a new Sudoku game with a randomly generated puzzle.

3. **User Input**:
   - Enter your moves in the format `column-row-action` (e.g., `a1e` to enter a value in cell (A, 1)).
   - Actions:
     - `e`: Enter a value.
     - `s`: Show possible moves for the selected cell.

4. **Move Validation**:
   - The game will validate your move and inform you if it causes any clashes.
   - You have 10 lives to complete the puzzle. Each invalid move reduces your lives.

5. **Winning the Game**:
   - Complete the puzzle without any errors to win the game.

## Classes and Methods

### `Board` Class

- `__init__()`: Initializes an empty board and its numbers.
- `is_duplicate_in_list(list)`: Checks for duplicates in a list.
- `find(board, list, target)`: Searches for an element in the board.
- `get_row(row, col)`: Gets the entire row for a given cell.
- `get_col(row, col)`: Gets the entire column for a given cell.
- `get_block(row, col)`: Gets the entire block for a given cell.
- `is_valid(row, col, num, board)`: Validates the cell value.
- `clashes(row, col, board)`: Checks for clashes and their locations.
- `solution_board()`: Generates a complete Sudoku board.
- `puzzle_board(board)`: Generates a puzzle board by removing numbers.
- `is_board_complete(board)`: Checks if the board is complete.
- `possible_moves(row, col, board)`: Returns possible values for a cell.
- `display_board(board_1)`: Displays the board to the user.

### `Player` Class

- `__init__(board)`: Initializes the Board class.
- `user_input()`: Receives and validates user input.
- `show_possible_moves(row, col, board_2)`: Shows possible moves for a cell.
- `enter_value(row, col, board_1, board_2, lives)`: Allows user to enter values and checks for validity.
- `help()`: Displays the game rules and instructions.
