"""File to verify that sudoku solver works as expected"""

import numpy as np

from sudoku_solver import check_box


def test_check_box():
    """
    Verifies that numpy matrix is
    returning bool whether it can or not add
    the value in following the sudoku rules
    """
    box = np.array([[2,4],[1,9]])
    assert not check_box(box, 1)
    assert check_box(box, 8)