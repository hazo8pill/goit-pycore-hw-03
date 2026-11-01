from datetime import date, datetime


class DateFormatError(ValueError):
    """Raised when a date string is not in 'YYYY-MM-DD' format."""


def get_days_from_today(date_str: str) -> int:
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except (ValueError, TypeError) as err:
        raise DateFormatError(f"Invalid date {date_str!r}, expected 'YYYY-MM-DD'.") from err

    return (date.today() - input_date).days
