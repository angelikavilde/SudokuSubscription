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


def check_three_by_three(box: np.array, value: int) -> bool:
    """Checks that the value is available for that three by three box"""
    pass


def check_row(row: np.array, value: int) -> bool:
    """Checks that the value is available for that row"""
    return not value in row


def check_column(column: np.array, value: int) -> bool:
    """Checks that the value is available for that column"""
    pass


if __name__ == "__main__":
    fake = np.empty((9, 9))
    "for every 1-9, check every row"
    for i in range(1, 2):
        for j in range(1, 2):
            for k in range(1, 10):
                if test_sudoku[i-1, j-1] == "x":
                    print(
                        check_row(test_sudoku[i-1, :], k), test_sudoku[i-1, :], i, j, k)
                    # check col
                    # check box
                else:
                    pass
