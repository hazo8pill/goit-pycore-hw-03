from datetime import date, datetime


class DateFormatError(ValueError):
    """Raised when a date string is not in 'YYYY-MM-DD' format."""


def get_days_from_today(date_str: str) -> int:
    """Return days from `date_str` ('YYYY-MM-DD') to today.

    Positive for past dates, negative for future ones. Time of day is ignored.
    Raises DateFormatError on malformed input.
    """
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except (ValueError, TypeError) as err:
        raise DateFormatError(f"Invalid date {date_str!r}, expected 'YYYY-MM-DD'.") from err
    return (date.today() - input_date).days
