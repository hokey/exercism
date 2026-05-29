"""
Killer Sudoku Helper
"""
import itertools
from collections import defaultdict
from functools import lru_cache

SUDOKU_DIGITS: tuple[int] = tuple(range(1, 10))
PRECOMPUTED: dict[tuple[int, int], list[tuple[int, ...]]] = defaultdict(list)

for cage_size in range(1,10):
    for combination in itertools.combinations(SUDOKU_DIGITS, cage_size):
        PRECOMPUTED[(cage_size, sum(combination))].append(combination)

@lru_cache(maxsize=None)
def _filtered_combinations(size: int, target: int, exclude: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """
    Filters out the precomputed set of solutions givne the size and target for the cage

    :param int target: The target sum of the cage
    :param int size: The number of cells in the cage
    :param tuple[int, ...] exclude: The digits already taken and not available for the cage
    :return tuple[tuple[int, ...], ...]:  All of the possible candidates for the cage
    """
    base = PRECOMPUTED.get((size, target), [])
    exclude_set = set(exclude)

    return tuple(
        combination
        for combination in base
        if exclude_set.isdisjoint(combination)
    )

def combinations(target: int, size: int, exclude: list[int]):
    """
    Produces the number of combinations for a cage in killer sudoku

    :param int target: The target sum of the cage
    :param int size: The number of cells in the cage
    :param list[int] exclude: The digits already taken and not available for the cage
    :return list[list[int]]:  All of the possible candidates for the cage
    """
    return [
        list(combination)
        for combination in _filtered_combinations(size, target, tuple(sorted(exclude)))
    ]
