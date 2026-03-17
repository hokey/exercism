'''
Diamond utility
'''


def rows(letter: chr) -> list[str]:
    '''
    Print out a diamond shape based on the alphabetic upper case letter given

    :param chr letter: Target letter for diamond size
    :return list[str): List representing the diamond
    '''
    character = ord('A')
    distance = ord(letter) - character
    padding = distance * 2 + 1
    diamond = []
    for _ in range(0, distance + 1):
        diamond.append(row(character, padding))
        character += 1
    character -=1
    for _ in range(0, distance):
        character -= 1
        diamond.append(row(character, padding))
    return diamond


def row(character: int, padding: int) -> str:
    '''
    Given an ordinal integer representing a character and a padding boundary, produce a centered string

    :param int character: ordinal integer of a character
    :param int padding: the padding or width of the string
    :return str: center, padded string with characters 
    '''
    if character == ord('A'):
        return f'{chr(character): ^{padding}}'
    else:
        return f'{chr(character) + ' ' * (1 + 2*(character - ord('A') - 1))  + chr(character): ^{padding}}'