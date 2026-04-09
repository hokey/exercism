"""
Transpose strings
"""
from itertools import zip_longest

def transpose(text):
    """
    Transposes strings based on new line delimeters and space padding for mismatches

    :param str text: Text to transpose
    :return str: Transposed text
    """

    if not text:
        return text

    lines = text.split("\n")
    lengths = [len(line) for line in lines]

    result = []

    for row_index, chars in enumerate(zip_longest(*lines, fillvalue=" ")):
        row = list(chars)

        # Remove ONLY padding spaces from the right
        col = len(row) - 1
        while col >= 0 and row[col] == " " and row_index >= lengths[col]:
            col -= 1

        result.append("".join(row[:col + 1]))

    return "\n".join(result)
          