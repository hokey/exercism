"""
Scrabble Score Utility
"""
LETTER_SCORES = {
    **dict.fromkeys("AEIOULNRST", 1),
    **dict.fromkeys("DG", 2),
    **dict.fromkeys("BCMP", 3),
    **dict.fromkeys("FHVWY", 4),
    "K": 5,
    **dict.fromkeys("JX", 8),
    **dict.fromkeys("QZ", 10),
}
def score(word: str) -> int:
    """
    Calculates the scrabble score for a given word

    :param str word: scrabble word
    :return int: score
    """
    scrabble_score = 0
    for character in word.upper():
        scrabble_score += LETTER_SCORES.get(character, 0)
    return scrabble_score