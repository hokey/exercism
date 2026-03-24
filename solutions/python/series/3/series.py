"""
Series generators
"""

def slices(series: str, length: int) -> list[str]:
    """
    Given the series and the length of slice, produce slices of the series

    :param str series: Series of characters
    :param int length: Length of slices to produce
    :return list[str]
    """
    if not series:
        raise ValueError("series cannot be empty")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [
        series[index:index + length]
        for index in range(len(series) - length + 1)
    ]