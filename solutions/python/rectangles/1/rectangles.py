"""
Rectangle detector
"""
from itertools import combinations

def rectangles(strings: list[str]) -> int:
    """
    Given a string represenation of a graph, detect all rectangles.
    Rectangles are in the form of "+" for corners and "-" or "|" for edges.

    :param list[str] strings: The graph
    :return int: The count of rectangles
    """
    points: list[tuple[int, int]] = [
        (index_x, index_y)
        for index_x, row in enumerate(strings)
        for index_y, column in enumerate(row)
        if column == "+"
    ]

    point_set: set[tuple[int, int]] = set(points)
    
    rectangles = {
        frozenset([(x1, y1), (x1, y2), (x2, y1), (x2, y2)])
        for (x1, y1), (x2, y2) in combinations(points, 2)
        if x1 != x2 and y1 != y2
        if (x1, y2) in point_set and (x2, y1) in point_set
    }

    return sum(
        1 for rectangle in rectangles
        if is_connected_rectangle(rectangle, strings)
    )


def is_connected_rectangle(rectangle: frozenset[tuple[int, int]] , grid: list[str]) -> bool:
    """
    Given a frozen set of tuples representing a rectangle in a grid and the grid itself,
        determine if the rectangle is connected.

    :param frozenset[tuple[int, int]] rectangle: The rectangle
    :param list[str]: The grid
    :return bool: If the rectangle is connected
    """
    xs = sorted([p[0] for p in rectangle])
    ys = sorted([p[1] for p in rectangle])

    x1, x2 = xs[0], xs[-1]
    y1, y2 = ys[0], ys[-1]

    for y in range(y1 + 1, y2):
        if grid[x1][y] not in "-+":
            return False
        if grid[x2][y] not in "-+":
            return False

    for x in range(x1 + 1, x2):
        if grid[x][y1] not in "|+":
            return False
        if grid[x][y2] not in "|+":
            return False

    return True
