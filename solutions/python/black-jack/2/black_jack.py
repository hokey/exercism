"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
SUITS = ['J','Q','K']
SUIT_VALUE = 10
ACE_VALUES = [1,11]
DOUBLE_DOWN_VALUES = [9,10,11]
POINT_THRESHOLD = 21


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    result = 0
    if card in SUITS:
        result = SUIT_VALUE
    elif card is 'A':
        result = ACE_VALUES[0]
    else:
        result = int(card)
    return result

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    result = card_one, card_two
    if value_of_card(card_one) > value_of_card(card_two):
        result = card_one
    elif value_of_card(card_two) > value_of_card(card_one):
        result = card_two
    return result


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    result = ACE_VALUES[1]
    if card_one is 'A' and value_of_card(card_two) + ACE_VALUES[1] + ACE_VALUES[1] > POINT_THRESHOLD:
        result = ACE_VALUES[0]
    elif card_two is 'A' and value_of_card(card_one) + ACE_VALUES[1] + ACE_VALUES[1] > POINT_THRESHOLD:
        result = ACE_VALUES[0]
    elif value_of_card(card_one) + value_of_card(card_two) + ACE_VALUES[1] > POINT_THRESHOLD:
        result = ACE_VALUES[0]
    return result


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    result = False
    if card_one is 'A' and value_of_card(card_two) is SUIT_VALUE:
        result = True
    elif card_two is 'A' and value_of_card(card_one) is SUIT_VALUE:
        result = True
    return result


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    result = False
    if card_one in SUITS and card_two in SUITS:
        result = True
    elif card_one == card_two:
        result = True
    return result


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    result = False
    if value_of_card(card_one) + value_of_card(card_two) in DOUBLE_DOWN_VALUES:
        result = True
    return result
