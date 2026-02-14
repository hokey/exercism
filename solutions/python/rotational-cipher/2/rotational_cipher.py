from string import ascii_lowercase, ascii_uppercase

def rotate(text: str, key: int) -> str:
    """
    Rotational cipher implementation handling multiple keys and translating according to text.

    :param str text: Original text
    :param int key: The rotational key type
    :return str: Cipher text
    """
    new_text = []
    for character in text:
        if character.islower():
            new_text.append(chr((ord(character) - ord('a') + key) % 26 + ord('a')))
        elif character.isupper():
            new_text.append(chr((ord(character) - ord('A') + key) % 26 + ord('A')))
        else:
            new_text.append(character)
    return "".join(new_text)