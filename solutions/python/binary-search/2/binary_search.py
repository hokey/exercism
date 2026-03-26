"""
Binary search approaches
"""


def find(search_list, value):
    """
    Given a sorted list execute a binary search to see if a given value is in the list

    :param list[int] search_list: A sorted list of of numbers
    :param int value: the number we search the list
    """
    left = 0
    right = len(search_list)
    
    if right == 0:
        raise ValueError("value not in array")
    if search_list[-1] < value:
        raise ValueError("value not in array")

    result = None
    count = 0
    index = (right + left) // 2
    while right != left: 
        index = (right + left) // 2       
        if search_list[index] == value:
            result = index
            break

        if search_list[index] < value:
            if index == left:
                break
            left = index
        elif search_list[index] > value:
            if index == right:
                break
            right = index
        count = count + 1

    if result is None:
        raise ValueError("value not in array")
    
    return result
            

def binary_search(search_list, value):
    """
    Recursive binary search that I did first because I misred the instructions

    :param list[int] search_list: A sorted list of of numbers
    :param int value: the number we search the list
    """
    middle = len(search_list) // 2
    if search_list[middle] == value:
        return value
    if len(search_list) == 1:
        raise ValueError("value not in array")
    if search_list[middle] > value:
        return find(search_list[:middle], value)
    else:
        return find(search_list[middle:], value)