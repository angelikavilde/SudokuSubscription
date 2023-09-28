""""""

import numpy as np


test_sudoku = np.array([["x", "x", 4, "x", 5, "x", "x", "x", "x"],
                        [9, "x", "x", 7, 3, 4, 6, "x", "x"],
                        ["x", "x", 3, "x", 2, 1, "x", 4, 9],
                        ["x", 3, 5, "x", 9, "x", 4, 8, "x"],
                        ["x", 9, "x", "x", "x", "x", "x", 3, "x"],
                        ["x", 7, 6, "x", 1, "x", 9, 2, "x"],
                        [3, 1, "x", 9, 7, "x", 2, "x", "x"],
                        ["x", "x", 9, 1, 8, 2, "x", "x", 3],
                        ["x", "x", "x", "x", 6, "x", 1, "x", "x"]], dtype='object')


def check_box(box: np.array, value: int) -> bool:
    """Checks that the value is available for that three by three box"""
    return all(value not in row for row in box)  # TODO verify


def check_line(line: np.array, value: int) -> bool:
    """Checks that the value is available for that row/column"""
    return not value in line


def check_all_conditions(row: np.array, column: np.array, box: np.array, value: int) -> bool:
    """Checks that all 3 checks are valid"""
    return all([check_line(row, value),
                check_line(column, value),
                check_box(box, value)])


def get_position(x: int) -> int:
    """Returns starting position for the box"""
    return (x // 3) * 3


if __name__ == "__main__":
    fake = np.empty((9, 9))
    "for every 1-9, check every row"
    loop = True
    while loop:
        loop = False
        # print(test_sudoku)
        print(fake)
        print()
        for i in range(9):
            for j in range(9):
                possible_values = []
                if test_sudoku[i, j] == "x":
                    for possible_value in range(1, 10):
                        row = test_sudoku[i, :]
                        column = test_sudoku[:, j]
                        i_start_pos = get_position(i)
                        j_start_pos = get_position(j)
                        box = test_sudoku[i_start_pos: i_start_pos +
                                          3, j_start_pos: j_start_pos + 3]
                        if check_all_conditions(row, column, box, possible_value):
                            possible_values.append(possible_value)
                    if len(possible_values) == 1:
                        # fake[i, j] = possible_values[0]
                        test_sudoku[i, j] = possible_values[0]
                    else:
                        loop = True

        # print(fake)
        print(test_sudoku)
