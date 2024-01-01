"""File to create a fully filled sudoku grid"""

import numpy as np

from sudoku_solver import check_all_conditions, get_position


def log_and_remove_error(success_coords: dict, previous_fails: dict):
    """Logs and removesa the error coordinate and the value to later change"""
    # something went wrong (red oval on diagram)

    # removing last logged success
    last_invalid_coords = success_coords["coordinates"].pop()
    last_invalid_value = success_coords["values"].pop()

    # saving last logged success as a fail
    previous_fails["coordinates"].append(last_invalid_coords)
    previous_fails["values"].append(last_invalid_value)

    # replace wrong coordinate back with x
    sudoku[last_invalid_coords[0], last_invalid_coords[1]] = 'x'
    # print(sudoku)

    cell = 1
    box_n = find_box_and_cell(last_invalid_coords[0], last_invalid_coords[1])
    value = last_invalid_value
    # print("here",box_n, cell, value, previous_fails, success_coords)
    # print(cell)
    # fill_the_grid(box_n, cell, value, previous_fails, success_coords)
    return value, box_n, cell, previous_fails, success_coords


def find_box_and_cell(row, column) -> int:
    """Finds the box and the cell number of the provided coords"""
    # Determine the box number
    box_x = row // 3 + 1
    box_y = column // 3 + 1

    box_number = (box_x - 1) * 3 + box_y

    # Determine the cell number within the box
    # cell_x = row % 3
    # cell_y = column % 3
    # cell_number_within_box = cell_x * 3 + cell_y + 1

    return box_number#, cell_number_within_box


def check_if_already_failed_coords(coords: tuple, value: int, previous_fails: dict) -> bool: #!Change name to more approp
    """Returns True if value is NOT in previously failed coordinates"""
    coord_failed_for_indexes = {indx for indx, fail
            in enumerate(previous_fails["coordinates"]) if coords == fail}
    values_coord_failed_for = {previous_fails["values"][indx] for indx in coord_failed_for_indexes}
    return value not in values_coord_failed_for


def find_cell_coords(box_n: int, cell: int) -> tuple:
    """Returns the coordinates of the cell provided with cell n in the box n"""
    box_row = (box_n - 1) // 3
    box_col = (box_n - 1) % 3
    column = (cell - 1) % 3 + box_col * 3
    row = (cell - 1) // 3 + box_row * 3
    return row, column


def get_sudoku_partial_arrays(row_n: int, column_n: int) -> tuple:
    """Returns row, column and box of the sudoku"""
    row = sudoku[row_n, :]
    column = sudoku[:, column_n]
    # if (row_n, column_n) == (1,6):
    #     print("coords: ", row_n,column_n)
    #     print(sudoku)
    #     print(f"column: {column}")
    #     print(f"row: {row}")
    i_start_pos = get_position(row_n)
    j_start_pos = get_position(column_n)
    box = sudoku[i_start_pos: i_start_pos + 3,
                    j_start_pos: j_start_pos + 3]
    return row, column, box

#repeated step 2:
def fill_the_grid(box_n: int, cell: int, value: int, previous_fails: dict, success_coords: dict):
    """TODO"""
    coords = find_cell_coords(box_n, cell)
    # print(f"coords: {coords}", previous_fails)
    row, column, box = get_sudoku_partial_arrays(coords[0], coords[1])
    # print(f"row:{row}, column: {column}, box: {box}")
    # does step 2
    if check_all_conditions(row, column, box, value) and check_if_already_failed_coords(coords, value, previous_fails) and sudoku[coords] == 'x':
        sudoku[coords] = value

        # save success coords
        success_coords["coordinates"].append(coords)
        success_coords["values"].append(value)

        if box_n != 9:
            box_n += 1
            cell = 1
            # repeat the step with next box and first cell of that box
            return value, box_n, cell, previous_fails, success_coords
        else:
            if value != 9:
                value += 1
                box_n = 1
                cell = 1
                # returns sudoku and then it does the next value with first box and first cell
                return value, box_n, cell, previous_fails, success_coords
            else:
                # FINISH
                value += 1
                return value, box_n, cell, previous_fails, success_coords
    else:
        if cell != 9:
            cell += 1
            # repeat this step with new cell value and same box
            return value, box_n, cell, previous_fails, success_coords
        else:
            # print(box_n, cell, value, previous_fails, success_coords)
            return log_and_remove_error(success_coords, previous_fails)


if __name__ == "__main__":
    sudoku = np.full((9, 9), 'x', dtype='object')
    # start
    # i = 1 # value = i (same as word value lower in step 2)
    # this and sudoku to be properly made into global vals (they're kinda too rn but not properly)
    success_coords = {"coordinates": [], "values": []}
    previous_fails = {"coordinates": [], "values": []}

    value = 1
    j = 1
    k = 1
    try:
        while value != 10:
            value, j, k, previous_fails, success_coords = fill_the_grid(j, k, value, previous_fails, success_coords)
            if len(previous_fails["coordinates"]) > 1:
                print(f"box: {j}, cell: {k}")
                print("FULL sudoku: ", sudoku)
                print(previous_fails, success_coords)
            if len(previous_fails["coordinates"]) == 3:
                break
    except (ValueError, TypeError, IndexError) as e:
        print(e)
    print(sudoku)
