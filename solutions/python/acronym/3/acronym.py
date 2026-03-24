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
    return "".join(
        word[0].upper()
        for word in words.replace("-", " ").translate(translator).split()
    )
    
