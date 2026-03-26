def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    Give a word, return the list of anagrams from a list of candidates

    :param str word: Looking for anagrams of this word
    :return list[str]: Ananagrams of the word
    """
    anagrams = []
    sorted_word = sorted(word.lower())
    for test_word in candidates:
        if word.lower() == test_word.lower():
            continue
        if sorted(test_word.lower()) == sorted_word:
            anagrams.append(test_word)
    return anagrams