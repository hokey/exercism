"""
VLQ - Variable Length Quantity utility
"""

def encode(numbers: list[int]) -> list[int]:
    """
    Encodes a given number in the VLQ sytle format

    :param list[int | str] numbers: list of numbers in hex, bin, or int format to encode
    :return list[int | str]: list of encoded numbers
    """
    result = []

    for number in numbers:
        if number == 0:
            result.append(0)
            continue

        chunks = []
        current_value = number

        while current_value > 0:
            chunks.append(current_value & 0x7F)
            current_value >>= 7

        chunks.reverse()

        for index in range(len(chunks) - 1):
            chunks[index] |= 0x80

        result.extend(chunks)

    return result


def decode(bytes_: list[int | str]) -> list[int | str]:
    """
    Given a list of bytes, decode them in to a hexadecimal number

    :param list[int | str]: The list of bytes to decode
    :return list[int | str]: The list of decoded bytes
    """
    result = []
    current_value = 0

    for byte in bytes_:
        current_value = (current_value << 7) | (byte & 0x7F)

        # Last byte of this number
        if (byte & 0x80) == 0:
            result.append(current_value)
            current_value = 0

    if not result:
        raise ValueError("incomplete sequence")

    return result
