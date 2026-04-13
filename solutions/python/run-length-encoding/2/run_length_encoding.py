"""
Run Length Library
"""

def decode(string: str) -> str:
    """
    Decode an encoded run length string

    :param str string: encoded string
    :return str: decoded string
    """
    result = []
    count = ""
    for character in string:
        if character.isdigit():
            count += character
        else:
            result.append(character * (int(count) if count else 1))
            count = ""
    return "".join(result)


def encode(string: str) -> str:
    """
    Run length encode a string
    """
    if not string:
        return ""
    result = []
    current = []
    for character in string:
        if not current or current[0] == character:
            current.append(character)
        else:
            result.append(f"{str(len(current)) if len(current) > 1 else ""}{current[0]}")
            current = [character]
    result.append(f"{str(len(current)) if len(current) > 1 else ""}{current[0]}")
    return "".join(result)
