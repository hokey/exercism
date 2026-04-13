"""
Word Counting Utility
"""
import string

def count_words(sentence):
    """
    Count the number of words in a sentence.  Sentences can contain special characters and returns.

    :param str sentence:
    :return dict:  A dictionary with string words as keys and the int count of words
    """
    word_count = {}
    word_sentence = sentence.replace("_", " ").replace(",", " ")
    words = [word.lower().strip(string.punctuation) for word in word_sentence.split()]
    for word in set(words):
        if word:
            word_count[word] = words.count(word)
    return word_count