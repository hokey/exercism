from string import ascii_lowercase

def is_isogram(string):
    """
    Determine if a iven a word or phrase is an isogram

    :param str string: a word or phrase
    :return boo: if the work or phrase is an isogram
    """
    string_set = set(string.lower())
    for character in string_set:
        if character in ascii_lowercase and string.lower().count(character) > 1:
            return False
    return True
