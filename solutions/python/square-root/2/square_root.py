"""
Square root library
"""


def square_root(number: int) -> int:
    """
    Integer square root (binary search) 

    :param int number: target number for square root
    :return int: the square root
    """
    left = 0
    right = number + 1

    while left != right - 1:
        middle = (left + right) // 2
        if middle * middle <= number:
            left = middle
        else:
            right = middle

    return left