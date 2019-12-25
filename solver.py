board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]]


def complete_grid(brd):
    find = find_empty(brd)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if check_valid(brd, i, (row, col)):
            brd[row][col] = i

            if complete_grid(brd):
                return True

            brd[row][col] = 0

    return False


def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if board[i][j] == 0:
                return i, j  # row, col

    return None


def check_valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for j in range(len(brd)):
        if brd[j][pos[1]] == num and pos[0] != j:
            return False

    # Check brdx
    brdx_x = pos[1] // 3
    brdx_y = pos[0] // 3

    for i in range(brdx_y * 3, brdx_y * 3 + 3):
        for j in range(brdx_x * 3, brdx_x * 3 + 3):
            if brd[i][j] == num and (i, j) != pos:  # i != pos[1] and j != pos[0]
                return False

    return True


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
