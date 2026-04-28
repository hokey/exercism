"""
Pythagorean Triplet Utility
"""
from math import gcd

def triplets_with_sum(number):
    """
    Given a number, calculate the Pythagorean triplets, a^2 + b^2 = c^2, where a + b + c = number.

    :param int number: The summation of the numbers involved in the Pythagorean triplet
    :return list[list[int]]: The list of Pythagorean triples
    """
    for m in range(2, int((number // 2) ** 0.5) + 1):
        if number % (2 * m) != 0:
            continue

        sm = number // (2 * m)

        for n in range(1, m):
            if (m + n) % 2 == 0:
                continue
            if gcd(m, n) != 1:
                continue
            if sm % (m + n) != 0:
                continue

            k = sm // (m + n)

            a = k * (m*m - n*n)
            b = k * (2*m*n)
            c = k * (m*m + n*n)

            if a > b:
                a, b = b, a

            yield [a, b, c]