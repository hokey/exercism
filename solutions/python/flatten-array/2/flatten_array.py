"""
List flattener
"""

def flatten(iterable):
    """
    Flatten a given nested list to a list

    :param list iterable: nested list
    :param return: flattened list
    """
    result = []
    for item in iterable:
        if isinstance(item, list):
            result += flatten(item)
        elif item is not None:
            result.append(item)
    return result
