def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_8_queens(board, row, solutions):
    # If all queens are placed
    if row == 8:
        solutions.append(board[:])
        return
    
    # Try placing the queen in all columns of the current row
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # Place the queen
            solve_8_queens(board, row + 1, solutions)  # Recur to place the next queen
            board[row] = -1  # Backtrack and remove the queen

def print_solution(board):
    """Helper function to print a solution in a readable format."""
    for row in board:
        line = ['Q' if i == row else '.' for i in range(8)]
        print(' '.join(line))
    print()

def solve():
    board = [-1] * 8  # Initialize the board, -1 means no queen placed
    solutions = []
    solve_8_queens(board, 0, solutions)

    # Print all solutions
    print(f"Total solutions: {len(solutions)}\n")
    for solution in solutions:
        print_solution(solution)

# Run the solution
solve()
