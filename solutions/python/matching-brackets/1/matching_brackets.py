"""
Matching Brackets
"""

def is_paired(input_string: str) -> bool:
    """
    Check to see if brackets are properly paired given a string

    :param str input_string: text to check
    :return bool: Correct pairing
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in input_string:
        if char in pairs.values():  # opening
            stack.append(char)
        elif char in pairs:  # closing
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack