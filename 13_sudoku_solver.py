def print_board(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ". join(str(cell) for cell in row))

def find_empty_location(board):
    """Find an empty location on the board."""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 0:
                return i, j
    return None

def is_valid(board, row, col, num):
    """Check if a number is valid in the given cell."""
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True        

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # Solved

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Reset on backtrack

    return False


sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku puzzle solved successfully!")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")