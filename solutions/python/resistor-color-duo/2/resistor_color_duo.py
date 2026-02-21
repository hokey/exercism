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


def color_code(color: str) -> str:
    """
    Given a color, return the resistor code if it exists

    :param str color: lookup color 
    :return str: resistor code if present
    """
    if color in colors():
        return COLOR_BANDS[color]
    return ""


def colors() -> list[str]:
    """
    Returns the resistor colors

    :param list[str]: List of resistor colors
    """
    return  list(COLOR_BANDS.keys())


def value(color_list: list[str]) -> int | None:
    """
    Given a color combination of '<COLOR>-<COLOR>*' return the summed value

    :param str color_str: Resistor colors a '<COLOR>-<COLOR>*' format
    :param int value: Calculated resistor values
    """
    if color_list[0] in colors() and color_list[1] in colors():
        return int(str(color_code(color_list[0])) + str(color_code(color_list[1])))
