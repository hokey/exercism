'''
Diamond utility
'''


def rows(letter: str) -> list[str]:
    '''
    Print out a diamond shape based on the alphabetic upper case letter given

    :param str letter: Target letter for diamond size
    :return list[str): List representing the diamond
    '''
    character = ord('A')
    distance = ord(letter) - character
    padding = distance * 2 + 1
    diamond = []
    for _ in range(0, distance + 1):
        diamond.append(row(character, padding))
        character += 1
    return diamond + diamond[0:-1][::-1]


def row(character: int, padding: int) -> str:
    '''
    Given an ordinal integer representing a character and a padding boundary, produce a centered string

    :param int character: ordinal integer of a character
    :param int padding: the padding or width of the string
    :return str: center, padded string with characters 
    '''
    if character == ord('A'):
        return f'{chr(character): ^{padding}}'
    return f'{chr(character) + ' ' * (1 + 2*(character - ord('A') - 1))  + chr(character): ^{padding}}'