"""
Cipher class for lowercase alphabetic items
"""
import secrets
from string import ascii_lowercase
from dataclasses import dataclass, field
from enum import Enum


class CipherDirection(Enum):
    ENCODE = 1
    DECODE = -1


@dataclass
class Cipher:
    """
    Cipher Vigenere
    """
    key: str = field(default_factory=lambda: "".join(secrets.choice(ascii_lowercase) for item in range(100)))
    def __post_init__(self):
        self._valid_chars = set(ascii_lowercase)
        self.validate(self.key)

    def _transform(self, text: str, direction: CipherDirection) -> str:
        self.validate(text)
        if not isinstance(direction, CipherDirection):
            raise ValueError("Direction must be valid CipherDirection")
        result = []
        for index, character in enumerate(text):
            ascii_index = ord(character) - ord('a')
            cipher_change = ord(self.key[index % len(self.key)]) - ord('a')
            result.append(chr((
                (ascii_index + direction.value * cipher_change) 
            ) % 26 + ord('a')))
        return "".join(result)
        
    def encode(self, text: str) -> str:
        """
        Encodes a given text with the local cipher key
        :param str text: The given text to encode
        :return str: The encoded text
        """
        return self._transform(text, CipherDirection.ENCODE)
        
    def decode(self, text: str) -> str:
        """
        Decodes the given text with the local cipher key
        :param str text: The given text to decode
        :return str: The decoded text
        """
        return self._transform(text, CipherDirection.DECODE)

    def validate(self, text: str) -> None:
        """
        Validates the text against ther rules for this class, in this case only lowercase letters

        :param str text: Text to validate against
        """
        if any(character not in self._valid_chars for character in text):
            raise ValueError("Must be lowercase alphabetic letters only")