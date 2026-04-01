"""
Proverb Utility
"""
PREFIX = "For want of a "
FINAL_PREFIX = "And all for the want of a "
THE = " the "
SUFFIX = " was lost."

def proverb(*input_data, qualifier: str) -> list[str]:
    """
    Do the proverb base the the pieces given and ending with a potential qualifier

    :param list[str] pieces: The words to use with the proverb
    :param str qualifier: The qualifier applied at the end
    :return list[str]: The proverb sentences
    """
    pieces = input_data
    proverb_pieces = []
    for index, piece in enumerate(pieces):
        if index == 0:
            proverb_pieces.append(
                f"{FINAL_PREFIX}{(qualifier + " " + piece) if qualifier else piece}."
            )
        else:
            proverb_pieces.insert(index - 1,
                f"{PREFIX}{pieces[index - 1]}{THE}{piece}{SUFFIX}"
            )
    return proverb_pieces