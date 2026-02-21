SQUARES = 64

def square(number):
    """
    Finds the number of doubled items at a certain square in a board

    :param int numnber: the position of the square on the board
    :return int: the value of items on the square
    """
    if 0 < number <= SQUARES:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    """
    Calculates the total sum of items alloted to from a board style calculation
    :return int: the total sum of items
    """
    return sum(map(square, range(1, SQUARES + 1)))