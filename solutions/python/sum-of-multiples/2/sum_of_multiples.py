"""
Library ot handle calculations for game
"""

def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Given the limit of multiples, calculate the sum of all multiples of the given multiple list

    :param int limit: Upper boundary of numbers to consider
    :param list[int]: List of multiples to calculate against
    """
    if limit == 0:
        return 0
        
    multiples_set = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        multiples_set.update(range(multiple, limit, multiple))
    return sum(multiples_set)