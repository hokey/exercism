"""
ETL library for game
"""

def transform(legacy_data):
    """
    Given legacy scoring data, convert the letter and points to a more universal system

    :param dict[int, list[str]] legacy_data:  legacy data table
    :return dict[str, int]: new data table
    """
    return {
        letter.lower(): point
        for point, letters in legacy_data.items()
        for letter in letters
    }
