def is_valid(isbn):
    """
    Determine if the given string is a valid ISBN number

    :param string isbn: Test string to validate
    :return bool: If the test string is a valid ISBN number
    """
    isbn_sum = 0
    factor = 10
    test_isbn = isbn.replace("-", "")
    if len(test_isbn) != 10:
        return False
    for character in test_isbn:
        if character in ("X", "x"):
            if factor > 1:
                return False
            isbn_sum += factor * 10
        elif character.isdigit():
            isbn_sum += factor * int(character)
        else:
            return False
        factor = factor - 1
    return isbn_sum % 11 == 0