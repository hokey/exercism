import string

def is_pangram(sentence: str) -> bool:
    """
    Detects if a string has all case-insenstive aplpabetical letters in it

    :param str sentence: The given sentence string
    :return bool: If it has all case-insenstive aplpabetical letters in it
    """
    seen = set()
    for character in sentence.lower():
        if character in string.ascii_lowercase:
            seen.add(character)
            if len(seen) == 26:
                return True
    return False