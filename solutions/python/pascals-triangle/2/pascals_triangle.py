"""
Pascals Triangle
https://en.wikipedia.org/wiki/Pascals_triangle
"""

def rows(row_count:int) -> list[list[int]]:
    """
    Produces the number of rows given by row_count for Pascals Triangle.
    :param row_count: Number of rows
    :return list[list[int]]: Pascals Triangle
    """
    if row_count < 0:
        raise ValueError("number of rows is negative")
    return build_rows([], row_count)


def build_rows(triangle: list[list[int]], row_count:int) -> list[list[int]]:
    """
    Builds rows of Pascals Triangle.
    :param list[list[int]] triangle: Pascals Triangle
    :param int row_count: Number of rows of Pascals Triangle to build
    :return list[list[int]]: Pascals Triangle
    """
    if len(triangle) == row_count:
        return triangle
    if not triangle:
        triangle.append([1])
    else:
        row: list[int] = []
        left: int = 0
        right: int = 0
        for index in range(0, len(triangle[-1]) + 1):
            if index - 1 < 0:
                left = 0
            else:
                left = triangle[-1][index-1]
            if index == len(triangle[-1]):
                right = 0
            else:
                right = triangle[-1][index]
            row.append(left + right)
        triangle.append(row)
    return build_rows(triangle, row_count)
