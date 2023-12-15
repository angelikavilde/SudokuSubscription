import numpy as np
import random
from sudoku_solver import check_all_conditions, get_position, count_x, solve_sudoku


def log_and_remove_error():
    # something went wrong (red oval on diagram)

    last_invalid_coords = success_coords["coordinates"].pop()
    last_invalid_value = success_coords["values"].pop()

    # saving a fail
    previous_fails["coordinates"].append(last_invalid_coords)
    previous_fails["values"].append(last_invalid_value)

    # removing last logged success
    success_coords["coordinates"].pop()
    success_coords["values"].pop()

    k = 1
    j = "last used in coords above j" #TODO calculate which box it is
    i = last_invalid_value
    # go to step 2
    fill_the_grid()


def fill_the_grid(column: int, row: int, value: int, previous_fails: dict, success_coords: dict):
    #repeated step 2:
    coords = (column, row)

    # finds every matched coords in fails:
    coord_failed = {indx for indx, fail 
            in enumerate(previous_fails["coordinates"]) if coords == fail}
    values_coord_failed_for = {previous_fails["values"][indx] for indx in coord_failed}

    # does step 2
    if check_all_conditions(row, column, box, value) and value not in values_coord_failed_for:
        sudoku[coords] = value
    
        # save success coords
        success_coords["coordinates"].append(coords)
        success_coords["coordinates"].append(value)
        if j != 9:
            j += 1
            # go to step 2 with new j and same k
        else:
            if value != 9:
                value += 1
                return sudoku
            else:
                # FINISH
                print(sudoku)
    else:
        if k != 9:
            k += 1
            # repeat step 2 with new k and same j
        else:
            log_and_remove_error()


#! PSEUDOCODE BELOW
if __name__ == "__main__":
    sudoku = np.full((9, 9), 'x', dtype='object')
    # start
    # i = 1 # value = i (same as word value lower in step 2)
    success_coords = {"coordinates": [], "values": []}
    previous_fails = {"coordinates": [], "values": []}

    for i in range(1,10):
        j = 1 #box numb
        k = 1 #cell numb
        sudoku = fill_the_grid()

    # #repeated step 1:
    # j = 1 #box numb
    # k = 1 #cell numb