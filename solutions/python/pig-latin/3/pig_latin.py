"""
Pig latin
"""
import re

VOWEL_SOUND = re.compile(r"^(?:[aeiou]|xr|yt)", re.IGNORECASE)
CONSONANT_QU = re.compile(r"^([^aeiouy]*qu)(.+)", re.IGNORECASE)
CONSONANT_Y = re.compile(r"^([^aeiou]+)(y\w*)$", re.IGNORECASE)
CONSONANT_VOWEL = re.compile(r"^([^aeiou]+)(.+)", re.IGNORECASE)

def translate(text: str) -> str:
    """
    Translates the text into pig latin

    :param str text: original text
    :return str: pig latin text
    """

    def translate_word(word: str) -> str:
        """
        Translates a word into pig latin

        :param str word: original text
        :return str: pig latin word
        """
        if VOWEL_SOUND.match(word):
            return word + "ay"

        match = CONSONANT_QU.match(word)
        if match:
            return match.group(2) + match.group(1) + "ay"

        match = CONSONANT_Y.match(word)
        if match:
            return match.group(2) + match.group(1) + "ay"

        match = CONSONANT_VOWEL.match(word)
        if match:
            return match.group(2) + match.group(1) + "ay"

        return word + "ay"

    return " ".join(translate_word(word) for word in text.split())