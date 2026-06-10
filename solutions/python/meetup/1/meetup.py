import calendar
from datetime import date, timedelta

teenth: list[int] = [13,14,15,16,17,18,19]
day_week_count: dict[str, int] = {
    "first": 0,
    "second": 1,
    "third": 2,
    "fourth": 3,
    "fifth": 4,
    "last": -1
}

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
    message: explanation of the error.

    """
    def __init__(self):
        """
        Constructor.
        """
        super().__init__("That day does not exist.")


def meetup(year, month, week, day_ofa_week: str) -> date:
    """
    Determines the date based on the given year, month, week, and day_of_week.  This includes teenth days
    :param int year: Year
    :param int month: Month
    :param str week: Week, can be first, second, third, fourth, last, teenth.
    :param str day_of_week: Day of the week
    :return date: date of the meetup:
    """
    day_ofa_week = day_ofa_week.lower().title()
    if day_ofa_week not in calendar.day_name:
        raise MeetupDayException()
    try:
        if week == "teenth":
            meetup_date: date = date(year, month, 13)
            for _ in range(7):
                if calendar.day_name[meetup_date.weekday()] == day_ofa_week:
                    return meetup_date
                meetup_date += timedelta(days=1)
        else:
            days_by_weekday: dict[str, list[int]] = {
                calendar.day_name[i]: []
                for i in range(7)
            }
            for week_item in calendar.monthcalendar(year, month):
                for weekday, day in enumerate(week_item):
                    if day:
                        days_by_weekday[calendar.day_name[weekday]].append(day)

            if week == "fifth" and len(days_by_weekday[day_ofa_week]) < 5:
                raise MeetupDayException()
            return date(year, month, days_by_weekday[day_ofa_week][day_week_count[week]])
    except Exception:
        raise MeetupDayException()