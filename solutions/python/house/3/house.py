"""
Build me a house poem
"""

START = 'This is'
CONNECTOR = ' that'
END = '.'
STANZAS = [
    ' the house that Jack built',
    ' the malt',
    ' the rat',
    ' the cat',
    ' the dog',
    ' the cow with the crumpled horn',
    ' the maiden all forlorn',
    ' the man all tattered and torn',
    ' the priest all shaven and shorn',
    ' the rooster that crowed in the morn',
    ' the farmer sowing his corn',
    ' the horse and the hound and the horn'
]

STANZA_ACTIONS = [
    '',
    ' lay in',
    ' ate',
    ' killed',
    ' worried',
    ' tossed',
    ' milked',
    ' kissed',
    ' married',
    ' woke',
    ' kept',
    ' belonged to'
]


def recite(start_verse, end_verse):
    """
    Recite the poem based and where to start and how many further along we should go

    :param int start_verse: where to start for the recital poem
    :param int end_verse: where to end for the recital poem
    """
    recitals = []
    while True:
        recitals.append(START + build_recite(start_verse))
        start_verse += 1
        if start_verse > end_verse:
            break
    return recitals


def build_recite(length: int) -> str:
    """
    Build the poem with the specified length

    :param int length: How far down to do recite
    :return str: the recited poem
    """
    if length == 0:
        return END
    if length == 1:
        return STANZAS[length-1] + build_recite(length-1)
    return STANZAS[length-1] + CONNECTOR + STANZA_ACTIONS[length-1] + build_recite(length-1)