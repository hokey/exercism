"""
Acronym Library
"""
import string


def abbreviate(words):
    """
    Given a string of words, produce the acronym

    :param str words: Words to condense
    :return str: Acronym of words
    """
    translator = str.maketrans("", "", string.punctuation)
    words = words.replace("-", " ").translate(translator)
    words = words.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym
