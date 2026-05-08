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
    :return dict[str: int]: saddle points
    """
    if not matrix:
        return matrix
    validate_matrix(matrix)
    max_points: list[SaddlePoint] = find_max_points(matrix)
    min_points: list[SaddlePoint] = find_min_points(matrix)
    return [saddle_point for saddle_point in max_points if saddle_point in min_points] 


def validate_matrix(matrix: list[list[int]]) -> None: 
    """
    Validates the regularity of a given matrix
    
    :param list[list[int]] matrix: regular matrix to search
    """
    last_row_length: int | None = None
    for row in matrix:
        if last_row_length is None:
            last_row_length = len(row)
        else:
            if last_row_length != len(row):
                raise ValueError("irregular matrix")
            last_row_length = len(row)

    
def find_max_points(matrix: list[list[int]]) -> list[SaddlePoint]:
    """
    Given a matrix, find all the points where the position has the max value with respect to each row
    
    :param list[list[int]] matrix: regular matrix to search
    :return dict[str: int]: saddle points
    """
    validate_matrix(matrix)
    saddle_points_list: list[SaddlePoint] = []
    for row_index, row in enumerate(matrix):
        max_column: int = max(row)
        for column_index, column in enumerate(row):
            if column == max_column:
                saddle_points_list.append({"row": row_index + 1, "column": column_index + 1})
    return saddle_points_list

    
def find_min_points(matrix: list[list[int]]) -> list[SaddlePoint]:
    """
    Given a matrix, find all the points where the position has the min value with respect to each column
    
    :param list[list[int]] matrix: regular matrix to search
    :return dict[str: int]: saddle points
    """
    validate_matrix(matrix)
    saddle_points_list: list[SaddlePoint] = []
    for column_index in range(len(matrix[0])):
        min_row: int | None = None
        for row_index, row in enumerate(matrix):
            if min_row is None:
                min_row = row[column_index]
            elif row[column_index] < min_row:
                min_row = row[column_index]
            else:
                continue
        for row_index, row in enumerate(matrix):
            if row[column_index] == min_row:
                saddle_points_list.append({"row": row_index + 1, "column": column_index + 1})
    return saddle_points_list   