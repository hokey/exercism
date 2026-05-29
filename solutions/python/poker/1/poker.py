"""
Poker Hands
"""
from collections import Counter

RANKS = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
}


def parse_hand(hand_str: str) -> tuple[list[str], list[str]]:
    """
    Parses a string representing a Poker hand into a list of values and suits

    :param str hand_str: The string of the poker hand
    :return tuple[list[str],list[str]]: A tuple of the list of values and suits
    """
    cards = hand_str.split()
    values = []
    suits = []

    for card in cards:
        if len(card) == 3:  # 10X
            values.append(RANKS[card[:2]])
            suits.append(card[2])
        else:
            values.append(RANKS[card[0]])
            suits.append(card[1])

    values.sort(reverse=True)
    return values, suits


def score(hand_str: str) -> tuple[int,list[int]]:
    """
    Given a string representing a Poker hand, score it based on Poker rules

    :param str hand_str: The string of the poker hand
    :return tuple[int,list[int]]: The score and the list of values scored with
    """
    values, suits = parse_hand(hand_str)

    counts = Counter(values)
    freq = sorted(counts.values(), reverse=True)
    ordered = sorted(counts.items(), key=lambda counted: (-counted[1], -counted[0]))

    is_flush = len(set(suits)) == 1
    is_straight = len(set(values)) == 5 and max(values) - min(values) == 4

    # Handle A-2-3-4-5 straight
    if set(values) == {14, 5, 4, 3, 2}:
        is_straight = True
        values = [5, 4, 3, 2, 1]

    if is_straight and is_flush:
        return (8, values)
    if freq == [4, 1]:
        return (7, [value for value, _ in ordered])
    if freq == [3, 2]:
        return (6, [value for value, _ in ordered])
    if is_flush:
        return (5, values)
    if is_straight:
        return (4, values)
    if freq == [3, 1, 1]:
        return (3, [value for value, _ in ordered])
    if freq == [2, 2, 1]:
        return (2, [value for value, _ in ordered])
    if freq == [2, 1, 1, 1]:
        return (1, [value for value, _ in ordered])

    return (0, values)


def best_hands(hands: list[str]) -> list[str]:
    """
    Given a list of hands, pick the Poker winner(s)

    :param list[str]: List of poker hands
    :return list[str]: List of winners
    """
    scored = [(score(poker_hand), poker_hand) for poker_hand in hands]
    best = max(poker_score for poker_score, _ in scored)
    return [poker_hand for poker_score, poker_hand in scored if poker_score == best]