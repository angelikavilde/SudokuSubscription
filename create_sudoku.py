import numpy as np
import random
from sudoku_solver import check_all_conditions, get_position, count_x, solve_sudoku

# a = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2), (1, 2), (2, 1), (3, 3),
    #      (4, 4), (5, 5), (4, 5), (5, 4), (4, 3), (3, 4), (3, 5), (5, 3), (2, 0),
    #      (0, 2), (6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    # random.shuffle(a)
    # b = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2), (1, 2), (2, 1), (3, 3),
    #      (4, 4), (5, 5), (4, 5), (5, 4), (4, 3), (3, 4), (3, 5), (5, 3), (2, 0),
    #      (0, 2), (6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    # while x < 81:  # count_x(sudoku) > 81 - difficulty:
    #     if len(a) == 0:
    #         i = random.randint(0, 8)
    #         j = random.randint(0, 8)
    #         print("yes")
    #         if (i, j) in b:
    #             continue
    #     else:
    #         i, j = a[-1]
    #     if sudoku[i, j] != 'x':
    #         # print(i, j, sudoku[i, j])
    #         continue
    #     value = random.randint(1, 9)
    #     row = sudoku[i, :]
    #     # print("value", value, "i,j", (i, j))
    #     column = sudoku[:, j]
    #     i_start_pos = get_position(i)
    #     j_start_pos = get_position(j)
    #     # if (i_start_pos + j_start_pos) % 2 == 1:
    #     #     continue
    #     box = sudoku[i_start_pos: i_start_pos + 3,
    #                  j_start_pos: j_start_pos + 3]
    #     # print(f"check {value} isn't in those", check_all_conditions(row, column, box, value),
    #     #       row, column, box, "end")
    #     if check_all_conditions(row, column, box, value):
    #         sudoku[i, j] = value
    #         if a:
    #             a.pop()
    #         print("count", count_x(sudoku))
    #         x += 1
    #     copy_sudoku = sudoku.copy()
    #     if solve_sudoku(copy_sudoku):
    #         print(f"worked in {x}")
    #         break
    #     # print(count_x(sudoku), (i, j), value)
    #     # print()
    # print(sudoku)
    # print(solve_sudoku(sudoku))

# (6, 6), (6, 7), (6, 8),
# (7, 6), (7, 7), (7, 8),
# (8, 6), (8, 7), (8, 8)

# (0, 6), (1, 6), (2, 6),
# (0, 7), (1, 7), (2, 7),
# (0, 8), (1, 8), (2, 8)

# (6, 0), (6, 1), (6, 2),
# (7, 0), (7, 1), (7, 2),
# (8, 0), (8, 1), (8, 2)


if __name__ == "__main__":
    sudoku = np.full((9, 9), 'x', dtype='object')
    a = list(i for i in range(1,10))
    b = list(i for i in range(0,9))
    print(sudoku)
    # c = b.copy()
    random.shuffle(a); random.shuffle(b)
    step_record = {}
    backtracked = {"step": [], "coordinate_failed": []}
    # x|x|x
    # x|x|x
    # x|x|x
    step_count = 0
    box_start_positions = [(0,0), (0,3), (3,0), (3,3), (0,6), (6,0), (6,6), (6,3), (3,6)]
    for i in a:
        # i is the value we place -- no need to change
        for j in b:
            # every j is the new box we place it in
            i_start_pos = box_start_positions[j][0]
            j_start_pos = box_start_positions[j][1]
            box = sudoku[i_start_pos: i_start_pos + 3,
                     j_start_pos: j_start_pos + 3]
            value_added_this_box = False
            for k in a:
                column_n = (k % 3) - 1 + (i_start_pos // 3)
                # k%3 is column n within box, -1 is for index start, box start pos//3
                # is to add column n value if the box is not in 1st region
                row_n = (k % 3) - 1 + (i_start_pos // 3)
                cell = sudoku[row_n, column_n]
                row = sudoku[row_n, :]
                column = sudoku[:, column_n]

                if cell == "x":
                    # for time improvement only attempt non x cells + that would alter
                    # cells_attempted_within_box count dependency to re-do the step
                    continue

                if check_all_conditions(row, column, box, i):
                    sudoku[row_n, column_n] = i
                    step_count += 1
                    step_record[f"step{step_count}"] = {f"{i}" : (row_n, column_n)}
                    step_record["latest_step"] = step_count
                    value_added_this_box = True
                    break

            if not value_added_this_box:
                # this means one of the previous steps has gone wrong
                backtrack_last_step()

    