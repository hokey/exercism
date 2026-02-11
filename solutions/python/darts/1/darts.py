from math import sqrt

def score(x, y):
    """
    Calculate the score based on the Cartesian coordinates given for a dart board given the following scoring system:
        If the dart lands outside the target, player earns no points (0 points).
        If the dart lands in the outer circle of the target, player earns 1 point.
        If the dart lands in the middle circle of the target, player earns 5 points.
        If the dart lands in the inner circle of the target, player earns 10 points.

    :param int x: X Cartesian coordinate of the throw
    :param int y: Y Cartesian coordinate of the throw
    :return int: The score of the throw
    """
    radius = sqrt(x ** 2 + y ** 2)
    score = 0
    if 5 < radius <= 10:
        score = 1
    elif 1 < radius <= 5:
        score = 5
    elif 0 <= radius <= 1:
        score = 10
    return score