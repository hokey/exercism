"""
Killer Sudoku Helper
"""
import itertools
SUDUKO_DIGITS: list[int] = [1,2,3,4,5,6,7,8,9]
def combinations(target: int, size: int, exclude: list[int]):
    """
    Produces the number of combinations for a cage in killer sudoku

    :param int target: The target sum of the cage
    :param int size: The number of cells in the cage
    :param list[int] exclude: The digits already taken and not available for the cage
    :return list[list[int]]:  All of the possible candidates for the cage
    """
    digit_list = [digit for digit in SUDUKO_DIGITS if digit not in exclude]
    candidates = itertools.combinations(digit_list, size)
    return [list(candidate) for candidate in candidates if sum(candidate) == target]