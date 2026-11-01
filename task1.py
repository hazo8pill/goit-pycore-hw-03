"""Task 1: count the days between a given date and today."""

from datetime import date, datetime


class DateFormatError(ValueError):
    """Raised when a date string is not in 'YYYY-MM-DD' format."""


def get_days_from_today(date_str: str) -> int:
    """Return the number of days from `date_str` to today.

    Args:
        date_str: Date in 'YYYY-MM-DD' format, e.g. '2020-10-09'.

    Returns:
        Whole days between the date and today: positive for past dates,
        negative for future ones, 0 for today. Time of day is ignored.

    Raises:
        DateFormatError: If `date_str` is malformed, not a real date
            (e.g. '2021-02-30') or not a string.

    Examples:
        >>> get_days_from_today(date.today().isoformat())
        0
        >>> get_days_from_today('2021/10/09')
        Traceback (most recent call last):
        ...
        task1.DateFormatError: Invalid date '2021/10/09', expected 'YYYY-MM-DD'.
    """

    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except (ValueError, TypeError) as err:  
        raise DateFormatError(f"Invalid date {date_str!r}, expected 'YYYY-MM-DD'.") from err
    return (date.today() - input_date).days
