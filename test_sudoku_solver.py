"""File to verify that sudoku solver works as expected"""

import numpy as np

from sudoku_solver import check_box, check_line


def test_check_box():
    """
    Verifies that numpy matrix is
    returning bool whether it can or not add
    the value in following the sudoku rules
    """
    box = np.array([[2, 4], [1, 9]], dtype="object")
    assert not check_box(box, 1)
    assert check_box(box, 8)


def test_check_line():
    """
    Verifies that function returns correct
    bool value based on whether a number can
    be placed into the array
    """
    line = np.array([1, 2, "x"], dtype="object")
    assert check_line(line, 5)
    assert not check_line(line, 2)