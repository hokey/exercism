"""
Utility to convert old math numbers
"""
GLYPHS = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9"
}

def convert(input_grid: list[str]) -> str:
    """
    Attempt to convert a grid of glyphs into numerical charcters given these rules:
    - The grid is made of one of more lines of cells.
    - Each line of the grid is made of one or more cells.
    - Each cell is three columns wide and four rows high (3x4) and represents one digit.
    - Digits are drawn using pipes ("|"), underscores ("_"), and spaces (" ").
    - If the input is not a valid size, your program should indicate there is an error.
    - If the input is the correct size, but a cell is not recognizable, your program should output a "?" for that character.

    :param list[str] input_grid: grid of glpyhs
    :return str: string representation of numbers
    """
    if len(input_grid) % 4 > 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 > 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    numbers: list[str] = []
    for row_index in range(0, len(input_grid), 4):
        for column_index in range(0, len(input_grid[row_index]), 3):
            numbers.append(GLYPHS.get(
                input_grid[row_index][column_index:column_index + 3] +
                input_grid[row_index + 1][column_index:column_index + 3] +
                input_grid[row_index + 2][column_index:column_index + 3] +
                input_grid[row_index + 3][column_index:column_index + 3]
                , "?"))
        if row_index + 4 < len(input_grid):
            numbers.append(",")
    return "".join(numbers)
        

    
        

