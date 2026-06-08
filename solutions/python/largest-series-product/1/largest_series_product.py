"""
Largest Series Product
"""
from math import prod

def largest_product(series: str, size: int) -> int:
    """
    Determine the largest product among series up to given length.

    :param str series: The series to create the largest product for.
    :param int size: The size of the series to create the largest product for.
    :return int: The largest product among series up to given length.
    """
    if size <= 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    largest: int = 0
    for index in range(len(series) - size + 1):
        largest = max(largest, prod([int(digit) for digit in series[index:index + size]]))
    return largest