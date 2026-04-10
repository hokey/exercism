"""
Factory library using primes
"""

def largest_prime_factor(number: int) -> int:
    """
    Find the largest prime factor for a number

    :param int number: Candidate number
    :return int: Largest prime factor of candidate
    """
    index = 2
    while index * index <= number:
        if number % index:
            index += 1
        else:
            number //= index
    return number
    
def factors(value: int) -> list[int]:
    """
    Find all the prime factors of a given number

    :param int number: Candidate number
    :return list[int]: The prime factors of the candidate number
    """
    prime_factors = []
    count = 0
    while value > 1:
        count = largest_prime_factor(value)
        prime_factors.append(count)
        value = int(value / count)
    
    return prime_factors[::-1]