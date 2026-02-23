"""
Resistor Color Expert
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

COLOR_TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
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


def value(color_list: list[str]) -> int:
    """
    Given a color combination of return the summed value

    :param str color_str: Resistor colors
    :param int value: Calculated resistor values
    """
    if len(color_list) == 1:
        return 0 

    color_value = ""
    for color in color_list:
        color_value +=  str(color_code(color))
    return int(color_value)
    

def label(color_list: list[str]) -> str:
    """
    Give a list of colors, label the resistor.  

    :param list[str] color_list: The list of colors
    :return str: resitince in ohms
    """
    color_label = ""
    if len(color_list) == 1:
        return str(value(color_list)) + " ohms"
        
    color_value = value(color_list[:-2])
    color_value = int(color_value) * 10 ** COLOR_BANDS[color_list[-2]]
    
    if color_value // 1000000000 > 0:
        color_label = f"{color_value / 1000000000:g} gigaohms"
    elif color_value // 1000000 > 0:
        color_label = f"{color_value / 1000000:g} megaohms"
    elif color_value // 1000 > 0:
        color_label =  f"{color_value / 1000:g} kiloohms"
    else:
        color_label =  f"{color_value:g} ohms"
        
    return color_label


def tolerance(color_list: list[str]) -> str:
    """
    Given a resistence band color list, determine the tolerance

    :param list[str] color_list: The list of colors
    :return str: tolerance in percent
    """
    if len(color_list) > 1:
        return " ±" + COLOR_TOLERANCE[color_list[-1]]
    return ""


def resistor_label(color_list: list[str]) -> str:
    return label(color_list) + tolerance(color_list)
