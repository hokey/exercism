"""
Yacht Dice Game
"""
from collections import Counter
# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if sorted(Counter(dice).values()) == [5] else 0
ONES = lambda dice: 1 * dice.count(1)
TWOS = lambda dice: 2 * dice.count(2)
THREES = lambda dice: 3 * dice.count(3)
FOURS = lambda dice: 4 * dice.count(4)
FIVES = lambda dice: 5 * dice.count(5)
SIXES = lambda dice: 6 * dice.count(6)
FULL_HOUSE = lambda dice: sum(dice) if sorted(Counter(dice).values()) == [2,3] else 0
FOUR_OF_A_KIND = lambda dice: next(
    (number * 4 for number, count in Counter(dice).items() if count >= 4),
    0
)
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    """
    Given the category score five rolled dice. It's the yacht dice game.

    :param list[int] dice: 5 rolled dice
    :param ? category: the category to store
    :return int: yacht score
    """
    return category(dice)