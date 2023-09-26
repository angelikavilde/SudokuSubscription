""""""

# x x 4 x 5 x x x x
# 9 x x 7 3 4 6 x x
# x x 3 x 2 1 x 4 9
# x 3 5 x 9 x 4 8 x
# x 9 x x x x x 3 x
# x 7 6 x 1 x 9 2 x
# 3 1 x 9 7 x 2 x x
# x x 9 1 8 2 x x 3
# x x x x 6 x 1 x x

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
    return True


def check_line(line: np.array, value: int) -> bool:
    """Checks that the value is available for that row/column"""
    return not value in line


def check_all_conditions(row: np.array, column: np.array, box: np.array, value: int):
    """Checks that all 3 checks are valid"""
    return all([check_line(row, value), check_line(column, value),
               check_box(box, value)])


def get_position(x):
    result = (x // 3) * 3
    return [result, result + 1,  result + 2]


if __name__ == "__main__":
    fake = np.empty((9, 9))
    "for every 1-9, check every row"
    for i in range(9):
        for j in range(9):
            for k in range(1, 10):
                if test_sudoku[i, j-1] == "x":
                    row = test_sudoku[i, :]
                    column = test_sudoku[:, j]
                    coordinates = (get_position(i), get_position(j))
                    print(
                        check_line(row, k), row, i, j, k)
                    check_line(column, k)
                    # check box
                else:
                    pass
