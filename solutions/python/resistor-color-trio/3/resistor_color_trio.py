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
    Given a color combination of return the summed value

    :param str color_str: Resistor colors
    :param int value: Calculated resistor values
    """
    if color_list[0] in colors() and color_list[1] in colors():
        return int(str(color_code(color_list[0])) + str(color_code(color_list[1])))
    return None

def label(color_list: list[str]) -> str:
    """
    Give a list of colors, label the resistor.  

    :param list[str] color_list: The list of colors
    :return str: resitince in ohms
    """
    color_value = str(value(color_list)) + str(10 ** COLOR_BANDS[color_list[2]])[1:]
    zero_count = color_value.count("0")
    color_label = ""
    if zero_count < 3:
        color_label = color_value + " ohms"
    elif zero_count < 6:
        color_label =  color_value[:-3:] + " kiloohms"
    elif zero_count < 9:
        color_label =  color_value[:-6:] + " megaohms"
    else:
        color_label =  color_value[:-9:] + " gigaohms"
    return color_label