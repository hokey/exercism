"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

def is_sublist(small, big):
    """
    Explicitly check if small is a sublist of big

    :param list[int] small: list to check
    :param list[int] big: test list
    :return bool: If small is a sublist of big
    """
    if not small:
        return True
    len_small = len(small)
    return any(big[index:index + len_small] == small for index in range(len(big) - len_small + 1))


def sublist(list_one, list_two):
    """
    Given two integer lists, determine the classifcation of the relationship between the two

    :param list[int] list_one: Integer list
    :param list[int] list_two: Integer list
    :return int: The documented classification between the two lists
    """
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL