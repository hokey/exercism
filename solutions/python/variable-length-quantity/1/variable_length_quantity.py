"""
VLQ - Variable Length Quantity utility
"""

def encode(numbers: list[int | str]) -> list[int | str]:
    """
    Encodes a given number in the VLQ sytle format

    :param list[int | str] numbers: list of numbers in hex, bin, or int format to encode
    :return list[int | str]: list of encoded numbers
    """
    result = []

    for n in numbers:
        if n == 0x0:
            result.append(0x0)
            continue
        bytes_ = []

        while n > 0:
            bytes_.append(n & 0x7F)
            n >>= 7

        bytes_.reverse()
        for i in range(len(bytes_) - 1):
            bytes_[i] |= 0x80

        result.extend(bytes_)

    return result


def decode(bytes_: list[int | str]) -> list[int | str]:
    """
    Given a list of bytes, decode them in to a hexadecimal number

    :param list[int | str]: The list of bytes to decode
    :return list[int | str]: The list of decoded bytes
    """
    result = []
    current = 0

    for b in bytes_:
        current = (current << 7) | (b & 0x7F)

        if (b & 0x80) == 0:
            result.append(current)
            current = 0

    if not result:
        raise ValueError("incomplete sequence")
    return result
