"""
Food Chain Song Utility 
"""
THINGS = [
    ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
    ("spider", "It wriggled and jiggled and tickled inside her."),
    ("bird", "How absurd to swallow a bird!"),
    ("cat", "Imagine that, to swallow a cat!"),
    ("dog", "What a hog, to swallow a dog!"),
    ("goat", "Just opened her throat and swallowed a goat!"),
    ("cow", "I don't know how she swallowed a cow!"),
    ("horse", "She's dead, of course!")
]
PHRASES = [
    "I know an old lady who swallowed a {thing}.",
    "She swallowed the {current_thing} to catch the {next_thing}{bird_thing}."
]


def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Recite parts of the Food Chain Song given the starting and ending verse
    :param int start_verse: The starting verse
    :param int end_verse: The ending verse
    """
    recitals: list[str] = []
    if start_verse > end_verse:
        raise ValueError("end verse must be greater than start verse.")
    if not (1 <= start_verse <= 8) or not (1 <= end_verse <= 8):
        raise ValueError("verse must be 1 to 8")
    for verse_number in range(start_verse, end_verse+1):
        recitals.extend(
            recite_verse(verse_number)
        )
        if verse_number != end_verse:
            recitals.append("")
    return recitals


def recite_verse(verse_number: int) -> list[str]:
    """
    Recite the verse part of the Food Chain Song
    :param int verse_number: Verse to recite
    :return str: The verse part
    """
    recital: list[str] = []
    first: bool = True
    if verse_number == len(THINGS):
        recital.append(PHRASES[0].format(thing=THINGS[-1][0]))
        recital.append(THINGS[-1][1])
        return recital
    for index in range(verse_number, 0, -1):
        if first:
            recital.append(PHRASES[0].format(thing=THINGS[index - 1][0]))
            recital.append(THINGS[index - 1][1])
            first = False
        else:
            recital.append(PHRASES[1].format(
                current_thing=THINGS[index][0],
                next_thing=THINGS[index -1][0],
                bird_thing=" that"+THINGS[index -1][1][2:-1] if index == 2 else ""))
            if index - 1 == 0:
                recital.append(THINGS[index - 1][1])
    return recital