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
    current_char = string[0]
    count = 1
    for character in string[1:]:
        if character == current_char:
            count += 1
        else:
            result.append(
                f"{count if count > 1 else ""}{current_char}"
            )
            current_char = character
            count = 1
    result.append(
        f"{count if count > 1 else ""}{current_char}"
    )
    return "".join(result)
