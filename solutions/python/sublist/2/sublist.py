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


def sublist(list_one, list_two):
    """
    Given two integer lists, determine the classifcation of the relationship between the two

    :param list[int] list_one: Integer list
    :param list[int] list_two: Integer list
    :return int: The documented classification between the two lists
    """
    if list_one == list_two:
        return EQUAL
    if list_one and not list_two:
        return SUPERLIST
    if not list_one and list_two:
        return SUBLIST
    else:
        str_list_one = "".join([str(x) for x in list_one])
        str_list_two = "".join([str(x) for x in list_two])
        if str_list_one in str_list_two:
            if len(list_one) > len(list_two):
                return UNEQUAL
            elif len(list_one) == len(list_two) and len(str_list_one) != len(str_list_two):
                return UNEQUAL
            else:
                return SUBLIST
        elif str_list_two in str_list_one:
            if len(list_two) > len(list_one):
                return UNEQUAL
            elif len(list_one) == len(list_two) and len(str_list_one) != len(str_list_two):
                return UNEQUAL
            else:
                return SUPERLIST
        else:
            return UNEQUAL