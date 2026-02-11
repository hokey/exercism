def factors(number):
    """
    Get a list of the factors for a number

    :param number: The number to derive the factors
    :return list: the list of factors for a number
    """
    factor = []
    if number == 0:
        raise ValueError("Factors must be a non zero number")
    for count in range(1,number+1):
        if number % count == 0:
            factor.append(count)
    return factor


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
        
    factor_sum = sum(factors(number)[:-1])
    if factor_sum > number:
        return "abundant"
    elif factor_sum < number:
        return "deficient"
    else:
        return "perfect"