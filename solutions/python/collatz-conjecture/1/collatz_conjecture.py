def steps(number):
    """
    Determine the number of steps it takes in a Collatz Conjecture (tm)

    :param int number: the starting number for the conjecture
    :return int: the number of steps to reach the conjecture
    """
    if number == 1:
        return 0
    elif number > 1:
        if number % 2 == 0:
            return 1 + steps(int(number/2))
        else:
            return 1 + steps(number * 3 + 1)
    else:    
        raise ValueError("Only positive integers are allowed")