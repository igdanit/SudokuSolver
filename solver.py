# This module contain all logic for solve the sudoku.

from typing import List

# Checking number. Satisfy or not
def check_num(sudoku, x, y, n):
    # x - column
    # y - row
    # n - number

    for i in range(9):
        if sudoku[i][x] == n or sudoku[y][i] == n:
            return False

    for k in range(3):
        for m in range(3):
            if sudoku[y // 3 * 3 + k][x // 3 * 3 + m] == n:
                return False

    return True

# Swap all empty strings in sudoku to int=0.
def str_to_int(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == '':
                sudoku[y][x] = 0
            else:
                sudoku[y][x] = int(sudoku[y][x])

    return sudoku

# Main function
def sudoku_solver(sudoku: List[List]):
    def solver(gen):
        for y in range(9):
            for x in range(9):
                if sudoku[y][x] == 0:
                    for n in range(1, 10):
                        if check_num(sudoku, x, y, n):
                            sudoku[y][x] = n
                            solver(gen)
                            sudoku[y][x] = 0
                    return
        gen.send(sudoku)
        return

    saver = save_sudoku()
    sudoku = str_to_int(sudoku)
    solver(saver)
    result = next(saver)
    return result


def gen_initializer(coro):
    def inner(*args, **kwargs):
        initialized = coro(*args, **kwargs)
        next(initialized)
        return initialized
    return inner


@gen_initializer
def save_sudoku():
    sudoku = yield
    sudoku_copy = []
    for row in sudoku:
        sudoku_copy.append(row.copy())
    while True:
        yield sudoku_copy


def main():
    sudoku = [['', '', '', '8', '', '', '', '', ''],
              ['4', '', '', '', '1', '5', '', '3', ''],
              ['', '2', '9', '', '4', '', '5', '1', '8'],
              ['', '4', '', '', '', '', '1', '2', ''],
              ['', '', '', '6', '', '2', '', '', ''],
              ['', '3', '2', '', '', '', '', '9', ''],
              ['6', '9', '3', '', '5', '', '8', '7', ''],
              ['', '5', '', '4', '8', '', '', '', '1'],
              ['', '', '', '', '', '3', '', '', '']]

    for row in sudoku_solver(sudoku):
        print(row)


if __name__ == '__main__':
    main()
