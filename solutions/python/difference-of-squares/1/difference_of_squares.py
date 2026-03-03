"""
Library for squares of numbers
"""

def square_of_sum(number):
    """ 
    Given an number, produce a square of the sum of values up to the number

    :param int number: upper bound number
    :reaturn int: square of sums
    """
    return (number * (number + 1) // 2) ** 2


def sum_of_squares(number):
    """
    Given a number, produce the some of squares for each value up to the number

    :param int number: upper bound number
    :return int: sum of squares
    """
    return (number * (number + 1) * (2 * number + 1)) // 6


def difference_of_squares(number):
    """
    Given a number, produce the difference between the sum of squares up to the number and then square of sums up to the number

    :param int number: upper bound number
    :return int:  difference of squares
    """
    return square_of_sum(number) - sum_of_squares(number)
