"""
Library for finding Primes
"""
import math

def prime(number: int) -> int:
    """
    Find the nth prime number

    Assumptions: We start at 2 and are leveraging the Sieve of Eratosthenes
    :param int number: The nth prime number to find
    :return int: The nth prime number value
    """
    if number < 1:
        raise ValueError('there is no zeroth prime')
    if number == 1:
        return 2
    if number < 6:
        return [2, 3, 5, 7, 11][number - 1]

    limit = int(number * (math.log(number) + math.log(math.log(number))))

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    count = 0

    for prime in range(2, limit + 1):
        if sieve[prime]:
            count += 1
            if count == number:
                return prime
            if prime * prime <= limit:
                sieve[prime*prime:limit + 1:prime] = [False] * len(range(prime*prime, limit+1, prime))