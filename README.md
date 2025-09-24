# Gomoku AI in Python

## Project Overview
This is a Python implementation of **Gomoku** (Five in a Row) with a simple AI opponent. The program tracks sequences of stones, evaluates the board, suggests optimal moves, and allows interactive gameplay between the user and computer.

## Features
- Detects **open** and **semi-open** sequences for both players.
- Evaluates the board using a scoring system to choose the best move for AI.
- Checks for **wins**, **draws**, or continuation.
- Interactive gameplay: User vs Computer.
- Functions for analysis and testing of core mechanics.
- Board printing in a clear, formatted layout.

## Key Functions
- `make_empty_board(sz)`: Creates an empty board of given size.
- `detect_row()`, `detect_rows()`: Identify sequences of stones.
- `is_bounded()`: Determines if sequences are open, semi-open, or closed.
- `search_max()`: Chooses the best AI move.
- `score()`: Evaluates board state numerically.
- `is_win()`: Checks if game is over.
- `play_gomoku(board_size)`: Main interactive game loop.

