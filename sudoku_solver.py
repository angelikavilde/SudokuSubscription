"""A sudoku solver to double check that the sodokus we create are valid"""

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


def go_through_sudoku(sudoku: np.array) -> np.array:
    """
    Runs through the sudoku and
    enters any valid numbers for that run through
    """
    for i in range(9):
        for j in range(9):
            possible_values = []
            if sudoku[i, j] == "x":
                for possible_value in range(1, 10):
                    row = sudoku[i, :]
                    column = sudoku[:, j]
                    i_start_pos = get_position(i)
                    j_start_pos = get_position(j)
                    box = sudoku[i_start_pos: i_start_pos +
                                 3, j_start_pos: j_start_pos + 3]
                    if check_all_conditions(row, column, box, possible_value):
                        possible_values.append(possible_value)
                if len(possible_values) == 1:
                    sudoku[i, j] = possible_values[0]
    print(sudoku)
    return sudoku


def solve_sudoku(sudoku: np.array) -> bool:
    is_not_complete = True
    while is_not_complete:
        sudoku_pre_count = np.count_nonzero(sudoku == 'x')
        print(sudoku_pre_count)
        sudoku = go_through_sudoku(sudoku)
        sudoku_after_count = np.count_nonzero(sudoku == 'x')
        print(sudoku_after_count)
        if sudoku_pre_count == sudoku_after_count:
            return False
        if 'x' not in sudoku:
            return True
    return False


if __name__ == "__main__":
    print(solve_sudoku(test_sudoku))
