"""
Library of list operations
"""

def append(list1: list[int], list2: list[int]) -> list[int]:
    """
    Add a list to another list

    :param list[int] list1: The first list to add
    :param list[int] list2: The second list to add
    :return list[int]: The list of added lists
    """
    return list1 + list2


def concat(lists: list[list[int]]) -> list[int]:
    """
    Give a list of lists, flatten them out to a single list

    :param list[list[int]] lists: The nested list of lists
    :return list[int]: The concatenated list
    """
    concat_list = []
    for item in lists:
        if isinstance(item, list):
            concat_list = concat_list + item
        else:
            concat_list.append(item)
    return concat_list


def filter(function, list):
    """
    Filter out the items in the list based on the function given

    :param lambda function: The lambda to filter against
    :param list[int]: The list to filter
    :return list[int]: The filtered list
    """
    filter_list = []
    for item in list:
        if function(item):
            filter_list.append(item)
    return filter_list


def length(list):
    """
    Return the lenght of the given list

    :param list list: The list to find the length of
    :return int: The length of the list
    """
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    """
    Given the function, apply it to each item in the list

    :param lambda function: The function each item the list should be applied
    :param list list: The list the function should run against
    :return list: The list with each element having the applied function
    """
    map_list = []
    for item in list:
        map_list.append(function(item))
    return map_list


def foldl(function, list, initial):
    """
    Apply the given function to the initial for each item in the list from left to right

    :param lambda function: The function to apply given each item in the list
    :param list list: The list of items to apply to the function
    :param int initial: The initial value to integrate with the function on and list
    """
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    """
    Apply the given function to the initial for each item in the list from right to left

    :param lambda function: The function to apply given each item in the list
    :param list list: The list of items to apply to the function
    :param int initial: The initial value to integrate with the function on and list
    """
    for index in range(len(list)-1, -1, -1):
        initial = function(initial, list[index])
    return initial


def reverse(list):
    """
    Given a list, return it in reversed order

    :param list list: The initial list
    :return list: The initial list in reversed order
    """
    return list[::-1]