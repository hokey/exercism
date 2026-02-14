from string import ascii_lowercase, ascii_uppercase

def rotate(text, key):
    """
    Rotational cipher implementation handling multiple keys and translating according to text.

    :param str text: Original text
    :param str key: The rotational key type
    :return str: Cipher text
    """
    if key in (0, 26):
        return text
    new_text = ""
    for index in range(0, len(text)):
        if text[index].islower():
            new_text = new_text + ascii_lowercase[(ascii_lowercase.index(text[index]) + key) % 26]
        elif text[index].isupper():
            new_text = new_text + ascii_uppercase[(ascii_uppercase.index(text[index]) + key) % 26]
        else:
            new_text = new_text + text[index]
    return new_text