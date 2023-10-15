"""A sudoku solver to double check that the sudokus we create are valid"""

import numpy as np


def check_box(box: np.ndarray, value: int) -> bool:
    """Checks that the value is available for that three by three box"""
    return all(value not in row for row in box)


def check_line(line: np.ndarray, value: int) -> bool:
    """Checks that the value is available for that row/column"""
    return not value in line


def check_all_conditions(row: np.ndarray, column: np.ndarray, box: np.ndarray, value: int) -> bool:
    """Checks that all 3 checks are valid"""
    return all([check_line(row, value),
                check_line(column, value),
                check_box(box, value)])


def get_position(x: int) -> int:
    """Returns starting position for the box"""
    return (x // 3) * 3


def go_through_sudoku(sudoku: np.ndarray) -> np.ndarray:
    """
    Runs through the sudoku and
    enters any valid numbers for that run through
    """
    for i in range(9):
        for j in range(9):
            possible_values = set()
            if isinstance(sudoku[i, j], str):
                if len(sudoku[i, j]) > 1:
                    values_to_check = {int(n) for n in sudoku[i, j][1:]}
                else:
                    values_to_check = range(1, 10)
                for possible_value in values_to_check:
                    row = sudoku[i, :]
                    column = sudoku[:, j]
                    i_start_pos = get_position(i)
                    j_start_pos = get_position(j)
                    box = sudoku[i_start_pos: i_start_pos + 3,
                                 j_start_pos: j_start_pos + 3]
                    if check_all_conditions(row, column, box, possible_value):
                        possible_values.add(str(possible_value))
                if len(possible_values) == 1:
                    sudoku[i, j] = int(possible_values.pop())
                else:
                    sudoku[i, j] = "x" + "".join(possible_values)
    return sudoku


def count_x(sudoku: np.ndarray) -> int:
    """Returns the count of "x" in numpy matrix"""
    flat_array = sudoku.flatten()
    unfilled_count_by_arr = np.char.count(flat_array.astype(str), "x")
    return sum(unfilled_count_by_arr)


def solve_sudoku(sudoku: np.ndarray) -> bool:
    """Returns true/false whether sudoku can be solved"""
    unfilled_count_after: int = True
    while unfilled_count_after:
        unfilled_count_before = count_x(sudoku)
        sudoku = go_through_sudoku(sudoku)
        unfilled_count_after = count_x(sudoku)
        if unfilled_count_before == unfilled_count_after:  # ! TODO: Could we assume that
            # there could be a case where this will break? DISCUSSION
            break
    return not unfilled_count_after


if __name__ == "__main__":
    test_sudoku = np.array([["x", "x", 4, "x", 5, "x", "x", "x", "x"],
                            [9, "x", "x", 7, 3, 4, 6, "x", "x"],
                            ["x", "x", 3, "x", 2, 1, "x", 4, 9],
                            ["x", 3, 5, "x", 9, "x", 4, 8, "x"],
                            ["x", 9, "x", "x", "x", "x", "x", 3, "x"],
                            ["x", 7, 6, "x", 1, "x", 9, 2, "x"],
                            [3, 1, "x", 9, 7, "x", 2, "x", "x"],
                            ["x", "x", 9, 1, 8, 2, "x", "x", 3],
                            ["x", "x", "x", "x", 6, "x", 1, "x", "x"]], dtype="object")
    print(solve_sudoku(test_sudoku))
