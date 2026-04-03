"""
Library ot handle calculations for game
"""

def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Given the limit of multiples, calculate the sum of all multiples of the given multiple list

    :param int limit: Upper boundary of numbers to consider
    :param list[int]: List of multiples to calculate against
    """
    multiples_set = set([0])
    number_set = range(1,limit)
    for multiple in multiples:
        if multiple == 0:
            continue
        for number in number_set:
            if number % multiple == 0:
                multiples_set.add(number)
    return sum(multiples_set)

    
