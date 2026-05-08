"""
Bottle Song Utility
"""
BOTTLE_NUMBERS = {
    0: "no",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

VERSE_TEMPLATE = "{begin} green bottle{plural} hanging on the wall,\n{begin} green bottle{plural} hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be {next} green bottle{plural_next} hanging on the wall."

def recite(start: int, take: int = 1) -> list[str]:
    """
    Recite the bottle song given the starting bottle and taking a number of steps in them

    Assumptions: This only goes to 10

    :param int start: The start of the bottle song
    :param int take: The number of verses to go in the song
    :param list[str]: The list of lines of the bottle songs
    """
    if start < 1 or start > 10:
        raise ValueError("Start must be within 1 to 10")
    if take > start:
        raise ValueError("Only take what is available")
    result: list[str] = []
    for bottle in range(start, start - take, -1):
        result += VERSE_TEMPLATE.format(
            begin=BOTTLE_NUMBERS[bottle].title(),
            next=BOTTLE_NUMBERS[bottle - 1],
            plural="s" if bottle > 1 else "",
            plural_next="s" if bottle - 1 != 1 else "").split("\n")
        if bottle > (start - take + 1):
            result += [""]
    return result
    
