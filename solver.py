board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]]


# Solves a board for one possible solution using backtracking
def complete_grid(brd):
    find = find_empty(brd)

    if not find:  # If no empty blocks exists the board has been completed
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if check_valid(brd, i, (row, col)):
            brd[row][col] = i

            if complete_grid(brd):  # Recursive call on the next empty grid
                return True

            brd[row][col] = 0  # Backtrack if first attempted number does not work, recheck with next value

    return False  # Board cannot be solved


# Finds the next empty square in a sudoku puzzle (marked by 0) and returns its position
def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return i, j  # row, col

    return None


# Determines if placing the given number in the given position is a valid placement
def check_valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for j in range(len(brd)):
        if brd[j][pos[1]] == num and pos[0] != j:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if brd[i][j] == num and (i, j) != pos:  # i != pos[1] and j != pos[0]
                return False

    return True


# Prints a board with horizontal and vertical lines for display
def print_board(brd):
    for i in range(len(brd)):

        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(brd[0])):

            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")


print_board(board)
complete_grid(board)
print("Solved Version:")
print_board(board)
