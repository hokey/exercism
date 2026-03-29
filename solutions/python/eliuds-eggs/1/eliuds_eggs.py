"""
Eliuds Eggs Contraption
"""

def egg_count(display_value: int) -> int:
    """
    Given a value on the display, calculate the correct number of eggs by taking the display number, converting to binary, and counting the 1s

    :param int display_value: The value on the display
    :return int: The correct number of eggs
    """
    number = 0
    binary_count = 0
    power = 0
    while number < display_value:
        number = 2 ** power
        power += 1

    number = display_value
    while number > 0:
        binary_count += number // (2 ** power)
        number = number % (2 ** power)
        power -= 1
        
    return binary_count