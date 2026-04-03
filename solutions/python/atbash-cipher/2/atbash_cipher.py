"""
Atbash Cipher
"""
import string

CRYPT = 'zyxwvutsrqponmlkjihgfedcba'


def encode(plain_text):
    """
    Encode the given text into an Atbash Cipher

    :param str plain_text: Text to encode
    :return str: Atbash encoded text
    """
    cipher = str.maketrans(string.ascii_lowercase, CRYPT, string.punctuation)
    text = plain_text.lower().replace(" ", "").translate(cipher)
    return " ".join((text[index:index+5] for index in range(0, len(text), 5)))


def decode(ciphered_text):
    """
    Decode the given text from an Atbash Cipher

    :param str plain_text: Atbash encoded text
    :return str: Decoded text
    """
    cipher = str.maketrans(CRYPT, string.ascii_lowercase)
    text = ciphered_text.replace(" ", "").translate(cipher)
    return text
