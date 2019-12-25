import numpy as np
import random as rand


def create_random_solve_board():
    b = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    permute_section(b)
    complete_grid(b)

    return b


def remove_numbers(brd):
    all_pos = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
               (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
               (2, 0), (0, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
               (3, 0), (0, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
               (4, 0), (0, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
               (5, 0), (0, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
               (6, 0), (0, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
               (7, 0), (0, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
               (8, 0), (0, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]

    np.random.shuffle(all_pos)

    for i in range(81):
        pos = all_pos[i]
        placeholder = brd[pos[0]][pos[1]]
        brd[pos[0]][pos[1]] = 0

        if len(get_possibilities(brd, (pos[0], pos[1]))) > 1:
            brd[pos[0]][pos[1]] = placeholder


def get_possibilities(brd, pos):
    total = list()

    for i in range(1,10):
        if check_valid(brd, i, pos):
            total.append(i)

    return total


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
            if brd[i][j] == 0:
                return i, j  # row, col

    return None


def permute_section(brd):
    section = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sec_1 = np.random.permutation(section)
    sec_2 = np.random.permutation(section)
    sec_3 = np.random.permutation(section)

    complete_sections(brd, sec_1, 0, 0)
    complete_sections(brd, sec_2, 3, 3)
    complete_sections(brd, sec_3, 6, 6)


def complete_sections(brd, sec, counter, disp):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            counter += 1
        brd[counter][i % 3 + disp] = sec[i]


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

newboard = create_random_solve_board()
print_board(newboard)
remove_numbers(newboard)
print("----------------------------------------------------------")
print_board(newboard)
