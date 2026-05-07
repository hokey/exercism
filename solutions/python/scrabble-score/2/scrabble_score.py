"""
Scrabble Score Utility
"""

def score(word: str) -> int:
    """
    Calculates the scrabble score for a given word

    :param str word: scrabble wordc
    :return int: score
    """
    scrabble_score = 0
    if not word:
        return scrabble_score
    for character in word:
        if character.upper() in {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"}:
            scrabble_score += 1
        elif character.upper() in {"D", "G"}:
            scrabble_score += 2
        elif character.upper() in {"B", "C", "M", "P"}:
            scrabble_score += 3
        elif character.upper() in {"F", "H", "V", "W", "Y"}:
            scrabble_score += 4
        elif character.upper() in {"K"}:
            scrabble_score += 5
        elif character.upper() in {"J", "X"}:
            scrabble_score += 8
        else: # {"Q", "Z"}
            scrabble_score += 10
    return scrabble_score