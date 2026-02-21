"""
Resistor Color Mapper
"""

COLOR_BANDS = {
            "black": 0,
            "brown": 1,
            "red": 2,
            "orange": 3,
            "yellow": 4,
            "green": 5,
            "blue": 6,
            "violet": 7,
            "grey": 8,
            "white": 9,
}

def color_code(color):
    """
    Given a color, return the resistor code if it exists

    :param str color: lookup color 
    :return str: resistor code if present
    """
    if color in colors():
        return COLOR_BANDS[color]
    return ""


def colors():
    """
    Returns the resistor colors

    :param list[str]: List of resistor colors
    """
    return  list(COLOR_BANDS.keys())
