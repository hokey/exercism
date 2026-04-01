"""
Proverb Utility
"""
PREFIX = "For want of a "
FINAL_PREFIX = "And all for the want of a "
THE = " the "
SUFFIX = " was lost."
SPACE = " "

def proverb(*input_data: str, qualifier: str) -> list[str]:
    """
    Do the proverb base the the pieces given and ending with a potential qualifier

    :param list[str] *input_data: The words to use with the proverb
    :param str qualifier: The qualifier applied at the end
    :return list[str]: The proverb sentences
    """
    proverb_pieces: list[str] = []
    for previous, current in zip(input_data, input_data[1:]):
        proverb_pieces.append(
            f"{PREFIX}{previous}{THE}{current}{SUFFIX}"
        )
    if input_data:
        proverb_pieces.append(
            f"{FINAL_PREFIX}{(qualifier + SPACE + input_data[0]) if qualifier else input_data[0]}."
        )
    return proverb_pieces