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
    row = None
    for index in range(0, distance + 1):
        if character == ord('A'):
            row = f'{chr(character): ^{padding}}'
        else:
            row = f'{chr(character) + ' ' * (1 + 2*(character - ord('A') - 1)) + chr(character): ^{padding}}'
        diamond.append(row)
        character += 1
    character -=1
    for index in range(0, distance):
        character -= 1
        if character == ord('A'):
            row = f'{chr(character): ^{padding}}'
        else:
            row = f'{chr(character) + ' ' * (1 + 2*(character - ord('A') - 1))  + chr(character): ^{padding}}'
        diamond.append(row)
        
    return diamond