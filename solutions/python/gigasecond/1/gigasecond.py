"""
Giga second library
"""
import datetime

GIGA_SECOND = 10 ** 9

def add(moment: datetime) -> datetime:
    """
    Given a datetime moment, add a gigasecond

    :param datetime moment: The starting moment
    :param datetime: The new moment aftr a gigasecond
    """
    return moment + datetime.timedelta(seconds=GIGA_SECOND)