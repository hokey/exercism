"""
Word Counting Utility
"""
import string
from collections import Counter

def count_words(sentence):
    """
    Count the number of words in a sentence.  Sentences can contain special characters and returns.

    :param str sentence:
    :return dict[str, int]:  A dictionary with string words as keys and the int count of words
    """
    sentence = sentence.replace("_", " ").replace(",", " ")

    
    punctuation = string.punctuation.replace("'", "")
    translator = str.maketrans('', '', punctuation)

    word_count = Counter()
    for token in sentence.split():
        word = token.casefold().translate(translator).strip("'")
        if word:
            word_count[word] +=1
    return dict(word_count)