"""
Crypto Square Utility
"""
from string import punctuation
from math import sqrt, ceil

def cipher_text(plain_text):
    """
    Encode the given plain text into a sqare cipher

    :param str plain_text: Message to encode
    :return str: Encoded square cipher text
    """
    remove: dict[int, int | str | None] = str.maketrans("","", punctuation+" ")
    normalized_text: str = plain_text.translate(remove).lower()
    if not normalized_text:
        return normalized_text
    columns: int = ceil(sqrt(len(normalized_text)))
    square: list[str] = [normalized_text[index : index + columns].ljust(columns, " ") for index in range(0, len(normalized_text), columns) ]
    return " ".join(["".join(column) for column in zip(*square)])

            

    

    

    
    
    
