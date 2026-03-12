from string import ascii_lowercase

def is_isogram(string):
    """
    Determine if a iven a word or phrase is an isogram

    :param str string: a word or phrase
    :return boo: if the work or phrase is an isogram
    """
    seen = set()
    for character in string.lower():
        if character in ascii_lowercase:
            if character in seen:
                return False
            seen.add(character)
    return True
