"""
Flower Field Game Utility
"""
DIRECTIONS = [
    (-1,-1),
    (-1, 0),
    (-1, 1),
    (0,-1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

VALID_CHARACTERS = [" ", "*"]

def annotate(garden: list[str]) -> list[str]:
    """
    Given a garden in the Flower Field Game, return an annotated version signaling counts of flowers
    for each square

    :param list[str] garden: A valid garden with spaces and flowers
    :return list[str]: The annotated version setting up the game
    """
    if len(set([len(row) for row in garden])) > 1:
        raise ValueError("The board is invalid with current input.")
    if not garden or (len(garden) == 1 and not garden[0]):
        return garden
    result: list[list[str]] = [list(row) for row in garden]
    for row_index, row in enumerate(garden):
        for column_index, column in enumerate(row):
            if column not in VALID_CHARACTERS:
                raise ValueError("The board is invalid with current input.")
            if column == "*":
                continue
            flower_count = _flower_count(garden, row_index, column_index)
            if flower_count > 0:
                result[row_index][column_index] = str(flower_count)
    return ["".join(row) for row in result]
            
            
def _flower_count(garden: list[str], row: int, column: int) -> int:
    """
    Given a location, find the count of flowers (*) in a garden.

    :param int row: The row of the location
    :param int column: The column of the location
    :param list[str] garden: The garden to search
    :return int: The count of flowers
    """
    total: int = 0
    num_rows: int = len(garden)
    num_columns: int = len(garden[0])
    for dir_row, dir_column in DIRECTIONS:
        new_row, new_column = row + dir_row, column + dir_column
        if 0 <= new_row < num_rows and 0 <= new_column < num_columns and garden[new_row][new_column] == "*":
            total += 1
    return total