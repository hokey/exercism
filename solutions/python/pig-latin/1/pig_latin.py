"""
Pig latin
"""
import re

RULE_1 = re.compile(r"\b(?:[aeiou]|xr|yt)\w*\b", re.IGNORECASE)
RULE_2 = re.compile(r"\b([^aeiou]*)([aeiou]\w*)\b", re.IGNORECASE)
RULE_3 = re.compile(r"\b([^aeiouy]*?qu|[^aeiouy]+)(\w*)\b", re.IGNORECASE)
RULE_4 = re.compile(r"\b([^aeiou]*?y|[^aeiou]+)(\w*)\b", re.IGNORECASE)

def translate(text):
    """
    Translates the text into pig latin

    :param str text: original text
    :return str: pig latin text
    """
    pig_latin = []

    for word in text.split():
        if RULE_1.findall(word):
            for match in RULE_1.findall(word):
                pig_latin.append(match.replace(match, match+"ay"))
        elif RULE_3.findall(word):
            for match in RULE_3.finditer(word):
                pig_latin.append(word.replace(match.group(0), match.group(2)+match.group(1)+"ay"))
        elif RULE_4.findall(word):
            for match in RULE_4.finditer(word):
                pig_latin.append(text.replace(match.group(0), match.group(2)+match.group(1)+"ay"))
        elif RULE_2.findall(word):
            for match in RULE_2.finditer(word):
                pig_latin.append(word.replace(match.group(0), match.group(2)+match.group(1)+"ay"))   
    return " ".join(pig_latin)