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


def backtrack_last_step(sudoku_grid: np.ndarray, step_record: dict, do_not_try_dict: dict):
    """"""
    last_coordinate = step_record["coordinates"][-1]
    last_value = step_record["values"][-1]
    step_record["coordinates"].pop()
    step_record["values"].pop()
    sudoku_grid[last_coordinate[0],last_coordinate[1]] = "x"
    if do_not_try_dict[str(last_coordinate)]:
        do_not_try_dict[str(last_coordinate)].append(last_value)
    else:
        do_not_try_dict[str(last_coordinate)] = [last_value]
    return sudoku_grid, step_record, do_not_try_dict, last_value, last_coordinate

def create_sudoku():
    """"""
    sudoku = np.full((9, 9), 'x', dtype='object')
    a = list(i for i in range(1,10))
    b = list(i for i in range(0,9))

    # random.shuffle(a); random.shuffle(b)
    step_record = {}
    step_record["values"] = []
    step_record["coordinates"] = []

    box_start_positions = [(0,0), (0,3), (3,0), (3,3), (0,6), (6,0), (6,6), (6,3), (3,6)]
    failed_placements_dict = {}

    for i in a:
    # i is the value we place
        for j in b:
            # every j is the new box we place it in
            i_start_pos = box_start_positions[j][0]
            j_start_pos = box_start_positions[j][1]
            box_info_and_fill(j_start_pos, a, i_start_pos, failed_placements_dict, step_record, sudoku)

def fill_box(step_record, sudoku, i_start_pos, j_start_pos, box, value):
    a = 
    for k in a:
        column_n = (k % 3) - 1 + (i_start_pos // 3)
        # k%3 is column n within box, -1 is for index start, box start pos//3
        # is to add column n value if the box is not in 1st region
        row_n = (k % 3) - 1 + (j_start_pos // 3)
        cell = sudoku[row_n, column_n]
        row = sudoku[row_n, :]
        column = sudoku[:, column_n]

        if cell == "x":
            # for time improvement only attempt non x cells + that would alter
            # cells_attempted_within_box count dependency to re-do the step
            continue

        if check_all_conditions(row, column, box, value):
            sudoku[row_n, column_n] = value
            step_record["values"].append(value)
            step_record["coordinates"].append((row_n, column_n))
            value_added_this_box = True
            break
    return value_added_this_box, sudoku, step_record


def box_info_and_fill(j_start_pos, i_start_pos, failed_placements_dict, step_record, sudoku):
    # j is box number
    # i is value adding
    a = list(i for i in range(1,10))
    box = sudoku[i_start_pos: i_start_pos + 3,
                j_start_pos: j_start_pos + 3]
    value_added_this_box = False
    value_added_this_box, sudoku, step_record = \
        fill_box(a, step_record, sudoku, i_start_pos, j_start_pos, box, i)
    if not value_added_this_box:
        # this means one of the previous steps has gone wrong
        sudoku, step_record, failed_placements_dict, re_try_val, last_failed_coord = \
        backtrack_last_step(sudoku, step_record, failed_placements_dict)
        i_start_pos = get_position(last_failed_coord[0])
        j_start_pos = get_position(last_failed_coord[1])
        box_info_and_fill()

if __name__ == "__main__":
    create_sudoku()