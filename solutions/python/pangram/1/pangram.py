import re

def is_pangram(sentence: str) -> bool:
    """
    Detects if a string has all case-insenstive aplpabetical letters in it

    :param str sentence: The given sentence string
    :return bool: If it has all case-insenstive aplpabetical letters in it
    """
    return len(set(list(re.sub(r"[^a-z]", "", sentence.lower())))) == 26
