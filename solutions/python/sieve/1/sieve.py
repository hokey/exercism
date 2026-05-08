"""
Sieve of Eratosthenes
"""

def primes(limit: int) -> list[int]:
    """
    Use the Sieve of Eratosthenes to produce all primes up a limit

    :param int limit: Upper bound for list of primes
    :return list[int]: List of primes up to limit
    """
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if sieve[number]:
            if number * number <= limit:
                sieve[number * number : limit + 1 : number] = [False] * (((limit - number * number ) // number) + 1)
    return [index for index, number in enumerate(sieve) if number]
    