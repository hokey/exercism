"""
Conway's Game of Life
"""
from itertools import chain

def tick(matrix: list[list[int]]) -> list[list[int]]:
    """
    Marches one tick forward in generation of game of life

    Assumptions: matrix is square, it must be at least 3x3, no wraparounds on the matrix

    :param list[list[int]] matrix: the current generation
    :return list[list[int]]: the next generation tick
    """
    size = len(matrix)
    next_matrix = [[0 for _ in range(size)] for _ in range(size)]

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if check(matrix, row, column):
                next_matrix[row][column] = 1
    return next_matrix


def check(matrix: list[list[int]], row: int, column: int) -> bool:
    """
    Checks the neighbors of a spot on the matrix against these set of rules:
    - Any live cell with two or three live neighbors lives on.
    - Any dead cell with exactly three live neighbors becomes a live cell.
    - All other cells die or stay dead.

     Assumptions: matrix is square, it must be at least 3x3
     
    :param list[list[int]] matrix: the game matrix
    :param row int: the row location
    :param column int: the column location
    :return bool: if there is life at the give row and column
    """
    size = len(matrix)
    row_min = max(row - 1, 0)
    row_max = min(row + 1, size)
    column_min = max(column - 1, 0)
    column_max = min(column + 1, size)

    check_matrix = [check_row[column_min:column_max+1] for check_row in matrix[row_min:row_max+1]]
    count = sum(list(chain.from_iterable(check_matrix))) - matrix[row][column]
  
    if matrix[row][column] == 1 and (count == 2 or count == 3):
        return True
    if matrix[row][column] == 0 and count == 3:
        return True
    return False