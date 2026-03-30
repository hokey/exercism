"""
Word Counting Utility
"""
import re
from collections import Counter

WORD_RE = re.compile(r"[^\W_]+(?:'[^\W_]+)*", re.UNICODE)

def count_words(sentence: str) -> dict[str, int]:
    """
    Count the number of words in a sentence.  Sentences can contain special characters and returns.

    :param str sentence:
    :return dict[str, int]:  A dictionary with string words as keys and the int count of words
    """
    return Counter(WORD_RE.findall(sentence.casefold()))