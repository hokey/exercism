"""
Twelve Days of Christmas Library
"""
DAYS = [
    "a Partridge in a Pear Tree.", 
    "two Turtle Doves, ", 
    "three French Hens, ", 
    "four Calling Birds, ", 
    "five Gold Rings, ", 
    "six Geese-a-Laying, ", 
    "seven Swans-a-Swimming, ", 
    "eight Maids-a-Milking, ", 
    "nine Ladies Dancing, ", 
    "ten Lords-a-Leaping, ", 
    "eleven Pipers Piping, ", 
    "twelve Drummers Drumming, "
]
START_PREFIX =  "On the "
DAY_NAMES = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]  
START_SUFFIX = " day of Christmas my true love gave to me: "
AND = "and "

def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Recite parts of the Twelve Days of Christmas given the starting and eding verse
    """
    recitals = []
    for day_number in range(start_verse, end_verse+1):
        recitals.append(
            recite_day(day_number)
        )
    return recitals

def recite_day(day_number: int) -> str:
    """
    Recite the day part of the Twelve Days of Christmas

    :param int day_number: Day to recite
    :return str: The day part
    """
    recital = []
    recital.append(
        f"{START_PREFIX}{DAY_NAMES[day_number-1]}{START_SUFFIX}"
    )
    for day in range(day_number-1, -1, -1):
        if day == 0 and day_number > 1:
            recital.append(AND)
        recital.append(
            f"{DAYS[day]}"
        )
    return "".join(recital)