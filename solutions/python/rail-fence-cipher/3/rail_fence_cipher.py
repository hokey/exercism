"""
Rail Fence Cipher Utility
"""

def encode(message: str, rails: int) -> str:
    """
    Encodes a message using the Rail Fence Cipher

    :param str message: Message to encode
    :param int rails: The number for rails for the Cipher
    :return str: The encoded message
    """
    if rails < 1:
        raise ValueError("Must have positive number of rails")
    if rails == "":
        return ""
    if rails == 1:
        return message
    railway: list[list[str]] = [["."] * len(message) for index in range(rails)]
    zig: list[int] = list(range(0,rails)) + list(range(rails - 2, 0, -1))
    for index, character in enumerate(message):
        railway[zig[index % len(zig)]][index] = character
    return "".join(
        "".join(
            character for character in row if character != ".")
        for row in railway
    )
        
def decode(encoded_message: str, rails: int) -> str:
    """
    Decodes a message using the Rail Fence Cipher

    :param str message: Message to decode
    :param int rails: The number for rails for the Cipher
    :return str: The decoded message
    """
    if rails < 1:
        raise ValueError("Must have positive number of rails")
    if rails == "":
        return ""
    if rails == 1:
        return encoded_message
    rail_counts: list[int] = [0] * rails
    message_pieces: list[list[str]] = []
    zig: list[int] = list(range(0,rails)) + list(range(rails - 2, 0, -1))
    for index in range(len(encoded_message)):
        rail_counts[zig[index % len(zig)]] += 1
    index_space: int = 0
    for space in rail_counts:
        message_pieces.append(list(encoded_message[index_space:space+index_space]))
        index_space += space
    message: list[str] = []
    for index in range(len(encoded_message)):
        message.append(
            message_pieces[zig[index % len(zig)]].pop(0)
        )
    return "".join(message)