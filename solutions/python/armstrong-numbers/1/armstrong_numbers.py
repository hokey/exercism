def is_armstrong_number(number):
    """
    Determines if a given number is an Armstrong number

    :param int number: the number in question
    :return bool: if the number is an Armstrong number
    """
    return number == sum(map(lambda x: int(x) ** len(list(str(number))), list(str(number))))