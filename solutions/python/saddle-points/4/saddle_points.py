"""
Saddle Points Utility
"""
from typing import TypedDict


class SaddlePoint(TypedDict):
    """
    Saddle point of a matrix
    """
    row: int
    column: int

    
def saddle_points(matrix: list[list[int]]) -> list[SaddlePoint]: 
    """
    Given a regular matrix, determine the saddle points with the following rules:
    - largest in row
    - smallest in column

    :param list[list[int]] matrix: regular matrix to search
    :return list[SaddlePoint]: saddle points
    """
    if not matrix:
        return []
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    saddle_points_list: list[SaddlePoint] = []
    
    max_rows = [max(row) for row in matrix]
    min_columns = [min(matrix[row_index][column_index] for row_index in range(len(matrix)))
               for column_index in range(len(matrix[0]))]

    return [
        {"row": row_index+1, "column": column_index+1}
        for row_index, max_row in enumerate(max_rows)
        for column_index, min_column in enumerate(min_columns)
        if max_row == min_column
    ]