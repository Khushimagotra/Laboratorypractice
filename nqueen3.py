def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if a queen can be placed at the given position
        for i in range(row):
            if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
                return False
        return True

    def place_queen(board, row):
        # Base case: All queens are placed
        if row == n:
            return True
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if place_queen(board, row + 1):
                    return True
        return False

    board = [-1] * n
    if place_queen(board, 0):
        return board
    else:
        return None

n = int(input("Enter the value of N: "))
solution = solve_n_queens(n)
if solution:
    print("Solution found:")
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
else:
    print("No solution found.")