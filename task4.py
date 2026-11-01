"""Task 4: find colleagues to congratulate on their birthday this week."""

from datetime import date, datetime, timedelta

DATE_FORMAT = '%Y.%m.%d'
DAYS_AHEAD = 7


def _in_year(birthday: date, year: int) -> date:
    """Return `birthday` moved to `year`; 29 Feb becomes 1 Mar in non-leap years."""
    try:
        return birthday.replace(year=year)
    except ValueError:
        return date(year, 3, 1)


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """Return who to congratulate in the next 7 days, including today.

    Birthdays falling on Saturday or Sunday are congratulated on the
    following Monday.

    Args:
        users: Dicts with 'name' and 'birthday' ('YYYY.MM.DD') keys.

    Returns:
        Dicts with 'name' and 'congratulation_date' ('YYYY.MM.DD') keys.

    Example:
        If today is 2024.01.22:
        >>> get_upcoming_birthdays([
        ...     {'name': 'John Doe', 'birthday': '1985.01.23'},
        ...     {'name': 'Jane Smith', 'birthday': '1990.01.27'},
        ... ])  # doctest: +SKIP
        [{'name': 'John Doe', 'congratulation_date': '2024.01.23'},
         {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}]
    """

    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], DATE_FORMAT).date()
        birthday_this_year = _in_year(birthday, today.year)
        if birthday_this_year < today:
            birthday_this_year = _in_year(birthday, today.year + 1)

        if (birthday_this_year - today).days >= DAYS_AHEAD:
            continue

        congratulation_date = birthday_this_year
        if congratulation_date.weekday() >= 5:  
            congratulation_date += timedelta(days=7 - congratulation_date.weekday())

        upcoming.append({
            'name': user['name'],
            'congratulation_date': congratulation_date.strftime(DATE_FORMAT),
        })

    return upcoming
