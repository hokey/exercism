"""
Line messaging
"""
MIDDLE_MESSAGE = ", you are the "
END_MESSAGE = " customer we serve today. Thank you!"
NUMBER_MAP = {
    "1": "st",
    "2": "nd",
    "3": "rd"
}

def line_up(name, number):
    """
    Given a name and number, produce a friendly sentence for that person's position in line

    :param str name: Customer name
    :param int number: Customer's place in line
    :return str: Friendly sentence annoucing customer's place in line
    """
    
    position = NUMBER_MAP[str(number)[-1]] if number % 100 not in [11,12,13] and  str(number)[-1] in NUMBER_MAP.keys() else "th"
    return name + MIDDLE_MESSAGE + str(number) + position + END_MESSAGE
