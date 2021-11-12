# Responsible for representation of sudoku in Kivy.
# In this app, sudoku represents like a grid of grids.
# One small grid contain a cells, which you can use to write a value(int).
# Mask of grid(main, and little ones):
#
#         1  |  2  |  3
#       _____|_____|_____
#         4  |  5  |  6
#       _____|_____|_____
#         7  |  8  |  9
#            |     |
#
# The number in mask it's a position of value or a little grid(which contains values).
# In code i call the little grid as square.
# Sudoku contain 9 squares. And this squares contain a numerical series from 1 to 9.


from typing import List, Dict
from solver import sudoku_solver


def list_to_square(list_values: List):
    mask = [['', '', ''],
            ['', '', ''],
            ['', '', '']]
    for i in range(9):
        value = list_values[i]
        row_num = i // 3
        cell_num = i % 3
        mask[row_num][cell_num] = value

    return mask


def square_to_sudoku(list_squares: List):
    mask = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    for i in range(9):
        segment = list_squares[i]
        for g in range(3 * (i // 3), 3 * (i // 3) + 3):
            mask[g] += segment[g % 3]
    return mask

# Taking a Dict of cells and making sudoku from them.
def sudoku_filler(sudoku_grid: Dict):
    snakes = []
    for square in sudoku_grid.values():
        snakes.append(list_to_square(square))
    sudoku_layout = square_to_sudoku(snakes)

    sudoku = []

    for row in sudoku_layout:
        sudoku_row = []
        for cell in row:
            sudoku_row.append(cell.text)
        sudoku.append(sudoku_row)

    solved_sudoku = sudoku_solver(sudoku)

    counter = 0
    while counter != 81:
        sudoku_layout[counter // 9][counter % 9].text = str(solved_sudoku[counter // 9][counter % 9])
        counter += 1

    return