"""
Palindrome Products Utility
"""
import math
from collections.abc import Iterable

def largest(min_factor: int = 0, max_factor: int = 0) -> tuple[int, Iterable[tuple[int, int]]]:
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return find_palindrome(min_factor, max_factor, True)


def smallest(min_factor: int = 0, max_factor: int = 0) -> tuple[int, Iterable[tuple[int, int]]]:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return find_palindrome(min_factor, max_factor, False)
    

def find_palindrome(min_factor: int = 0, max_factor: int = 0, find_max: bool = True) -> tuple[int, Iterable[tuple[int, int]]]:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param int min_factor: int with a default value of 0
    :param int max_factor: int
    :param int direction: The direction to search [1, -1]
    :return tuple: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    best: tuple[int, Iterable[tuple[int, int]]] | None = None
    factors = []

    # Control iteration direction
    outer = range(min_factor, max_factor + 1)
    if find_max:
        outer = reversed(outer)

    for i in outer:
        inner = range(i, max_factor + 1)
        if find_max:
            inner = reversed(inner)

        for j in inner:
            product = i * j

            # --- pruning ---
            if best is not None:
                if find_max and product < best:
                    break
                if not find_max and product > best:
                    break

            if str(product) == str(product)[::-1]:
                if best is None:
                    best = product
                    factors = [(i, j)]
                elif product == best:
                    factors.append((i, j))
                else:
                    best = product
                    factors = [(i, j)]

    return best, factors