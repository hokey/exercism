def leap_year(year):
    """ 
    Determine if year is a leap year

    :param year: int - the given year
    :return: bool - True if divisible by for except for multiples of 100 where it has to be divisible by 400
        
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
