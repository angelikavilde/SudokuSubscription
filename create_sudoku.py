import numpy as np
import random
from sudoku_solver import check_all_conditions, get_position, count_x, solve_sudoku


if __name__ == "__main__":
    sudoku = np.full((9, 9), 'x', dtype='object')
    difficulty = 30
    x = 0
    a = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2), (1, 2), (2, 1), (3, 3),
         (4, 4), (5, 5), (4, 5), (5, 4), (4, 3), (3, 4), (3, 5), (5, 3), (2, 0),
         (0, 2), (6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    random.shuffle(a)
    b = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2), (1, 2), (2, 1), (3, 3),
         (4, 4), (5, 5), (4, 5), (5, 4), (4, 3), (3, 4), (3, 5), (5, 3), (2, 0),
         (0, 2), (6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    while x < 81:  # count_x(sudoku) > 81 - difficulty:
        if len(a) == 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            print("yes")
            if (i, j) in b:
                continue
        else:
            i, j = a[-1]
        if sudoku[i, j] != 'x':
            # print(i, j, sudoku[i, j])
            continue
        value = random.randint(1, 9)
        row = sudoku[i, :]
        # print("value", value, "i,j", (i, j))
        column = sudoku[:, j]
        i_start_pos = get_position(i)
        j_start_pos = get_position(j)
        # if (i_start_pos + j_start_pos) % 2 == 1:
        #     continue
        box = sudoku[i_start_pos: i_start_pos + 3,
                     j_start_pos: j_start_pos + 3]
        # print(f"check {value} isn't in those", check_all_conditions(row, column, box, value),
        #       row, column, box, "end")
        if check_all_conditions(row, column, box, value):
            sudoku[i, j] = value
            if a:
                a.pop()
            print("count", count_x(sudoku))
            x += 1
        copy_sudoku = sudoku.copy()
        if solve_sudoku(copy_sudoku):
            print(f"worked in {x}")
            break
        # print(count_x(sudoku), (i, j), value)
        # print()
    print(sudoku)
    print(solve_sudoku(sudoku))

# (6, 6), (6, 7), (6, 8),
# (7, 6), (7, 7), (7, 8),
# (8, 6), (8, 7), (8, 8)

# (0, 6), (1, 6), (2, 6),
# (0, 7), (1, 7), (2, 7),
# (0, 8), (1, 8), (2, 8)

# (6, 0), (6, 1), (6, 2),
# (7, 0), (7, 1), (7, 2),
# (8, 0), (8, 1), (8, 2)
